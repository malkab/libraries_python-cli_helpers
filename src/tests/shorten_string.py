#!/usr/bin/env python3
# coding=UTF8

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cli_helpers.src.cli_helpers import shorten_string

s0 = "Aute deserunt voluptate ut sunt sunt pariatur tempor eiusmod proident"
s1 = "Esse veniam ut nisi officia est"

print("Len s0: %s > %s -Final" % (len(s0), shorten_string(s0, 40, 10)));
print("Len s1: %s > %s -Final" % (len(s1), shorten_string(s1, 40, 10)));
