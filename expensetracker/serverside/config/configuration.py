#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import os, sys, yaml

class Configuration:
    """ configuration interface of the application """

    _confdir = ""

    def __init__(self):
        """ constructor """
        self._confdir = os.path.dirname(os.path.abspath(__file__))


    def get_config(self, configfilename):
        """ function that reads and returns the file contents of config file """
        if not configfilename:
            return None

        configfile = "%s/etc/%s" % (self._confdir, configfilename)
        if not os.path.exists(configfile):
            return None

        with open(configfile, "r") as conffile:
            return yaml.load(conffile)


    def __del__(self):
        """ destructor """
        pass
