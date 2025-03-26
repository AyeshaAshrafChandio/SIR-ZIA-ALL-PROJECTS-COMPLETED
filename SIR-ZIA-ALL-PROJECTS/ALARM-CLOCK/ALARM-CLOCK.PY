import time
from datetime import datetime, timedelta  # Import timedelta
import winsound  # Import winsound module

def play_beep():
    """Play a beep sound using winsound."""
    frequency = 1000  # Frequency of the beep sound (in Hz)
    duration = 2000   # Duration of the beep sound (in milliseconds)
    winsound.Beep(frequency, duration)

def set_alarm(alarm_time):
    """Set an alarm for a specific time in HH:MM:SS format."""
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")  # Get current time
        if current_time >= alarm_time:  # Check if current time matches alarm time
            print("⏰ Time's up! Wake up! 🔔")
            play_beep()  # Play the beep sound
            break
        print(f"⏳ Current time: {current_time}. Waiting...")
        time.sleep(1)  # Wait for 1 second before checking again

def snooze(snooze_minutes):
    """Snooze the alarm for a specified number of minutes."""
    snooze_time = (datetime.now() + timedelta(minutes=snooze_minutes)).strftime("%H:%M:%S")
    print(f"⏸ Snoozing for {snooze_minutes} minutes. Alarm will ring at {snooze_time}...")
    set_alarm(snooze_time)

def main():
    print("⏰ Welcome to the Alarm Clock! ⏰")

    while True:
        # Ask user for alarm time in HH:MM:SS format
        alarm_time = input("\nSet alarm time (HH:MM:SS): ")

        # Validate the input format
        try:
            datetime.strptime(alarm_time, "%H:%M:%S")
        except ValueError:
            print("❌ Invalid time format! Please use HH:MM:SS.")
            continue

        # Set the alarm
        set_alarm(alarm_time)

        # Ask if the user wants to snooze
        snooze_option = input("Do you want to snooze? (y/n): ").lower()
        if snooze_option == 'y':
            try:
                snooze_minutes = int(input("Enter snooze time (in minutes): "))
                if snooze_minutes < 1:
                    print("❌ Please enter a positive number of minutes.")
                    continue
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")
                continue
            snooze(snooze_minutes)

        # Ask if the user wants to set another alarm
        another = input("Do you want to set another alarm? (y/n): ").lower()
        if another != 'y':
            print("🚀 Thank you for using the Alarm Clock. Goodbye! 🚀")
            break

# Run the program
if __name__ == "__main__":
    main()