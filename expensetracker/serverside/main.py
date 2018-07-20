#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import os, sys
import yaml
from sqlite3 import DatabaseError, DataError
from serverside.exceptions.customexceptions import ETGeneralException, ETInputValueException
from serverside.allowance import Allowance
from serverside.expensetype import ExpenseType
from serverside.expenselocation import ExpenseLocation
from serverside.expense import Expense

class Main(Allowance, ExpenseType, ExpenseLocation, Expense):
    """ Expense Tracker Application """
    _appconfig = []

    def __init__(self):
        """ constructor """
        self._read_app_config()


    def _read_app_config(self):
        """ private function to read the application configuration """
        from serverside.config.configuration import Configuration
        try:
            conf = Configuration()
            self._appconfig = conf.get_config(configfilename = "app_config.yaml")
        except Exception:
            raise


    def __del__(self):
        """ destructor """
        pass
