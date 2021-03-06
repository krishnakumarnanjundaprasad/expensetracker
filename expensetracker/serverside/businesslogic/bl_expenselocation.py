#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import os, sys
from sqlite3 import DatabaseError, DataError
from serverside.sqlinterface.expenselocationsqlinterface import ExpenseLocationSqlInterface
from serverside.exceptions.customexceptions import ETGeneralException, ETInputValueException

class BlExpenseLocation:
    """ Business logic definitions for expense locations """

    _sqli = None

    def __init__(self):
        """ constructor """
        self._sqli = ExpenseLocationSqlInterface()

    def __del__(self):
        """ destructor """
        pass
