import subprocess
import time

# Function to put PC to sleep (Linux)
def sleep_pc():
    subprocess.run(["systemctl", "suspend"])

# Timer with countdown display
def sleep_timer(minutes):
    total_seconds = round(minutes * 60)
    
    for remaining in range(total_seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        print(f"\rSleep in: {mins:02d}:{secs:02d}", end="", flush=True)
        time.sleep(1)
    
    print("\nPutting PC to sleep now!")
    sleep_pc()

# Main execution
if __name__ == "__main__":
    print("Simple Sleep Timer")
    try:
        minutes = float(input("Enter minutes until sleep: "))
        sleep_timer(minutes)
    except KeyboardInterrupt:
        print("\nTimer cancelled!")
    except ValueError:
        print("Please enter a valid number!")