#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import os, sys
import yaml
import sqlite3
from datetime import datetime
from serverside.exceptions.customexceptions import ETGeneralException, ETInputValueException
from serverside.sqlinterface.sqlinterface import SqlInterface

class ExpenseSqlInterface(SqlInterface):
    """ SQLite3 interface for expense """

    def __del__(self):
        """ destructor """
        pass
