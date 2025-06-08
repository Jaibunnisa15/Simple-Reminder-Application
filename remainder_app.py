import time
import threading

reminders = {}

def add_reminder():
    while True:
        reminder_time = input("Enter time for reminder (in seconds): ")
        
        if reminder_time.isdigit():  # Ensure input is a valid number
            reminder_time = int(reminder_time)
            break
        else:
            print("Invalid input! Please enter a number in seconds.")
    
    message = input("Enter reminder message: ")
    
    if reminder_time in reminders:
        reminders[reminder_time].append(message)  # Add to existing list
    else:
        reminders[reminder_time] = [message]  # Create a new list
    
    print(f"Reminder set for {reminder_time} seconds: {message}")
    
def view_reminders():
    if reminders:
        print("\nScheduled Reminders:")
        for sec, msgs in reminders.items():
            print(f"In {sec} seconds: {', '.join(msgs)}")
    else:
        print("\nNo reminders set.")

def check_reminders():
    while True:
        time.sleep(1)
        triggered = [sec for sec in reminders.keys() if sec == 0]
        for sec in triggered:
            for msg in reminders[sec]:  # Loop through all messages for that time
                print(f"\n🔔 Reminder: {msg}")
            del reminders[sec]  # Remove after triggering
        # Countdown timers
        for sec in list(reminders.keys()):
            reminders[sec - 1] = reminders.pop(sec)

# Start the reminder checking in a separate thread
threading.Thread(target=check_reminders, daemon=True).start()

# Command-line interface
while True:
    print("\nReminder App")
    print("1. Add Reminder")
    print("2. View Reminders")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_reminder()
    elif choice == "2":
        view_reminders()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")