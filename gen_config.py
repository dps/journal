#!/usr/bin/python
# -*- coding: utf-8 -*-
import locale
import gen_events as events

# Year to generate for
year = 2019

# True if the week starts on Monday (European convention), False if it starts on Sunday.
week_starts_on_Monday = True

# Locale -- uncomment one only, use utf-8 encoding ONLY
#
#locale.setlocale(locale.LC_ALL, 'en_AU.utf-8')      # Australia
locale.setlocale(locale.LC_ALL, 'en_GB.utf-8')      # Great Britain
#locale.setlocale(locale.LC_ALL, 'fr_FR.utf-8')      # France
#locale.setlocale(locale.LC_ALL, 'de_DE.utf-8')      # Deuchland
#locale.setlocale(locale.LC_ALL, 'es_ES.utf-8')      # Espaniol

# Define "Week" and "Notes" words, being used in the Weekly Planner
Week_locale = 'Week'
HowGo_locale = 'How did it go?'
Notes_locale = 'Notes'
Week_Goals_locale = 'Week Goals'
Physical_Activity_locale = 'Exercise'

# What events should be built in to the calendar?
# Pass in the year, month, day, event name, and True if the day is a holiday
# and should be greyed out on the calendar
events.add_event(year, 1, 1, "New Year's Day", True)
events.add_event(year + 1, 1, 1, "New Year's Day", True)

