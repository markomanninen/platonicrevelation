#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: __init__.py

try:
	from .main import helper, concat
except:
	from main import helper, concat
try:
	from .svg import svg
except:
	from svg import svg
try:
	from .table import table
except:
	from table import table

__version__ = "0.0.2"