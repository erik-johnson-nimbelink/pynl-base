###
 # \file
 #
 # \brief AT interface utilities
 #
 # (C) NimbeLink Corp. 2020
 #
 # All rights reserved except as explicitly granted in the license agreement
 # between NimbeLink Corp. and the designated licensee.  No other use or
 # disclosure of this software is permitted. Portions of this software may be
 # subject to third party license terms as specified in this software, and such
 # portions are excluded from the preceding copyright notice of NimbeLink Corp.
 ##

from nimbelink.cell.at.result import Result

class Response(object):
    """A response to an AT command
    """

    DefaultNewLine = "\r\n"
    """The default line endings to use"""

    def __init__(self, result, output = None, newLine = None):
        """Creates a response

        :param self:
            Self
        :param result:
            The result of the response
        :param output:
            Generic output, sans result indicator

        :return none:
        """

        if output == None:
            output = ""

        if newLine == None:
            newLine = Response.DefaultNewLine

        self.result = result
        self.output = output

        self._newLine = newLine

    def __bool__(self):
        """Gets a boolean representation of the response

        :param self:
            Self

        :return True:
            Response was a success
        :return False:
            Response was a failure
        """

        if self.result:
            return True

        return False

    def __str__(self):
        """Gets a string representation of the response

        :param self:
            Self

        :return String:
            Us
        """

        string = ""

        if len(self.output) > 0:
            string += self.output + self._newLine

        string += "{}".format(self.result)

        return string

    @staticmethod
    def makeFromString(string, newLine = None):
        """Creates a new response from output

        :param string:
            The raw string output to parse
        :param newLine:
            The newline style to use

        :return None:
            Failed to parse response
        :return Response:
            The response
        """

        if newLine == None:
            newLine = Response.DefaultNewLine

        # If there is a final \r\n at the very end, discard it
        if string.endswith(newLine):
            string = string[:-2]

        # Find the last occurrence of \r\n, which would come before our result
        resultStart = string.rfind(newLine)

        # If that failed, this isn't a valid response
        if resultStart == -1:
            return None

        # Split the string into generic output and the final result
        output = string[:resultStart]
        result = string[resultStart + 2:]

        # Make the result from the last line
        result = Result.makeFromString(string = result)

        # If that failed, this isn't a valid response
        if result == None:
            return None

        return Response(output = output, result = result)
