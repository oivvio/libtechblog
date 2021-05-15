# -*- coding: utf-8 -*-

import os
import shutil
import sys
import datetime
from pathlib import Path
from pathlib import PurePath
import yaml
import textwrap

from invoke import task
from invoke.util import cd
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer

from PIL import Image, ImageDraw, ImageFont

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


def preflight_check():
    if not (Path("tasks.py").exists() and Path("pelicanconf.py").exists()):
        print("Please run tasks from the root project folder")
        exit()

    print()


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


def make_presentation_poster(path, fontpath):

    # IMAGE_WIDTH = 1920
    IMAGE_WIDTH = 1600
    # IMAGE_HEIGHT = 1080
    IMAGE_HEIGHT = 900

    FONT_SIZE_TITLE = int(IMAGE_HEIGHT * 0.1)
    FONT_SIZE_BODY = int(IMAGE_HEIGHT * 0.05)
    LINE_HEIGHT_BODY = FONT_SIZE_BODY * 1.2
    PADDING_SIDE = IMAGE_WIDTH * 0.05
    PADDING_TOP = IMAGE_WIDTH * 0.03

    base = path.name
    imagepath = path.joinpath("image.png")
    textpath = path.joinpath("text.yml")

    output = path.joinpath("cover.jpg")

    assert imagepath.exists()
    assert textpath.exists()

    with open(textpath) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        data = yaml.load(file, Loader=yaml.FullLoader)
    print(data["title"])
    print(data["body"])

    # original layer
    original = Image.open(imagepath)
    size = (IMAGE_WIDTH, IMAGE_HEIGHT)
    original = original.resize(size, resample=Image.LANCZOS)
    original = original.convert("RGBA")

    # middle  layer
    middle = Image.new("RGBA", (IMAGE_WIDTH, IMAGE_HEIGHT), "BLACK")

    # blend them
    image = Image.blend(original, middle, 0.7)

    # convert back to RGB
    image = image.convert("RGB")
    draw = ImageDraw.Draw(image)

    # draw title
    font = ImageFont.truetype(fontpath.as_posix(), FONT_SIZE_TITLE)
    draw.text(
        # (MARGIN, MARGIN - top_offset + i * line_height),
        (PADDING_SIDE, PADDING_TOP),
        data["title"],
        font=font,
        fill="WHITE",
    )

    # draw body
    font = ImageFont.truetype(fontpath.as_posix(), FONT_SIZE_BODY)
    lines = textwrap.wrap(data["body"], 30)
    for index, line in enumerate(lines, start=0):
        BODY_PADDING_TOP = PADDING_TOP + FONT_SIZE_TITLE + (LINE_HEIGHT_BODY * index)
        draw.text(
            (PADDING_SIDE, BODY_PADDING_TOP),
            line,
            font=font,
            fill="WHITE",
        )

    # Save image
    image.save(
        open(output, "wb"),
        "JPEG",
        optimize=True,
        quality=75,
        progressive=True,
    )


#


@task
def make_video_posters(ctx):
    """ Generate the video posters """
    preflight_check()
    fontpath = Path("content/extra/FiraSans-Bold.ttf")
    assert fontpath.exists()

    path = Path("content/videoposters")

    for child in path.iterdir():
        make_presentation_poster(child, fontpath)
