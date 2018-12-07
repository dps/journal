#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from collections import defaultdict

events = defaultdict(list)

#--------------------------------------------------------------------
# Add an event to the calendar.
def add_event(year, month, day, name):
    events[datetime.date(year, month, day)].append(name)
