#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from collections import defaultdict

holidays = defaultdict(list)

#--------------------------------------------------------------------
# Add a holiday to the calendar.
def add_holiday(year, month, day, name):
    holidays[datetime.date(year, month, day)].append(name)
