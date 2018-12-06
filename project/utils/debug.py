
from __future__ import division
import sys
from bdb import BdbQuit

sys.dont_write_btyecode = True


def info(type, value, tb):
    if type is BdbQuit:
        exit(-1)

    if type is KeyboardInterrupt:
        exit(-1)

    if hasattr(sys, 'ps1') or not sys.stderr.isatty():
        # we are in interactive mode or we don't have a tty-like
        # device, so we call the default hook
        sys.__excepthook__(type, value, tb)
    else:
        import traceback, pdb
        # we are NOT in interactive mode, print the exception…
        traceback.print_exception(type, value, tb)
        print
        # …then start the debugger in post-mortem mode.
        # pdb.pm() # deprecated
        pdb.post_mortem(tb) # more “modern”

sys.excepthook = info