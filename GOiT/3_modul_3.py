from datetime import datetime, timedelta
 

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def find_next_weekday(start_date, weekday):
    start_weekday = start_date.weekday()
    days_ahead = weekday - start_weekday
    if days_ahead <= 0:
        days_ahead += 7

    next_date = start_date + timedelta(days=days_ahead)
    return next_date
        
        