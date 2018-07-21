#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import os, sys
import yaml
from sqlite3 import DatabaseError, DataError
from serverside.exceptions.customexceptions import ETGeneralException, ETInputValueException
from serverside.businesslogic.bl_expense import BlExpense

class Expense:
    """ Expense Main Class """

    _blexpense = None

    def __init__(self):
        """ constructor """
        self._blexpense = BlExpense()


    def get_all_expenses(self):
        """ get all the expenses """
        pass


    def __del__(self):
        """ destructor """
        pass
