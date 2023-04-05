def add_time(start, duration, day=None):
  #a dict of the days in the week in thier number correspondent
    days_dict = {
        "Saturday": 0,
        "Sunday": 1,
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday": 6
    }

    time, time_format = start.split()
    hour, minutes = time.split(':')
    hour = int(hour)
    minutes = int(minutes)

    # turning the clock in a 12 hour format
    if time_format == "PM":
        hour += 12

    # changing data to integers
    dur_hr, dur_min = duration.split(':')
    dur_hr = int(dur_hr)
    dur_min = int(dur_min)

    # Calculating total hours and minutes
    tot_min = minutes + dur_min
    ans_mins = tot_min % 60
    ext_hr = tot_min // 60
    tot_hr = hour + dur_hr + ext_hr


    ans_hour = (tot_hr % 24) % 12


    if ans_hour == 0:
        ans_hour = 12
    ans_hour = str(ans_hour)

    # total days 24 hr is 1 day
    tot_day = (tot_hr // 24)

    # deciding time format (AM/PM)
    ans_midday = ""
    if (tot_hr % 24) <= 11:
        ans_midday = "AM"
    else:
        ans_midday = "PM"

    # Handling single digit minutes case
    if ans_mins <= 9:
        ans_mins = '0' + str(ans_mins)
    else:
        ans_mins = str(ans_mins)

    time_stamp = ans_hour + ":" + ans_mins + ' ' + ans_midday
    if day == None:
        if tot_day == 0:
            return time_stamp
        if tot_day == 1:
            return time_stamp + ' (next day)'
        return time_stamp + ' (' + str(tot_day) + ' days later)'
    else:
        ans_day = (days_dict[day.lower().capitalize()] + tot_day) % 7
        for b, c in days_dict.items():
            if c == ans_day:
                ans_day = b
                break
        if tot_day == 0:
            return time_stamp + ', ' + ans_day
        if tot_day == 1:
            return time_stamp + ', ' + ans_day + ' (next day)'
        return time_stamp + ', ' + ans_day + ' (' + str(
            tot_day) + ' days later)'
