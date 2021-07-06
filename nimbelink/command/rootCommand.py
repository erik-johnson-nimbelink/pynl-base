"""
A 'root' command

(C) NimbeLink Corp. 2021

All rights reserved except as explicitly granted in the license agreement
between NimbeLink Corp. and the designated licensee. No other use or disclosure
of this software is permitted. Portions of this software may be subject to third
party license terms as specified in this software, and such portions are
excluded from the preceding copyright notice of NimbeLink Corp.
"""

import argparse
import logging
import typing

from .command import Command

class RootCommand(Command):
    """A 'root' command

    A 'root' command acts as the initial entry point for the NimbeLink command
    stack. A 'root' command is expected -- and intended -- to handle any
    NimbeLink-specific setup operations, such as providing any universal command
    flags, logging setup, etc.

    This class is not intended to be instantiated directly -- that is, there
    should not be any object created of the RootCommand class:

        command = RootCommand(...)

    Rather, this class is intended to provide a single, command source for some
    common root command operations. It should be used like so:

        class MyCommand(RootCommand):
            ...

            def addArguments(...):
                super().addArguments(...)
                ...

            def runCommand(...):
                super().runCommand(...)
                ...

        command = MyCommand()

    If the command inheriting from RootCommand -- 'MyCommand' in the example
    above -- is only or mostly wrapping sub-commands, you do not need to
    implement addArguments() and/or runCommand() if you do not have
    MyCommand-specific actions to take.
    """

    def addArguments(self, parser: argparse.ArgumentParser) -> None:
        """Adds arguments for our command

        :param self:
            Self
        :param parser:
            The parser to add arguments to

        :return none:
        """

        parser.add_argument(
            "-v", "--verbose",
            dest = "verbose",
            action = "count",
            default = 0,
            required = False,
            help = "Use verbose output"
        )

    def runCommand(self, args: typing.List[object]) -> None:
        """Runs the root command

        :param self:
            Self
        :param args:
            Our arguments

        :return None:
            Command not handled
        """

        # Get a logger for everything
        root = logging.getLogger()

        # Scale our logging verbosity according to the 'verbose' argument(s)
        if args.verbose > 0:
            level = logging.DEBUG
        else:
            level = logging.INFO

        # Apply our logging level
        root.setLevel(level)

        # Make a handler for logging to standard output
        handler = logging.StreamHandler()

        # Add the handler to our root loggers
        root.addHandler(handler)

        return None
