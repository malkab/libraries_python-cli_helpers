#!/usr/bin/env python3
# coding=UTF8

from cli_helpers.src.cli_helpers import shortenString

s0 = "Aute deserunt voluptate ut sunt sunt pariatur tempor eiusmod proident"
s1 = "Esse veniam ut nisi officia est"

print("Len s0: %s > %s -Final" % (len(s0), shortenString(s0, 40, 10)));
print("Len s1: %s > %s -Final" % (len(s1), shortenString(s1, 40, 10)));
