#!/usr/bin/python
# -*- coding: utf-8 -*-
import locale
import sys
import math
import calendar
import datetime

import gen_config as cfg
import gen_holidays as holidays

# DIY Calendar
#
# gen_Current_Macros.py -- generated specific macros for given year and locale
# ver 0.5.2, 23 Sep 2008
#
# This script prints out the LaTeX support macros for the DIY Planner, for the given year
#
# There are two types of functions:
#       - gen_macro_<...>       -- generates a LaTeX macro, page and language independent
#       - write_out_<...>           -- write out LaTeX files
#

#------------------------------------------------------------------------------

# using abbrevs in LaTeX macro names (can't use the locales here, using generic POSIX)
# abbrev and name coincide for May, marking the long with 'L'
day_abbr_C = ['Mon',    'Tue',     'Wed',       'Thu',      'Fri',    'Sat',      'Sun']
day_name_C = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
month_abbr_C = ['', 'Jan',     'Feb',      'Mar',   'Apr',   'May',  'Jun',  'Jul',  'Aug',    'Sep',       'Oct',     'Nov',      'Dec']
month_name_C = ['', 'January', 'February', 'March', 'April', 'MayL', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#--------------------------------------------------------------------
# Generate & write out locale (language dependent) macros
#
# defines:
#       \Mon ...,
#       \MonA ... as 'M' ... (one letter)
#       \January ...
#       \Jan ...

def write_out_i18n_macros(file):
    i18n_macros_FH = open(file, 'w')
    i18n_macros_FH.writelines('% Internationalization macros\n\n')

    i18n_macros_FH.writelines('\\newcommand{\\Week}{' + cfg.Week_locale + '}\n')
    i18n_macros_FH.writelines('\\newcommand{\\HowGo}{' + cfg.HowGo_locale + '}\n')
    i18n_macros_FH.writelines('\\newcommand{\\Notes}{' + cfg.Notes_locale + '}\n')
    i18n_macros_FH.writelines('\\newcommand{\\WeekGoals}{' + cfg.Week_Goals_locale + '}\n')
    i18n_macros_FH.writelines('\\newcommand{\\Exercise}{' + cfg.Physical_Activity_locale + '}\n')
    i18n_macros_FH.writelines('\n')

    if cfg.week_starts_on_Monday:
        weekday_range = range(0,7)
    else:
        weekday_range = range(-1,6)
    # capitalize 1-letter day abbrevs, bot not the rest (?)
    i18n_macros_FH.writelines('% Weekdays\n')
    for d in weekday_range:
        # i18n_macros_FH.writelines('\\newcommand{\\' + day_name_C[d] + '}{' + calendar.day_name[d].capitalize() + '}\n')
        i18n_macros_FH.writelines('\\newcommand{\\' + day_name_C[d] + '}{' + calendar.day_name[d] + '}\n')
    i18n_macros_FH.writelines('\n')

    i18n_macros_FH.writelines('% Weekdays in order based on cfg.week_starts_on_Monday\n')
    i = ord('A')
    for d in weekday_range:
        # i18n_macros_FH.writelines('\\newcommand{\\' + day_name_C[d] + '}{' + calendar.day_name[d].capitalize() + '}\n')
        i18n_macros_FH.writelines('\\newcommand{\\Day' + chr(i) + '}{' + calendar.day_name[d] + '}\n')
        i = i + 1
    i18n_macros_FH.writelines('\n')

    i18n_macros_FH.writelines('% Weekdays: abbreviated 2/3 letters\n')
    for d in weekday_range:
        # i18n_macros_FH.writelines('\\newcommand{\\' + day_abbr_C[d] + '}{' + calendar.day_abbr[d].capitalize() + '}\n')
        i18n_macros_FH.writelines('\\newcommand{\\' + day_abbr_C[d] + '}{' + calendar.day_abbr[d] + '}\n')
    i18n_macros_FH.writelines('\n')

    i18n_macros_FH.writelines('% Weekdays: abbreviated 1 letter\n')
    for d in weekday_range:
         i18n_macros_FH.writelines('\\newcommand{\\' + day_abbr_C[d] + 'A' + '}{' + calendar.day_abbr[d][0].capitalize() + '}\n')
    i18n_macros_FH.writelines('\n')

    i18n_macros_FH.writelines('% Months: abbreviated 3 letters\n')
    for m in range(1,13):
        # i18n_macros_FH.writelines('\\newcommand{\\' + month_abbr_C[m] + '}{' + calendar.month_abbr[m].capitalize() + '}\n')
        i18n_macros_FH.writelines('\\newcommand{\\' + month_abbr_C[m] + '}{' + calendar.month_abbr[m] + '}\n')
    i18n_macros_FH.writelines('\n')

    i18n_macros_FH.writelines('% Months\n')
    for m in range(1,13):
        # i18n_macros_FH.writelines('\\newcommand{\\' + month_name_C[m] + '}{' + calendar.month_name[m].capitalize() + '}\n')
        i18n_macros_FH.writelines('\\newcommand{\\' + month_name_C[m] + '}{' + calendar.month_name[m] + '}\n')
    i18n_macros_FH.writelines('\n')

    i18n_macros_FH.writelines('% Weekdays (abbreviated) table row (no // ending)\n')
    i18n_macros_FH.writelines('% - generates the weekdays header for monthly tables\n')
    i18n_macros_FH.writelines('%	#1 = macro to apply to name, default nothing\n')
    i18n_macros_FH.writelines('\\newcommand{\\WkdayTblRow}[1]{%\n')
    if cfg.week_starts_on_Monday:
        i18n_macros_FH.writelines('\t#1{\\Mon} & #1{\\Tue} & #1{\\Wed} & #1{\\Thu} & #1{\\Fri} & #1{\\Sat} & #1{\\Sun}}\n')
    else:
        i18n_macros_FH.writelines('\t#1{\\Sun} & #1{\\Mon} & #1{\\Tue} & #1{\\Wed} & #1{\\Thu} & #1{\\Fri} & #1{\\Sat}}\n')
    i18n_macros_FH.writelines('% - as above but condensed to just one letter\n')
    i18n_macros_FH.writelines('\\newcommand{\\WkdayTblRowA}[1]{%\n')
    if cfg.week_starts_on_Monday:
        i18n_macros_FH.writelines('\t#1{\\MonA} & #1{\\TueA} & #1{\\WedA} & #1{\\ThuA} & #1{\\FriA} & #1{\\SatA} & #1{\\SunA}}\n')
    else:
        i18n_macros_FH.writelines('\t#1{\\SunA} & #1{\\MonA} & #1{\\TueA} & #1{\\WedA} & #1{\\ThuA} & #1{\\FriA} & #1{\\SatA}}\n')
    i18n_macros_FH.writelines('\n')

    i18n_macros_FH.writelines('% Column types for monthly calendars.  These are generated so we can support both weeks\n')
    i18n_macros_FH.writelines('% starting on Monday and on Sunday.\n')
    if cfg.week_starts_on_Monday:
        i18n_macros_FH.writelines('\\newcolumntype{A}{>{\\hfill\\normalfont\\footnotesize}p{\\WkdayColWidthMonthTblYC}<{\\hspace*{0.5em}}@{\\extracolsep\\fill}}\n')
        i18n_macros_FH.writelines('\\newcolumntype{C}{>{\\hfill\\normalfont\\footnotesize\\color{WeekendDay}}p{\\WkdayColWidthMonthTblYC}<{\\hspace*{0.5em}}@{\\extracolsep\\fill}}\n')
        i18n_macros_FH.writelines('\\newcolumntype{E}{>{\\hfill\\bfseries\\tiny}p{\\WkdayColWidthMinicalMP}@{\\extracolsep\\fill}}\n')
        i18n_macros_FH.writelines('\\newcolumntype{G}{>{\\hfill\\bfseries\\tiny\\vstrut{0pt}\\color{WeekendDay}}p{\\WkdayColWidthMinicalMP}@{\\extracolsep\\fill}}\n')
    else:
        i18n_macros_FH.writelines('\\newcolumntype{A}{>{\\hfill\\normalfont\\footnotesize\\color{WeekendDay}}p{\\WkdayColWidthMonthTblYC}<{\\hspace*{0.5em}}@{\\extracolsep\\fill}}\n')
        i18n_macros_FH.writelines('\\newcolumntype{C}{>{\\hfill\\normalfont\\footnotesize}p{\\WkdayColWidthMonthTblYC}<{\\hspace*{0.5em}}@{\\extracolsep\\fill}}\n')
        i18n_macros_FH.writelines('\\newcolumntype{E}{>{\\hfill\\bfseries\\tiny\\vstrut{0pt}\\color{WeekendDay}}p{\\WkdayColWidthMinicalMP}@{\\extracolsep\\fill}}\n')
        i18n_macros_FH.writelines('\\newcolumntype{G}{>{\\hfill\\bfseries\\tiny}p{\\WkdayColWidthMinicalMP}@{\\extracolsep\\fill}}\n')

#--------------------------------------------------------------------
# generate one \MonthTbl<month_abbr> macro for the given month
#
# also \MonthTbl<month_abbr>Prev and \MonthTbl<month_abbr>Next
# if required trough 'postfix' optional arg (for previous and next year calendars

def gen_macro_MonthTbl(month, year, *postfix):
    day_of_week_month_start  = calendar.monthrange(year, month)[0]
    month_length             = calendar.monthrange(year, month)[1]

    # Macro optional postfix: 'Prev' or 'Next' (for previous or next year monthly calendars)
    if len(postfix) == 0:
        postfix = ['']
    if (postfix[0] != '') and (postfix[0] != 'Prev') and (postfix[0] != 'Next'):
        sys.stdout.write('\n\nERROR in extra param in gen_macro_MonthTbl() call, postfix value: "' + postfix[0]+ '" as given is not allowed.\n\n')
        return ''

    # macro def start
    macro_def = '\\newcommand{\MonthTbl' + month_abbr_C[ month ] + postfix[0] + '}[1][\hfill]{%\n'

    current_day = - day_of_week_month_start
    if cfg.week_starts_on_Monday:
        current_day = current_day + 1
    elif current_day == -6:
        # This would have caused a full empty row at the top of a month
        current_day = 1
    for row in range(6):                                # a month may have up to 6 rows
        for column in range(7):                         # 7 days a week

            end_of_current_day_insert = '} & '          # if in the middle of the table
            if column == 6 and row != 5:
                end_of_current_day_insert = '} \\\\\n'  # if at the end of a row, except last
            if column == 6 and row == 5:
                end_of_current_day_insert = '}'         # at the end of last row

            if (current_day > 0) and (current_day <= month_length):     # human-readable alignment: insert spaces as required
                if (current_day < 10):                                          # - days 1-9
                    macro_def += ' #1{' + str(current_day) + end_of_current_day_insert
                else:                                                           # - days 10-28/29/30/31
                    macro_def += '#1{' + str(current_day) + end_of_current_day_insert
            else:                                                               # - no days
                macro_def += '  #1{' + end_of_current_day_insert

            current_day = current_day + 1

    # macro def end
    macro_def += '}\n'
    return macro_def


#--------------------------------------------------------------------
# Generate and write out table macros for the current, previous and next years
#
# defines:
#       \MyYear{<year>}
#       \MyYearPrev{<year - 1>}
#       \MyYearNext{<year + 1>}
#       \MyYear{<year>}
#       \MonthTblJan ...
#       \MonthTblJanPrev ...
#       \MonthTblJanNext ...

def write_out_MonthTbl_macros(year, file):
    MonthTbl_macros_FH = open(file, 'w')
    MonthTbl_macros_FH.writelines('% Monthly tables macros for current, previous and next year\n\n\n')

    MonthTbl_macros_FH.writelines('% Current year -------------------------------------------------------\n\n')
    MonthTbl_macros_FH.writelines('\\newcommand{\MyYear}{' + str(year) + '}\n\n')

    for m in range(1, 13):
        MonthTbl_macros_FH.writelines(gen_macro_MonthTbl(m, year) + '\n')

    MonthTbl_macros_FH.writelines('% Prev year ----------------------------------------------------------\n\n')
    MonthTbl_macros_FH.writelines('\\newcommand{\MyYearPrev}{' + str(year - 1) + '}\n\n')
    for m in range(1, 13):
        MonthTbl_macros_FH.writelines(gen_macro_MonthTbl(m, year-1, 'Prev') + '\n')

    MonthTbl_macros_FH.writelines('% Next year ----------------------------------------------------------\n\n')
    MonthTbl_macros_FH.writelines('\\newcommand{\MyYearNext}{' + str(year + 1) + '}\n\n')
    for m in range(1, 13):
        MonthTbl_macros_FH.writelines(gen_macro_MonthTbl(m, year+1, 'Next') + '\n')


#--------------------------------------------------------------------
# generate the \MP<month>Left macro for given month and year
# - contains first 3 days of the week for current month
# - incomplete rows are filled from previous/next months and marked '#2'
# - row 6 days are supplied as optional args to '#1' on row 5
#   (months starting Sat with 31 days or Sun with 30/31 days)

def gen_macro_MPMonthLeft(month, year):
    day_of_week_month_start  = calendar.monthrange(year, month)[0]
    month_length             = calendar.monthrange(year, month)[1]

    if not cfg.week_starts_on_Monday:
        day_of_week_month_start = (day_of_week_month_start + 1) % 7

    # generate monthly calendar tables for current, previous and next
    if month == 1:      # curr month is January, prev month is December last year
        prev_month_days = calendar.monthrange(year, 12)[1]
    else:
        prev_month_days = calendar.monthrange(year, month - 1)[1]
    if month == 12:      # curr month is December, next month is January next year
        next_month_days = calendar.monthrange(year, 1)[1]
    else:
        next_month_days = calendar.monthrange(year, month + 1)[1]

    # macro start
    macro_def = '\\newcommand{\MP' + month_abbr_C[ month ] + 'Left}[2]{%\n'

    # first row, may have days from previous month
    row = 0
    for col in range(3):                        # Sun?, Mon, Tue, Wed? (depends on cfg.week_starts_on_Monday)
        day = col - day_of_week_month_start + 1
        if day <= 0:
            day = prev_month_days + day
            temp_month = month - 1
            temp_year = year
            if temp_month < 1:
                temp_month = 12
                temp_year -= 1
            macro_def += '& #2{' + str(day) + '}'   # days, max range 25-31, prev month
            macro_def += '{' + '\\\\'.join(holidays.holidays[datetime.date(temp_year, temp_month, day)]) + '}{} '
        else:
            macro_def += '&  #1{' + str(day) + '}'  # days, max range 1-7, curr month
            macro_def += '{' + '\\\\'.join(holidays.holidays[datetime.date(year, month, day)]) + '}{} '
    macro_def += '\\\\\n'

    # second to 4th rows
    for row in range(1,4):
        for col in range(3):                                                            # Sun?, Mon, Tue, Wed? (depends on cfg.week_starts_on_Monday)
            cal_day = row * 7 + col
            day = cal_day - day_of_week_month_start + 1
            if (day < 10):                                                              # human readable pretty printing
                macro_def += '&  #1{' + str(day) + '}'
            else:
                macro_def += '& #1{' + str(day) + '}'
            macro_def += '{' + '\\\\'.join(holidays.holidays[datetime.date(year, month, day)]) + '}{} '
        macro_def += '\\\\\n'

    # last row, two special cases: days from next month and overflows (sixth_row)
    row = 4
    end_of_current_day_insert = '} '
    for col in range(3):
        cal_day = row * 7 + col
        day = cal_day - day_of_week_month_start + 1
        if col == 2:
            end_of_current_day_insert = '}'
        if day > month_length:                                                   # add days from next month
            day = day - month_length
            temp_month = month + 1
            temp_year = year
            if temp_month > 12:
                temp_month = 1
                temp_year += 1
            macro_def += '&  #2{' + str(day) + '}'
            macro_def += '{' + '\\\\'.join(holidays.holidays[datetime.date(temp_year, temp_month, day)]) + '}{' + end_of_current_day_insert
        else:
            # month spanning on the sixth row ? pass the day+7 as optional arg to #1
            sixth_row_insert = ''
            cal_day = 5 * 7 + col
            dayRow6 = cal_day - day_of_week_month_start + 1
            if dayRow6 <= month_length:
                sixth_row_insert = '[' + str(dayRow6) + ']'
                end_of_current_day_insert = '\\\\'.join(holidays.holidays[datetime.date(year, month, dayRow6)]) + end_of_current_day_insert
            macro_def += '& #1' + sixth_row_insert + '{' + str(day) + '}'
            macro_def += '{' + '\\\\'.join(holidays.holidays[datetime.date(year, month, day)]) + '}{' + end_of_current_day_insert

    # macro end
    macro_def = macro_def + '}\n'
    return macro_def


#--------------------------------------------------------------------
# generate the \MP<month>Right
# (very similar to the \MP<month>Right, there is no 6 row problem)

def gen_macro_MPMonthRight(month, year):
    day_of_week_month_start  = calendar.monthrange(year, month)[0]
    month_length             = calendar.monthrange(year, month)[1]

    if not cfg.week_starts_on_Monday:
        day_of_week_month_start = (day_of_week_month_start + 1) % 7

    # generate monthly calendar tables for current, previous and next
    if month == 1:      # curr month is January, prev month is December last year
        prev_month_days = calendar.monthrange(year, 12)[1]
    else:
        prev_month_days = calendar.monthrange(year, month - 1)[1]
    if month == 12:      # curr month is December, next month is January next year
        next_month_days = calendar.monthrange(year, 1)[1]
    else:
        next_month_days = calendar.monthrange(year, month + 1)[1]

    # macro start
    macro_def = '\\newcommand{\MP' + month_abbr_C[ month ] + 'Right}[2]{%\n'

    # first row, may have days from previous month
    row = 0
    end_of_current_day_insert = '} & '          # if in the midddle of the table
    for col in range(3,7):                      # Wed? Thu, Fri, Sat, Sun? (depends on cfg.week_starts_on_Monday)
        if col == 6:
            end_of_current_day_insert = '} '    # at end of row
        day = col - day_of_week_month_start + 1
        if day <= 0:
            day = prev_month_days + day
            temp_month = month - 1
            temp_year = year
            if temp_month < 1:
                temp_month = 12
                temp_year -= 1
            macro_def += '#2{' + str(day) + '}'  # days from prev month: possible range 25-31,
            macro_def += '{' + '\\\\'.join(holidays.holidays[datetime.date(temp_year, temp_month, day)]) + '}{' + end_of_current_day_insert
        else:
            macro_def += ' #1{' + str(day) + '}'                   # days from curr month: possible range 1-7
            macro_def += '{' + '\\\\'.join(holidays.holidays[datetime.date(year, month, day)]) + '}{' + end_of_current_day_insert
    macro_def += '\\\\\n'

    # second to 4th row
    for row in range(1,4):
        end_of_current_day_insert = '} & '
        for col in range(3,7):                  # Wed? Thu, Fri, Sat, Sun? (depends on cfg.week_starts_on_Monday)
            cal_day = row * 7 + col
            day = cal_day - day_of_week_month_start + 1
            if col == 6:
                end_of_current_day_insert = '} '
            if (day < 10):     # pretty printing
                macro_def += ' #1{' + str(day) + '}'
            else:
                macro_def += '#1{' + str(day) + '}'
            macro_def += '{' + '\\\\'.join(holidays.holidays[datetime.date(year, month, day)]) + '}{' + end_of_current_day_insert
        macro_def += '\\\\\n'

    # last row, special case: days from next month
    row = 4
    end_of_current_day_insert = '} & '
    for col in range(3,7):                      # Wed? Thu, Fri, Sat, Sun? (depends on cfg.week_starts_on_Monday)
        cal_day = row * 7 + col
        day = cal_day - day_of_week_month_start + 1
        if col == 6:
            end_of_current_day_insert = '}'
        if day > month_length:           # add days from next month
            day = day - month_length
            temp_month = month + 1
            temp_year = year
            if temp_month > 12:
                temp_month = 1
                temp_year += 1
            macro_def += ' #2{' + str(day) + '}'
            macro_def += '{' + '\\\\'.join(holidays.holidays[datetime.date(temp_year, temp_month, day)]) + '}{' + end_of_current_day_insert
        else:
            macro_def += '#1' + '{' + str(day) + '}'
            macro_def += '{' + '\\\\'.join(holidays.holidays[datetime.date(year, month, day)]) + '}{' + end_of_current_day_insert

    # macro end
    macro_def = macro_def + '}\n'
    return macro_def


#--------------------------------------------------------------------
# Generate and write out table macros for the Monthly Planner

def write_out_MP_macros(year, file):
    MP_macros_FH = open(file, 'w')
    MP_macros_FH.writelines('% Monthly Planner tables macros for ' + str(year) + '\n\n\n')

    for m in range(1, 13):
       MP_macros_FH.writelines(gen_macro_MPMonthLeft(m, year) + '\n')
       MP_macros_FH.writelines(gen_macro_MPMonthRight(m, year) + '\n')


#--------------------------------------------------------------------
# generates the weeks list

def yeardatescalendar(year):
    # Joins monthdatescalendar(year, month) intelligently (no duplicates) for the full year
    # Return a list of the weeks in the year as full weeks. Weeks are lists of seven datetime.date objects.

    # week 0 is []
    weeks_list = [[]]

    myCal= calendar.Calendar()
    weeks_list +=  myCal.monthdatescalendar(year, 1)            # Jan goes in unconditionally
    for m in range(2, 13):
        curr_month = myCal.monthdatescalendar(year, m)
        if curr_month[0][0].month == m:                         # m > 1 always
            weeks_list += myCal.monthdatescalendar(year, m)     # direct join: month starts Monday
        else:
             weeks_list += myCal.monthdatescalendar(year, m)[1:] # skip first week: avoid duplication

    return weeks_list


#------------------------------------------------------------------------------
# Generate and write out table macros for the Weekly Planner
# special cases: first week may start Dec prev year, last week may end Jan next year

def write_out_WP_macros(year, file):
    WP_macros_FH = open(file, 'w')
    WP_macros_FH.writelines('% Weekly Planner macros for ' + str(year) + '\n\n\n')

    weeks = yeardatescalendar(year)

    for w in range(1, len(weeks)):
        curr_m  = weeks[w][6].month         # current month: from last day-of-week
        other_m = weeks[w][0].month         # month of first day-of-week: current month or previous

        curr_y = weeks[w][6].year           # year of last day-of-week, same as 'year', except maybe last week
        other_y = weeks[w][0].year

        # Month macros for the mini cals
        prev_month_table = '\MonthTbl'
        curr_month_table = '\MonthTbl' + month_abbr_C[curr_m]
        curr_month_name  = calendar.month_name[curr_m]
        next_month_table = '\MonthTbl'
        if (curr_m == 1) and (curr_y == year):      # first month correction: current month is Jan, prev is Dec last year
            prev_month_table += 'DecPrev'
            prev_month_name = calendar.month_name[12]
        else:
            prev_month_table += month_abbr_C[curr_m - 1]
            prev_month_name = calendar.month_name[curr_m - 1]

        if curr_m == 12:                            # last month correction: current month is Dec, next is Jan next year
            next_month_table += 'JanNext'
            next_month_name = calendar.month_name[1]
        else:
            next_month_table += month_abbr_C[curr_m + 1]
            next_month_name = calendar.month_name[curr_m + 1]

        if (curr_m == 1) and (curr_y == year + 1):  # last week correction: current month is Dec, prev is Nov, next is Jan next year
            prev_month_table = '\MonthTbl' + month_abbr_C[11]
            prev_month_name = calendar.month_name[11]
            curr_month_table = '\MonthTbl' + month_abbr_C[12]
            curr_month_name  = calendar.month_name[12]
            next_month_table = '\MonthTbl' + 'JanNext'
            next_month_name = calendar.month_name[1]

        left_pg_macro  = '\LeftPageWP{' + str(w) + '}'
        for d in range(0,3):
            left_pg_macro += '{' + str(weeks[w][d].day) + ' ' + calendar.month_abbr[weeks[w][d].month] + '}'
        for d in range(0,3):
            left_pg_macro += '{' + '\\\\'.join(holidays.holidays[weeks[w][d]]) + '}'

        right_pg_header = '\RightPageHeaderWP{'

        if other_m == curr_m:       # week contained
            right_pg_header = '\RightPageHeaderWP{' + calendar.month_abbr[curr_m] + ' ' + str(curr_y) +'}'
        elif other_m < curr_m:      # week spanning 2 months
            right_pg_header = '\RightPageHeaderWP{' + calendar.month_abbr[other_m] + ' -- ' + calendar.month_abbr[curr_m] + ' ' + str(curr_y) +'}'
        else:                       # first and last weeks correction
            right_pg_header = '\RightPageHeaderWP{' + calendar.month_abbr[12] + ' ' + str(other_y) + ' -- ' + calendar.month_abbr[1] + ' ' + str(curr_y) +'}'

        right_pg_macro = '\RightPageWP'
        for d in range(3,7):
            right_pg_macro += '{' + str(weeks[w][d].day) + ' ' + calendar.month_abbr[weeks[w][d].month] + '}'
        for d in range(3,6):
            if d == 5:
                right_pg_macro += '{' + '\\\\'.join(holidays.holidays[weeks[w][d]] + holidays.holidays[weeks[w][6]]) + '}'
            else:
                right_pg_macro += '{' + '\\\\'.join(holidays.holidays[weeks[w][d]]) + '}'
        #right_pg_macro += '{' + prev_month_name + '}' + '{' + prev_month_table + '}'
        #right_pg_macro += '{' + curr_month_name + '}' + '{' + curr_month_table + '}'
        #right_pg_macro += '{' + next_month_name + '}' + '{' + next_month_table + '}'

        WP_macros_FH.writelines(left_pg_macro + '\n')
        WP_macros_FH.writelines(right_pg_header + '\n')
        WP_macros_FH.writelines(right_pg_macro + '\n')

#====================================================================
# Main

write_out_i18n_macros('DYI_i18n.tex')
write_out_MonthTbl_macros(cfg.year, 'DYI_Month_Tables.tex')
write_out_MP_macros(cfg.year, 'DYI_Monthly_Planner_Tables.tex')
write_out_WP_macros(cfg.year, 'DYI_Weekly_Planner_Tables.tex')
