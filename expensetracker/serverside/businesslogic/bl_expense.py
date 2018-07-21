#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import os, sys
from sqlite3 import DatabaseError, DataError
from serverside.sqlinterface.expensesqlinterface import ExpenseSqlInterface
from serverside.exceptions.customexceptions import ETGeneralException, ETInputValueException

class BlExpense:
    """ Business logic definitions for expense """

    _sqli = None

    def __init__(self):
        """ constructor """
        self._sqli = ExpenseSqlInterface()


    def __del__(self):
        """ destructor """
        pass
