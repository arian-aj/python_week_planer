import random

print("welcome to python week planer")

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

deeds_array = ["Math", "Checkio", "Persian", "Reading", "Sport", "Philosophy"]

duration_array = ["45min", "90min", "1h", "2h"]

def week_plan() -> str:
    for i in range(7):
        print("Deeds of " + week_days[i] + ": ")
        for n in range(3):
            print(str(n + 1) + ". " + random.choice(deeds_array))
            print("duration: " + random.choice(duration_array))
    
    return "This is your weekplan"

print(week_plan())

