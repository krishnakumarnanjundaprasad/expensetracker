#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import os, sys
import datetime
from serverside.main import Main

global g_expensetracker_project_dir
g_expensetracker_project_dir = os.path.dirname(os.path.abspath(__file__))
if g_expensetracker_project_dir not in sys.path:
    sys.path.append(g_expensetracker_project_dir)

# header
sys.stdout.write("".ljust(80, "-"))
sys.stdout.write("\n")
sys.stdout.write("Expense Tracker".center(80))
sys.stdout.write("\n")
sys.stdout.write("".ljust(80, "-"))
sys.stdout.write("\n")

#current date
sys.stdout.write("%s\n\n" % datetime.datetime.now())

# initialization
mainobj = Main()
mainobj.get_current_month_allowance()

# footer
sys.stdout.write("\n")
sys.stdout.write("".ljust(80, "-"))
sys.stdout.write("\n")
