from haversine import haversine, Unit


def calc_max_distance(column, unit):
    max_distance = 0
    home = (float(column[0][0]), float(column[0][1]))
    for i in range(1, len(column) - 1):
        location = (float(column[i][0]), float(column[i][1]))
        distance = haversine(home, location, unit=Unit.METERS)
        if distance > max_distance:
            max_distance = distance
    if unit == 'imperial':
        # TODO: make the return conditional upon value, miles if >= 5280
        max_distance /= 1609
        return str(round(max_distance, 2)) + ' mi'
    return str(round(max_distance, 1)) + ' m'


def calc_flight_distance(column, unit):
    distance = 0
    for i in range(len(column) - 2):
        loc1 = (float(column[i][0]), float(column[i][1]))
        loc2 = (float(column[i + 1][0]), float(column[i + 1][1]))
        distance += haversine(loc1, loc2, unit=Unit.METERS)
    if unit == 'imperial':
        # TODO: make the return conditional upon value, miles if >= 5280
        distance /= 1609
        return str(round(distance, 2)) + ' mi'
    return str(round(distance, 1)) + ' m'


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


def get_max_altitude(column, unit):
    if unit == 'imperial':
        return str(round(column.max() * 3.281)) + ' ft'
    return str(column.max()) + ' m'


def get_max_ground_speed(column):
    return str(column.max()) + ' m/s'


def get_max_current(column):
    return str(column.max()) + ' A'
