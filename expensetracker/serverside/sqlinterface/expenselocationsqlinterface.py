#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import os, sys
import yaml
import sqlite3
from datetime import datetime
from serverside.exceptions.customexceptions import ETGeneralException, ETInputValueException
from serverside.sqlinterface.sqlinterface import SqlInterface

class ExpenseLocationSqlInterface(SqlInterface):
    """ SQLite3 interface for Expense Location """

    def get_all_expense_locations(self, getall= False, locid= 0,
        findbyid= False, searchparams = []):
        """
            Description: get the expense locations

            Parameters:
                - getall: flag when set will retrieve all locations
                - locid: ID of the expense location
                - findbyid: flag when set will retrieve the location of the given id
                - searchparams: list of search keys.
                    Example: [{'columnname': 'EL_StoreName', 'operator': '=', 'value': 'REWE' }, ]

            Returns:
                List of expense locations if found, else None
                Raises exceptions on errors
        """
        try:
            if not getall and not findbyid and not searchparams:
                raise ETInputValueException("Invalid parameters provided to get the expense locations")
        except sqlite3.DataError:
            raise
        except sqlite3.DatabaseError:
            raise
        except ETInputValueException:
            raise
        except ETGeneralException:
            raise
        except Exception:
            raise
        # return nothing
        return None


    def archive_expense_type(self, locid: int, user: str):
        """
            Description: archive the given expense location

            Parameters:
                - locid: ID of the expense location that has to be archived
                - user: name of the user archiving the record

            Returns:
                True if successfully archived, else None
                Raises exceptions on errors
        """
        pass


    def __del__(self):
        """ destructor """
        pass
