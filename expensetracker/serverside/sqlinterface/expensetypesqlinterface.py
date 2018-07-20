#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import os, sys
import yaml
import sqlite3
from datetime import datetime
from serverside.exceptions.customexceptions import ETGeneralException, ETInputValueException
from serverside.sqlinterface.sqlinterface import SqlInterface

class ExpenseTypeSqlInterface(SqlInterface):
    """ SQLite3 Interface for Expense Types """

    def get_expense_types(self, specificid= 0, specificname= "",
        findbyid= False, partialname= False):
        """
            Description: get the expense types

            Parameters:
                - specificid: get the expense type for the given id. default: 0
                - specificname: get the expense type for the given name. default: empty
                - findbyid: flag to search by id. default: False
                - partialname: flag to search for partial name. default: False

            Returns:
                List of expense type(s) if found, else None
                Raises exception on error
        """
        try:
            query = "SELECT * FROM ExpenseType WHERE IS_DELETED='False'"
            queryparams = None
            if findbyid and specificid <= 0:
                raise ETInputValueException("Invalid type id: %s" % specificid)
            if findbyid and specificid > 0:
                query += " AND ET_ID=:et_id"
                queryparams = { "et_id": specifictype, }
            elif specificname and partialname:
                query += " AND ET_Name like :et_name"
                queryparams = { "et_name": "%%%s%%" % specificname, }
            elif specificname:
                query += " AND ET_Name=:et_name"
                queryparams = { "et_name": specificname, }
            query += ";"
            return self._execute_query(query, queryparams)
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


    def add_expense_type(self, typename: str, user: str):
        """
            Description: insert a new expense type with the given name

            Parameters:
                - typename: name of expense type
                - user: name of user inserting the record

            Returns:
                True if inserted successfully, else None
                Raises exceptions on errors
        """
        try:
            if not typename:
                raise ETInputValueException("Type name cannot be empty")
            if self.get_expense_type(specificname=typename, partialname=True):
                raise ETGeneralException("Expense Type %s already exists" % typename)
            query = ("INSERT INTO ExpenseType (ET_Name, CREATEDBY, MODIFIEDBY) "
                "VALUES (?, ?, ?)")
            queryparams = (typename, user, user)
            return self._execute_query(query, queryparams, fetch=False)
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


    def update_expense_type(self, typeid: int, typename: str, user: str):
        """
            Description: Update the expense type

            Parameters:
                - typeid: expense type ID for which the name has to be updated.
                - typename: name to be updated with
                - user: name of the user updating the record

            Returns:
                True if update is successful, else None
                Raises execptions on errors
        """
        try:
            if typeid <= 0:
                raise ETInputValueException("Invalid type id: %s" % typeid)
            if not typename:
                raise ETInputValueException("Type name cannot be empty")
            if not self.get_expense_type(specificid=typeid, findbyid=True):
                raise ETGeneralException("Type ID: %s doesn't exist or this record is archived!" % typeid)
            if self.get_expense_type(specificname=typename):
                raise ETGeneralException("Type name: %s already exists!" % typename)
            query = ("UPDATE ExpenseType SET ET_Name=:et_name, "
                "MODIFIEDBY=:et_user, MODIFIEDON=datetime('now') "
                "WHERE ET_ID=:et_id;")
            queryparams = { "et_name": typename, "et_user": user, "et_id": typeid, }
            return self._execute_query(query, queryparams, fetch=False)
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


    def archive_expense_type(self, typeid: int, user: str):
        """
            Description: archive the given expense type

            Parameters:
                - typeid: ID of the expense type to be archived
                - user: name of the user archiving the record

            Returns:
                True if successfully archived, else None
                Raises execptions on errors
        """
        try:
            if typeid <= 0:
                raise ETInputValueException("Invalid type id: %s" % typeid)
            if not self.get_expense_type(specificid=typeid, findbyid=True):
                raise ETGeneralException("Type ID: %s doesn't exist or is already archived!" % typeid)
            query = ("UPDATE ExpenseType SET IS_DELETED='True', "
                "MODIFIEDBY=:et_user, MODIFIEDON=datetime('now') "
                "WHERE ET_ID=:et_id;")
            queryparams = { "et_user": user, "et_id": typeid, }
            return self._execute_query(query, queryparams, fetch=False)
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


    def get_archived_expense_types(self):
        """ get all the expense types that are archived """
        try:
            query = "SELECT * FROM ExpenseType WHERE IS_DELETED='True';"
            return self._execute_query(query)
        except sqlite3.DataError:
            raise
        except sqlite3.DatabaseError:
            raise
        except ETInputValueException:
            raise
        except Exception:
            raise
        # return nothing
        return None


    def __del__(self):
        """ destructor """
        pass
