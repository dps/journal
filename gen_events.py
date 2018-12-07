#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from collections import defaultdict

events = defaultdict(list)

#--------------------------------------------------------------------
# Add an event to the calendar.  If the event is a holiday, pass 'True'
# as the Holiday flag to have the calendar day greyed out
def add_event(year, month, day, name, holiday = False):
    events[datetime.date(year, month, day)].append((name, holiday))
