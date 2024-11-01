#!/usr/bin/env python3

"""
Debugger script to initiate an interactive debugging session.
"""

from models.__init__ import CONN, CURSOR
import ipdb

# Start the debugger
ipdb.set_trace()
