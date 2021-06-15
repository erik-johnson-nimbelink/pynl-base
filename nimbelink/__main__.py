"""
The main entry point for the NimbeLink package

(C) NimbeLink Corp. 2021

All rights reserved except as explicitly granted in the license agreement
between NimbeLink Corp. and the designated licensee. No other use or disclosure
of this software is permitted. Portions of this software may be subject to third
party license terms as specified in this software, and such portions are
excluded from the preceding copyright notice of NimbeLink Corp.
"""

import logging

import nimbelink.command as command

class NlCommand(command.Command):
    """Our root NimbeLink command
    """

    def __init__(self):
        """Creates a new NimbeLink command

        :param self:
            Self

        :return none:
        """

        super().__init__(
            name = "nimbelink",
            help = "provides NimbeLink Python package functionality",
            description =
                """Handles NimbeLink Python packages
                """,
            subCommands = command.__commands__
        )

        # Get a logger for all of our commands
        root = logging.getLogger(command.Command.LoggerNamespace)

        # Commands get 'info'-level logging
        root.setLevel(logging.INFO)

        # Make a handler for logging to standard output
        handler = logging.StreamHandler()

        # Add the handler to our command loggers
        root.addHandler(handler)

def main():
    """Handles commands

    :param none:

    :return none:
    """

    NlCommand().parseAndRun()

if __name__ == "__main__":
    main()
