import time

def countdown_timer():
    # Ask user for time input
    try:
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        total_seconds = minutes * 60 + seconds
    except:
        print("Please enter valid numbers!")
        return
    
    print(f"\n⏰ Countdown started for {minutes} minutes and {seconds} seconds!")
    
    # Countdown loop
    while total_seconds > 0:
        # Calculate minutes and seconds remaining
        mins_remaining = total_seconds // 60
        secs_remaining = total_seconds % 60
        
        # Display remaining time
        print(f"Time remaining: {mins_remaining:02d}:{secs_remaining:02d}")
        
        # Wait for 1 second
        time.sleep(1)
        
        # Decrease time
        total_seconds -= 1
    
    # Timer finished
    print("\n🔔 Time's up!")

# Start the timer
print("🌟 Simple Countdown Timer 🌟")
countdown_timer()