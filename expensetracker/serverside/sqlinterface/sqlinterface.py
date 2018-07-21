#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import os, sys
import yaml
import sqlite3
from datetime import datetime
from serverside.exceptions.customexceptions import ETInputValueException

class SqlInterface:
    """ Interface between SQLite3 and Business Logic """

    # class data members
    _db = ""

    # class member functions

    def __init__(self):
        """ constructor """
        # get the db file
        self._get_db_file()


    def _get_db_file(self):
        """ private function to retrieve the SQLite database file """
        from serverside.config.configuration import Configuration
        import platform
        self._db = ""
        try:
            conf = Configuration()
            sqlconfig = conf.get_config(configfilename = "sqlconfig.yaml")
            if sqlconfig:
                # get the dblocation based on the OS platform
                currentplatform = platform.system()
                if not currentplatform:
                    raise Exception("Unknown OS platform. Cannot operate under such platform")

                dblocation = ""
                if currentplatform.lower() == "windows":
                    dblocation = sqlconfig["connection-properties"]["windowsdblocation"]
                elif currentplatform.lower() == "linux":
                    dblocation = sqlconfig["connection-properties"]["linuxdblocation"]
                else:
                    raise Exception("Platform: %s is not yet supported. Can only operate on Windows or Linux" % currentplatform)

                sqldbfilepath = "%s/%s" % (
                    dblocation,
                    sqlconfig["connection-properties"]["dbname"]
                )
                if os.path.exists(sqldbfilepath):
                    self._db = sqldbfilepath
        except Exception:
            raise


    def _connect_to_sqlite3(self):
        """ private function to connect to the SQLite3 database """
        try:
            conn = sqlite3.connect(self._db)
            return conn
        except Exception as e:
            raise sqlite3.DatabaseError("Error occurred while connecting to %s\n%s\n" % (self._db, e))


    def _disconnect_from_sqlite3(self, conn=None):
        """ private function to release the database connection """
        if not conn:
            return

        try:
            conn.close()
        except Exception as e:
            raise sqlite3.DatabaseError("Error occurred while closing connection\n%s\n" % e)


    def _execute_query(self, query, queryparams=(), fetch=True):
        """
            Description: function to execute the given query with(out) params

            Access Permissions:
                This is a private/protected function.
                Only this class or classes inheriting this class can access this function

            Parameters:
                query: query to be executed
                queryparams: parameters to be supplied to execute the query. default: empty tuple
                fetch: flag to indicate whether to execute the query as fetch or commit. default: True

            Returns:
                fetch=True: List of result if found, else None
                fetch=False: True if query success committed, else None
        """
        conn = None
        try:
            if not query:
                raise ETInputValueException("Query cannot be empty!")
            conn = self._connect_to_sqlite3()
            sqlcursor = conn.cursor()
            if queryparams == None:
                queryparams = ()
            # execute the given query with the given params
            sqlcursor.execute(query, queryparams)
            # fetch the results if the flag is set
            if fetch:
                results = sqlcursor.fetchall()
                if results:
                    columnnames = map(lambda x: x[0], sqlcursor.description)
                    resultlist = []
                    for row in results:
                        rowdict = dict(zip(columnnames, row))
                        resultlist.append(rowdict)
                    return resultlist
            else:
                # commit the changes and return true
                conn.commit()
                return True
        except sqlite3.DatabaseError:
            raise
        except sqlite3.DataError:
            raise
        except ETInputValueException:
            raise
        except Exception:
            raise
        finally:
            self._disconnect_from_sqlite3(conn)
        # return nothing
        return None


    def __del__(self):
        """ destructor """
        pass
