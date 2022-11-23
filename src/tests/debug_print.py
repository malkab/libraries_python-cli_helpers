#!/usr/bin/env python3
# coding=UTF8

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cli_helpers.src.cli_helpers import debug_print

debug_print("The Mighty Descriptor", "The Phenomenal Message")

debug_print("The Magnificient sys Package", sys)

debug_print("And Now Without Message!")

debug_print("And Even With Several Messages!", "What An Incredible Feat", "This Is Unbelievable")
