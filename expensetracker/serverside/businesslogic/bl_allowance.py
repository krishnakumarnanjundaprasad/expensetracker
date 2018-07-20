#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import os, sys
from sqlite3 import DatabaseError, DataError
from serverside.sqlinterface.allowancesqlinterface import AllowanceSqlInterface
from serverside.exceptions.customexceptions import ETGeneralException, ETInputValueException

class BlAllowance:
    """ Business logic definitions for allowance """

    _sqli = None

    def __init__(self):
        """ constructor """
        self._sqli = AllowanceSqlInterface()


    def get_all_allowances(self):
        """ public method to get all allowances """
        try:
            return self._sqli.get_allowances(getall = True)
        except DatabaseError:
            raise
        except DataError:
            raise
        except Exception:
            raise

        return None


    def get_current_month_allowance(self):
        """ public method to get the current month's allowance """
        try:
            return self._sqli.get_allowances()
        except DatabaseError:
            raise
        except DataError:
            raise
        except Exception:
            raise

        return None


    def get_specific_month_allowance(self, month: int, year: int):
        """ public method to get specific month's allowance """
        try:
            if not month >= 1 and month <= 12:
                raise ETInputValueException("Invalid Month provided: %s" % month)
            if len(str(year)) < 4:
                raise ETInputValueException("Invalid Year provided: %s" % year)

            return self._sqli.get_allowances(specificmonth = month, specificyear = year)
        except DatabaseError:
            raise
        except DataError:
            raise
        except ETInputValueException:
            raise
        except Exception:
            raise

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

            return self._sqli.add_allowance(
                month= month, year= year, amount= amount, currency= currency, user= user
            )
        except DatabaseError:
            raise
        except DataError:
            raise
        except ETInputValueException:
            raise
        except Exception:
            raise

        return None


    def archive_allowance(self, allowanceid: int, user: str):
        """ archives the allowance with the given id """
        try:
            if allowanceid <= 0:
                raise ETInputValueException("Invalid allowance id: %s" % allowanceid)

            return self._sqli.archive_allowance(allowanceid, user)
        except DatabaseError:
            raise
        except DataError:
            raise
        except ETInputValueException:
            raise
        except Exception:
            raise

        return None


    def __del__(self):
        """ destructor """
        pass
