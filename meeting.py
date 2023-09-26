# Meeting room request feature
# a. allow input as Date, start time, end time
# b. time hours format is 24 hr, like 07 am to 10pm
# c. only 1 hr slot allowed, no less than or more than one hr allowed
# d. only single date alot allowed.
# e. if overlapping request received, reject request
# f. no database use required.
# g. this is standalone program



meeting_schedule = [] 

def request_meeting(date, start_time, end_time):
    
    for existing_start, existing_end, existing_date in meeting_schedule:
        if (
            existing_date == date and
            ((start_time >= existing_start and start_time < existing_end) or
            (end_time > existing_start and end_time <= existing_end))
        ):
            return "Meeting rejected due to overlaped"

    
    day_hr = 24  
    if end_time <= start_time or end_time > day_hr:
        return "Meeting rejected due to invalid meeting timing."

    meeting_schedule.append((start_time, end_time, date))
    return "Meeting accepted."


if __name__ == "__main__":
    while True:
        date = input("Enter date (DD-MM-YYYY): ")
        start_time = int(input("Enter start time: "))
        end_time = int(input("Enter end time: "))

        result = request_meeting(date, start_time, end_time)
        print(result)




        



