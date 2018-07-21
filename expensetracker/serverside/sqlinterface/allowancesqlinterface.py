#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import os, sys
import yaml
import sqlite3
from datetime import datetime
from serverside.exceptions.customexceptions import ETGeneralException, ETInputValueException
from serverside.sqlinterface.sqlinterface import SqlInterface

class AllowanceSqlInterface(SqlInterface):
    """ SQLite3 interface for Allowances """

    def get_allowances(self, getall= False, specificmonth= 0, specificyear= 0
        allowanceid=0, findbyid=False):
        """
            Description: get the allowances

            Parameters:
                - getall: get all allowances. default: False
                - specificmonth: get the allowance for specific month. defailt: 0
                - specificyear: get the allowance for specific year. default: 0

            Returns:
                List of allowance if found, else None.
                Raises exceptions on errors
        """
        try:
            if findbyid and allowanceid <= 0:
                raise ETInputValueException("Invalid allowance id: %s" % allowanceid)

            query = "SELECT * FROM Allowance WHERE IS_DELETED='False'"
            queryparams = None
            if not getall:
                if findbyid:
                    query = " AND Allowance_ID=:a_id"
                    queryparams = { "a_id": allowanceid, }
                else:
                    query += " AND Allowance_Month=:month AND Allowance_Year=:year"
                    month = datetime.now().month
                    year = datetime.now().year
                    # specific month and year
                    if specificmonth > 0:
                        month = specificmonth
                    if specificyear > 0:
                        year = specificyear
                    queryparams = { "month": month, "year": year, }
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


    def add_allowance(self, month: int, year: int, amount: float, currency: str, user: str):
        """
            Description: insert the allowance with the given data

            Parameters:
                - month: month for which the allowance has to be inserted
                - year: year for which the allowance has to be inserted
                - amount: allowance amount
                - currency: currency of allowance amount
                - user: user adding the allowance

            Returns:
                True if inserted successfully, else None.
                Raises exceptions on errors
        """
        try:
            if not month >= 1 and month <= 12:
                raise ETInputValueException("Invalid Month provided: %s" % month)
            if len(str(year)) < 4:
                raise ETInputValueException("Invalid Year provided: %s" % year)
            if currency != "EUR":
                raise ETInputValueException("Currency must be EUR. %s given" % currency)
            if user.lower() not in ["krishna", "indira"]:
                raise ETInputValueException("Invalid user: %s" % user)
            if amount < 200 and amount > 400:
                raise ETInputValueException("Allowance amount must be between 200 and 400. %s given" % amount)

            if self.get_allowances(specificmonth=month, specificyear=year):
                raise ETGeneralException("Allowance for month %s year %s already exists. Try updating" % (month, year))

            query = ("INSERT INTO Allowance (Allowance_Month, Allowance_Year, "
                "Allowance_Amount, Allowance_Currency, CREATEDBY, MODIFIEDBY) "
                "VALUES(?, ?, ?, ?, ?, ?)")
            queryparams = (month, year, amount, currency, user)
            return self._execute_query(query, queryparams, fetch=False)
        except sqlite3.DatabaseError:
            raise
        except sqlite3.DataError:
            raise
        except ETInputValueException:
            raise
        except ETGeneralException:
            raise
        except Exception:
            raise
        # return nothing
        return None


    def update_allowance(self, allowanceid: int, amount: float, user: str):
        """ update the allowance with the given parameters """
        try:
            if allowanceid <= 0:
                raise ETInputValueException("Invalid allowance id: %s" % allowanceid)
            if amount < 200 and amount > 400:
                raise ETInputValueException("Allowance amount must be between 200 and 400. %s given" % amount)

            if not self.get_allowances(findbyid=True, allowanceid=allowanceid):
                raise ETGeneralException("Allowance doesn't exist or is archived. ID: %s" % allowanceid)

            query = ("UPDATE Allowance SET Allowance_Amount=:a_amt, "
                "MODIFIEDBY=:a_user, MODIFIEDON=datetime('now') "
                "WHERE Allowance_ID=:a_id;")
            queryparams = { "a_amt": amount, "a_user": user, "a_id": allowanceid, }
            return self._execute_query(query, queryparams, False)
        except sqlite3.DatabaseError:
            raise
        except sqlite3.DataError:
            raise
        except ETInputValueException:
            raise
        except ETGeneralException:
            raise
        except Exception:
            raise
        # return nothing
        return None


    def archive_allowance(self, allowanceid: int, user: str):
        """
            Description: archive the given allowance

            Parameters:
                - allowanceid: ID of the allowance that has to be archived
                - user: name of the user archiving the record

            Returns:
                True if successfully archived, else None
                Raises exceptions on errors
        """
        try:
            if allowanceid <= 0:
                raise ETInputValueException("Invalid allowance id: %s" % allowanceid)

            if not self.get_allowances(findbyid=True, allowanceid=allowanceid):
                raise ETGeneralException("Allowance doesn't exist or is already archived. ID: %s" % allowanceid)

            query = ("UPDATE Allowance SET IS_DELETED='True', "
                "MODIFIEDON=datetime('now'), MODIFIEDBY=:a_user "
                "WHERE Allowance_ID=:a_id;")
            queryparams = { "a_user": user, "a_id": allowanceid, }
            return self._execute_query(query, queryparams, fetch=False)
        except sqlite3.DatabaseError:
            raise
        except sqlite3.DataError:
            raise
        except ETInputValueException:
            raise
        except ETGeneralException:
            raise
        except Exception:
            raise
        # return nothing
        return None


    def get_archived_allowance(self):
        """ get all the allowances that are archived """
        try:
            query = "SELECT * FROM Allowance WHERE IS_DELETED='True';"
            return self._execute_query(query)
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


    def __del__(self):
        """ destructor """
        pass
