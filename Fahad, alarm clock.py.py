import time
import winsound

def set_alarm(minutes, seconds):
    total_seconds = minutes * 60 + seconds

    if total_seconds >= 0:
        return total_seconds
    else:
        print("Invalid input. Please enter a valid time.")
        return set_alarm()

def play_alarm():
    frequency = 2500  # Set frequency to 2500 Hertz
    duration = 1000  # Set duration to 1000 milliseconds (1 second)

    print("Alarm is sounding!")
    winsound.Beep(frequency, duration)  # Play the 1-second beep sound

def alarm_clock(seconds):
    print(f"Alarm will sound in {seconds} seconds!")
    
    time.sleep(seconds)
    
    play_alarm()

# Set the alarm time directly (e.g., 0 minute and 12 seconds)
alarm_time = set_alarm(0, 12)
alarm_clock(alarm_time)
