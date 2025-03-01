from datetime import datetime, timedelta

#1
def subtract_five_days():
    current_date = datetime.now()
    new_date = current_date - timedelta(days=5)
    return new_date.strftime("%Y-%m-%d %H:%M:%S")

print("Date after subtracting five days:", subtract_five_days())

#2
def print_dates():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    return yesterday.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d"), tomorrow.strftime("%Y-%m-%d")

yesterday, today, tomorrow = print_dates()
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


#3
def drop_microseconds():
    now = datetime.now().replace(microsecond=0)
    return now.strftime("%Y-%m-%d %H:%M:%S")

print("Current datetime without microseconds:", drop_microseconds())


#4
def date_difference_in_seconds(date1, date2):
    format_str = "%Y-%m-%d %H:%M:%S"  
    dt1 = datetime.strptime(date1, format_str)
    dt2 = datetime.strptime(date2, format_str)
    difference = abs((dt2 - dt1).total_seconds())
    return difference

date1 = "2024-02-10 12:00:00"
date2 = "2024-02-15 12:00:00"
print("Difference in seconds:", date_difference_in_seconds(date1, date2))





