

from pynput import keyboard
import psutil

# Define the process name for WoW clients
wow_process_name = "WowClassic.exe"  # Adjust the actual process name if needed

from pynput import keyboard

# Callback function when a key is pressed
def on_key_press(key):
    try:
        # Print the pressed key
        print("Key pressed:", key.char)
        # stop the program if ] is pressed
        if key.char == "]":
            print("Program stopped")
            return False
    except AttributeError:
        # Handle special keys that don't have a char attribute
        print("Special key pressed:", key)

# Callback function when a key is released
def on_key_release(key):
    pass  # You can add additional logic here if needed

# Create a listener
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
