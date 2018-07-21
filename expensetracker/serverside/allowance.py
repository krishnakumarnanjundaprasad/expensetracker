#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import os, sys
import yaml
from sqlite3 import DatabaseError, DataError
from serverside.exceptions.customexceptions import ETGeneralException, ETInputValueException
from serverside.businesslogic.bl_allowance import BlAllowance

class Allowance:
    """ Allowance Main Class """

    _blallowance = None

    def __init__(self):
        """ constructor """
        self._blallowance = BlAllowance()


    def get_current_month_allowance(self):
        """ main function to get the allowance of current month """
        try:
            allowance = self._blallowance.get_current_month_allowance()
            if allowance:
                sys.stdout.write("Allowance: %s %s\n" % (
                    allowance[0]["Allowance_Amount"],
                    allowance[0]["Allowance_Currency"]
                ))
            else:
                sys.stdout.write("No allowance for this month\n")
        except DatabaseError:
            raise
        except DataError:
            raise
        except ETInputValueException:
            raise
        except Exception:
            raise


    def get_all_allowances(self):
        """ main function to get all the unarchived allowances """
        try:
            allowances = self._blallowance.get_all_allowances()
            if allowances:
                pass
            else:
                sys.stdout.write("No allowances allocated till now!\n")
        except DatabaseError:
            raise
        except DataError:
            raise
        except ETInputValueException:
            raise
        except Exception:
            raise


    def get_all_archived_allowances(self):
        """ main function to get all archived allowances """
        try:
            archivedallowances = self._blallowance.get_archived_allowance()
        except DatabaseError:
            raise
        except DataError:
            raise
        except ETInputValueException:
            raise
        except Exception:
            raise


    def __del__(self):
        """ destructor """
        pass
