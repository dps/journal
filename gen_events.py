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

def greg_easter(year):
    '''
    function to calculate easter given the year
    taken from https://www.tondering.dk/claus/cal/easter.php
    '''
    g = year%19
    c = int(year/100)
    h = (c-int(c/4)-int((8*c+13)/25)+19*g+15)%30
    i = h - int(h/28)*(1-int(29/(h+1))*int((21-g)/11))
    j = (year+int(year/4)+i+2-c+int(c/4))%7
    l = i-j
    easter_m = 3+int((l+40)/44)
    easter_d = l+28-31*int(easter_m/4)
    return easter_m,easter_d
