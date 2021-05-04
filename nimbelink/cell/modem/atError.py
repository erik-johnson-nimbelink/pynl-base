"""
An error on a Skywire modem

(C) NimbeLink Corp. 2021

All rights reserved except as explicitly granted in the license agreement
between NimbeLink Corp. and the designated licensee. No other use or disclosure
of this software is permitted. Portions of this software may be subject to third
party license terms as specified in this software, and such portions are
excluded from the preceding copyright notice of NimbeLink Corp.
"""

class AtError(Exception):
    """An error that occurs when an AT command fails with an error
    """

    def __init__(self, response, message = None):
        """Creates a new AT error

        :param self:
            Self
        :param response:
            The AT command's response
        :param message:
            A message about the failure

        :return none:
        """

        if message == None:
            message = "AT command failed"

        if response != None:
            message += ": {}".format(response)

        self._response = response
        self._message = message

        super(AtError, self).__init__(self._message)