#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import os, sys
from sqlite3 import DatabaseError, DataError
from serverside.sqlinterface.expensetypesqlinterface import ExpenseTypeSqlInterface
from serverside.exceptions.customexceptions import ETGeneralException, ETInputValueException

class BlExpenseType:
    """ Business logic to handle expense type related functions """

    _sqli = None

    def __init__(self):
        """ constructor """
        self._sqli = ExpenseTypeSqlInterface()


    def get_expense_type_by_id(self, typeid: int):
        """
            Description: Get the expense type by id

            Parameters:
                - typeid: ID to retrieve the expense type

            Returns:
                Expense type if found, else None
                Raises exceptions on errors
        """
        try:
            pass
        except sqlite3.DatabaseError:
            raise
        except sqlite3.DataError:
            raise
        except ETInputValueException:
            raise
        except Exception:
            raise
        # return nothing
        return None


    def get_expense_type_by_name(self, typename: str, partialname= False):
        """
            Description: Get the expense type by given name

            Parameters:
                - typename: name of the expense type
                - partialname: flag to indicate whether the given name is partial

            Returns:
                Expense type(s) if found, else None
                Raises exceptions on errors
        """
        try:
            pass
        except sqlite3.DatabaseError:
            raise
        except sqlite3.DataError:
            raise
        except ETInputValueException:
            raise
        except Exception:
            raise
        # return nothing
        return None


    def get_all_expense_types(self):
        """ Function to get all the expense types """
        try:
            return self._sqli.get_expense_types(getall=True)
        except sqlite3.DatabaseError:
            raise
        except sqlite3.DataError:
            raise
        except ETInputValueException:
            raise
        except Exception:
            raise
        # return nothing
        return None


    def get_all_archived_expense_types(self):
        """ function to get all the archived expense types """
        try:
            return self._sqli.get_archived_expense_types()
        except sqlite3.DatabaseError:
            raise
        except sqlite3.DataError:
            raise
        except ETInputValueException:
            raise
        except Exception:
            raise
        # return nothing
        return None


    def __def__(self):
        """ destructor """
        pass
