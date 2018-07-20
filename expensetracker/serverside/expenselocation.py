#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import os, sys
import yaml
from sqlite3 import DatabaseError, DataError
from serverside.exceptions.customexceptions import ETGeneralException, ETInputValueException
from serverside.businesslogic.bl_expenselocation import BlExpenseLocation

class ExpenseLocation:
    """ Expense Location Main Class """

    def __init__(self):
        """ constructor """
        pass


    def get_all_expense_locations(self):
        """ get all the expense locations """
        pass


    def __del__(self):
        """ destructor """
        pass
