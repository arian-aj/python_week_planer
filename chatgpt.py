import random
from datetime import datetime, timedelta

# Konfiguration
subjects = ["Persisch", "Mathe", "Philosophie", "Checkio", "Sport", "Reading"]
durations = [45, 60, 90, 120]  # in Minuten
days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
start_time = datetime.strptime("09:00", "%H:%M")
pause = timedelta(minutes=30)

def generate_day_schedule():
    selected_subjects = random.sample(subjects, 3)
    schedule = []
    current_time = start_time

    for subject in selected_subjects:
        duration = random.choice(durations)
        end_time = current_time + timedelta(minutes=duration)
        schedule.append(f"{current_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}: {subject} ({duration} min)")
        current_time = end_time + pause  # Pause nach dem Fach

    return schedule

def generate_week_schedule():
    week_schedule = ""
    for day in days:
        week_schedule += f"\n{day}:\n"
        schedule = generate_day_schedule()
        for entry in schedule:
            week_schedule += f"  {entry}\n"
    return week_schedule

plan = generate_week_schedule()
print(plan)
