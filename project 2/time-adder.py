week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

minutes_in_day = 24 * 60

def add_time(start, duration, weekday = "noday"):
    start_hours, start_minutes_marked = start.split(":")
    duration_hours, duration_minutes = duration.split(":")

    start_minutes, am_pm_mark = start_minutes_marked.split()
    #TODO: REFACTOR THIS
    start_hours = int(start_hours)
    start_minutes = int(start_minutes)
    duration_hours = int(duration_hours)
    duration_minutes = int(duration_minutes)

    if(am_pm_mark == "PM"):
        start_hours += 12

    operational_minutes = hour_to_minutes(start_hours) + start_minutes + hour_to_minutes(duration_hours) + duration_minutes

    days_later = int(operational_minutes // minutes_in_day)
    
    remainder_operational_minutes = operational_minutes % minutes_in_day
    
    hours_later = int(remainder_operational_minutes // 60)
    minutes_later = remainder_operational_minutes % 60

    #new_time = str(days_later) + " "+ str(hours_later) + " " + str(minutes_later)

    am_pm_result_mark = "AM"
    if(hours_later >= 12):
        hours_later -= 12
        am_pm_result_mark = "PM"

    #I see the need of this fix as a problem of the exercise's statement
    if(hours_later == 0):
        hours_later = 12
    
    #elif(hours_later == 12):
    #    am_pm_result_mark = "PM"
    #if(hours_later == 12 and am_pm_mark == "AM"):
    #    am_pm_result_mark = "AM"

    new_time = str(hours_later) + ":" + str(minutes_later).zfill(2) + " " + am_pm_result_mark
  
    day = "monday"
    if(weekday.lower() != "noday"):
        index_of_day = week_days.index(weekday.lower())

        calc_day_index = (index_of_day + days_later) % 7
        day = week_days[calc_day_index]

        new_time += ", " + day.capitalize()

    if(days_later == 1):
        new_time += " (next day)"
    elif(days_later > 1):
        new_time += " ("+ str(days_later) + " days later)"
        
    return new_time

def hour_to_minutes(hours):
    return hours * 60

def minutes_to_hour(minutes):
    return (minutes // 60), (minutes % 60)
