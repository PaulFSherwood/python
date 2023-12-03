import pygetwindow as gw
import pyautogui
from pynput.keyboard import Listener, Key

# Define the process name for WoW Classic clients
wow_process_name = "World of Warcraft"

# Track whether any key was pressed recently to avoid infinite loops
pressed_keys = set()

# Callback function when a key is pressed
def on_key_press(key):
    global pressed_keys
    
    try:
        # Stop the program if ] is pressed
        if key.char == "]":
            print("Program stopped")
            return False
        # If a key that hasn't been pressed yet is detected, send it to WoW clients
        if key.char not in pressed_keys:
            pressed_keys.add(key.char)
            # if they key 1, 2, 3, or 4 are pressed send it
            if key.char in ['1', '2', '3', '4']:
                send_key_to_wow_clients(key.char)
    except AttributeError:
        # Handle special keys that don't have a char attribute
        if key not in pressed_keys:
            pressed_keys.add(key)
            if key == Key.space:
                send_key_to_wow_clients('space')
            # Add more special keys as needed
            # else:
            #     send_key_to_wow_clients(<key-name>)
    except Exception as e:
        print("Error:", str(e))

# Callback function when a key is released
def on_key_release(key):
    global pressed_keys
    try:
        if hasattr(key, "char"):
            pressed_keys.discard(key.char)
        else:
            pressed_keys.discard(key)
    except AttributeError:
        pass

# Function to send a specific key to WoW Classic clients
import time

def send_key_to_wow_clients(key):
    print(f"Sending {key} to WoW clients")
    wow_windows = gw.getWindowsWithTitle(wow_process_name)
    for window in wow_windows:
        try:
            print(f"Activating and sending {key} to", window.title)
            window.activate()
            time.sleep(0.8)  # Add a slight delay after activating the window
            pyautogui.press(key)
        except Exception as e:
            print("Error:", str(e))

# Start the keyboard listener
with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
