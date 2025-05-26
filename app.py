import random
from datetime import datetime, timedelta

print("welcome to python week planer")

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

deeds_array = ["Math", "Checkio", "Persian", "Reading", "Sport", "Philosophy"]

duration_array = ["45min", "90min", "1h", "2h"]

pause = ["30min"]

def parse_duration(duration_str):
    if "min" in duration_str:
        minutes = int(duration_str.replace("min", ""))
        return timedelta(minutes=minutes)
    if "h" in duration_str:
        hours = int(duration_str.replace("h", ""))
        return timedelta(hours=hours)
    else:
        raise ValueError("Unsupported format")

def parse_pause(pause_str):
    if "min" in duration_str:
        minutes = int(pause_str.replace("min", ""))
        return timedelta(minutes=minutes)
    else:
        raise ValueError("Unsupported format")


time = datetime.strptime("09:00", "%H:%M").time()



def week_plan() -> str:
    for i in range(7):
        print("Deeds of " + week_days[i] + ": ")
        for n in range(3):
            print(str(n + 1) + ". " + random.choice(deeds_array))
            print("duration: " + random.choice(duration_array))
        
    
    return "This is your weekplan"

print(week_plan())

