Title: Emacs might not be doomed after all.
Date: 2020-10-08

I started using [Emacs](https://www.gnu.org/software/emacs/) in 1999 when I
ditched Windows for Linux. Over the years I've made attempts at getting into
using modern IDE:s but it's never lasted long. Part of it is habit but a big
reason is that I really enjoy hanging out in the terminal and if you're into
editors that run in the terminal Emacs is undeniably one of a very small number
of serious contenders.

The one thing that always bothered me about Emacs though is the lack of cohesion
between all the parts. Emacs is a great tool surrounded by a rich ecosystem, but
with no one in charge of making sure all of the pieces fit together that task
falls upon the user. Configuring Emacs always felt like rolling your own Linux
distro, a fun learning experience for a while and a frustrating
time sink in the long run.

## A Vim detour

In about 2012 I got fed up with trying to get different elisp modules to work
together (and also the snarkiness in the Emacs community at the time) and decided to give
[Vim](https://www.vim.org/) a try. I seem to remember that Vim was very much in
vogue back then. Speakers a tech conferences wielding MacBooks covered in
stickers used Vim. Rails-people used Vim. Vim felt like someone who hung out in a
coffee shop ordering macchiatos and Emacs felt more and more like a neckbeard
guy with bad personal hygiene.

Then in 2017 I came back to Emacs. Probably because Vim was plagued by the same
basic problem as Emacs. Coming back I was pleasantly surprised that there where
now [package managers](https://melpa.org) for Emacs. That made a big difference.
I got my config working for the languages I used and fiddled as little as
possible with it.

## The Language Server Protocol

But over the last few years a much more important shift has swept across the
editor landscape &mdash; the advent of the [Language Server
Protocol](https://langserver.org) coming out of [Visual Studio
Code](https://code.visualstudio.com/). The basic idea of the language server is
that you can build one tool for understanding and manipulating let's say Python
source code and then have different editors talk to that tool over LSP. Instead
of having 100 different editors figure out ways to work with Python, you build
one tool that does it and have all the editors talk to that tool over the same
protocol. I first experienced the bliss that is LSP using the TypeScript
language server with `lsp-mode` in Emacs. For some reason it worked out of the
box and provided an editor experience that was way ahead of what I would have
with other languages in Emacs. Since then I've tried numerous times to get
`lsp-mode` to work with the different Python lsp offerings but to no avail. This
has been going on for a couple of years.

## The advent of Emacs distributions

Last night I decided to give it another try. Temporarily throwing out all of my
Emacs config files and worked an hour at getting a basic working
`lsp-mode` &amp; Python configuration in place. Failing to get it to work and
googling for solutions I came across [Doom
Emacs](https://github.com/hlissner/doom-emacs). I'd heard about Doom Emacs and
it's sibling [Spacemacs](https://www.spacemacs.org/) before, but I'd thought of
them mainly as tools for making Emacs more palatable to new users coming over
from Vim. But Doom Emacs and Spacemacs are primarily Emacs distributions in the
same way that Debian and Ubuntu are Linux distributions. Having a distribution
around an editor might seem like overkill, but in the case of Emacs that is
sometimes referred to as an OS, it makes perfect sense.

After an hour or two of fiddling with Doom Emacs not only did I have `lsp-mode`
working with Python but I also had pretty much everything else that I care about
in Emacs back in place. My old Emacs config, measured 1200+ lines of code broken
up over 20 files. My Doom Emacs config is 320 lines of pre-generated highly
commented and readable configuration. Using `diff` I figured out that I changed
exactly 17 (seventeen) lines out of those 320 to get Emacs to behave the way I
want. It's only been a day but it's safe to say that I will not be going back to
vanilla Emacs any time soon.

## The future

What does all of this mean for the future? There's been some recent discussion
in the Emacs community about [how to attract new
users](https://lwn.net/Articles/832311/). Doom Emacs and Spacemacs gets
mentions. On the one hand, they are credited with easing the learning curve for
new users and on the other, they are critizied for not contributing back upstream.

To my mind, it's clear that the distros are here to stay and that they breathe
fresh air into the Emacs ecosystem. In combination with the rise of LSP they
provide Emacs a much-needed shot in the arm. I've been thinking of Emacs as a
problem in my development workflow for quite some time, thinking that sooner or
later I'll have to rip off the band aid and shift to using modern IDE:s,
thinking that the productivity gap between Emacs and modern tools would just get
wider. My experience with Doom Emacs finally having a Python-editing experience
on par with VSCode turned that thought on it's head. I now feel that I can
probably stay with Emacs another 20 years.

Then again it might be that editors will gradually be reduced to being clients
of language servers over the coming years. Replicating the immense ecosystem
around Emacs and starting afresh with a new terminal-based editor never seemed
plausible before. LSP has completely changed that and it's now very likely that
we will see a slew of modern "editors" that mostly act as packaging and
distribution for a curated list of language servers and a thin client to talk to
them.
