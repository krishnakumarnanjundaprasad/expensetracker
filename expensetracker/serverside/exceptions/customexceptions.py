#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

class ETException(Exception):
    """ All Expense Tracker Exceptions """
    def __str__(self):
        return self.arg[0]


class ETGeneralException(ETException):
    """ General Expense Tracker Exceptions """
    def __init__(self, reason):
        self.reason = reason
        super(ETGeneralException, self).__init__(reason)


    def __str__(self):
        return self.reason


    def plain_text(self):
        return "General Error"


    def title(self):
        return "Error"


class ETInputValueException(ETException):
    """ All exceptions related to the input values provided in the application """
    def __init__(self, reason):
        self.reason = reason
        super(ETInputValueException, self).__init__(reason)


    def __str__(self):
        return self.reason


    def plain_text(self):
        return "General Error"


    def title(self):
        return "Error"
