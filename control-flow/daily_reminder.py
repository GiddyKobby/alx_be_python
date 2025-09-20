# daily_reminder.py

# Ask for task description
task = input("Enter your task: ")

# Loop until valid priority is entered
while True:
    priority = input("Priority (high/medium/low): ").lower()
    match priority:
        case "high" | "medium" | "low":
            break
        case _:
            print("Please enter a valid priority: high, medium, or low.")

# Loop until valid time-bound input is entered
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ["yes", "no"]:
        break
    else:
        print("Please answer with 'yes' or 'no'.")

# Provide customized reminder
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Final output
print("\nReminder:", reminder)
