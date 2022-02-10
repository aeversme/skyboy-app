import pandas as pd
import datetime as dt
import time


def get_date(column):
    return column[0].date().strftime('%b %d, %Y')


def get_time(column):
    return column[0].time().strftime('%I:%M:%S %p')


def get_flight_length(column):
    hours, remainder = divmod((column.iat[-1] - column[0]).total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return '%s min %s sec' % (int(minutes), int(seconds))


def get_capacity_used(column):
    return str(column.iat[-1]) + ' mAh'


def get_tx_power(column):
    return str(column[0]) + ' mW'
