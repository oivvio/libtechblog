# -*- coding: utf-8 -*-

import os
import shutil
import sys
import datetime

from invoke import task
from invoke.util import cd
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer

CONFIG = {
    # Local path configuration (can be absolute or relative to tasks.py)
    "deploy_path": "output",
    # Remote server configuration
    "production": "oivvio@collins.liberationtech.net",
    "production_port": "2224",
    "dest_path": "/home/oivvio/sites/libtechstatic/www",
    # Port for `serve`
    "port": 9002,
}


@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG["deploy_path"]):
        shutil.rmtree(CONFIG["deploy_path"])
        os.makedirs(CONFIG["deploy_path"])


@task
def build(c, relative_urls=False):
    """Build local version of site"""
    relative_urls = " --relative-urls " if relative_urls else " "
    c.run(f"pelican -s pelicanconf.py {relative_urls}")


@task
def rebuild(c, relative_urls=False):
    """`build` with the delete switch"""
    relative_urls = " --relative-urls " if relative_urls else " "
    c.run(f"pelican -d -s pelicanconf.py {relative_urls}")


@task
def regenerate(c, relative_urls=False):
    """Automatically regenerate site upon file modification"""
    relative_urls = " --relative-urls " if relative_urls else " "
    c.run("pelican -r -s pelicanconf.py {relative_urls}")


@task
def watch_and_serve(c, relative_urls=True):
    """Watch content for changes and serve on PORT """
    relative_urls = " --relative-urls " if relative_urls else " "

    cmd = f"pelican -s pelicanconf.py {relative_urls}"
    print(cmd)
    c.run(cmd, pty=True)

    cmd = f"pelican --autoreload -s pelicanconf.py {relative_urls} --listen --port {CONFIG['port']} --bind '0.0.0.0'"
    print(cmd)
    c.run(cmd, pty=True)


@task
def serve(c):
    """Serve site at http://localhost:port/"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG["deploy_path"], ("", CONFIG["port"]), ComplexHTTPRequestHandler
    )

    sys.stderr.write("Serving on port {port} ...\n".format(**CONFIG))
    server.serve_forever()


@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)


@task
def preview(c):
    """Build production version of site"""
    c.run("pelican -s publishconf.py")


@task
def publish(c):
    """Publish to production via rsync"""

    c.run("pelican -s publishconf.py")

    cmd = (
        "rsync --delete -pthrvz -c "
        "{} -e 'ssh -p {production_port}' {production}:{dest_path}".format(
            CONFIG["deploy_path"].rstrip("/") + "/", **CONFIG
        )
    )

    print(cmd)
    c.run(cmd)


@task
def update_theme(ctx, watch=False):
    """Run this after editing the sass/html in ../themes/pelican-ghostwriter"""

    # Reinstall theme
    cmd = "pelican-themes --upgrade ../themes/pelican-ghostwriter"
    ctx.run(cmd)

    # Run sass
    cmd = "sassc ../themes/pelican-ghostwriter/sass/main.scss   > ../themes/pelican-ghostwriter/static/css/main.css"
    ctx.run(cmd)
