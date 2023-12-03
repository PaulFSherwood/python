import win32api
import win32con
import win32gui
from pynput.keyboard import Key, Listener

# Allowed keys and combinations
allowed_keys = ['1', '2', '3', '4', '5', 'a', 'd']
allowed_combinations = {
    'alt+b': (win32con.VK_MENU, 0x42),
    'alt+v': (win32con.VK_MENU, 0x56),
    'alt+c': (win32con.VK_MENU, 0x43),
    'alt+x': (win32con.VK_MENU, 0x58),
    'alt+z': (win32con.VK_MENU, 0x5A),
}

key_codes = {
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    'a': 0x41,
    'd': 0x44,
}

# Get handle to the WoW window (adjust title as needed)
wow_window_title = "World of Warcraft"
hWnd = win32gui.FindWindow(None, wow_window_title)
if not hWnd:
    print(f"Could not find window with title: {wow_window_title}")
    exit()

active = False

def send_key_to_wow(key, combination=False):
    if not combination:
        key_code = key_codes.get(key)
        if key_code:
            win32api.SendMessage(hWnd, win32con.WM_KEYDOWN, key_code, 0)
            win32api.SendMessage(hWnd, win32con.WM_KEYUP, key_code, 0)
    else:
        mod, key_code = allowed_combinations.get(key)
        win32api.SendMessage(hWnd, win32con.WM_KEYDOWN, mod, 0)
        win32api.SendMessage(hWnd, win32con.WM_KEYDOWN, key_code, 0)
        win32api.SendMessage(hWnd, win32con.WM_KEYUP, key_code, 0)
        win32api.SendMessage(hWnd, win32con.WM_KEYUP, mod, 0)

def on_press(key):
    # Display the key pressed (optional)
    try:
        print('{0} pressed'.format(key.char))
    except AttributeError:
        print('{0} pressed'.format(key))

def on_release(key):
    global active

    # Display the key released (optional)
    try:
        print('{0} released'.format(key.char))
        if key.char in allowed_keys and active:
            send_key_to_wow(key.char)
    except AttributeError:
        print('{0} released'.format(key))

    # Alt combinations
    if active and hasattr(key, 'vk'):
        alt_pressed = win32api.GetAsyncKeyState(win32con.VK_MENU)
        if alt_pressed:
            for combination, codes in allowed_combinations.items():
                if key.vk == codes[1]:
                    send_key_to_wow(combination, combination=True)

    # F5 to activate and F6 to deactivate
    if key == Key.f5:
        active = True
        print("Key forwarding activated!")
    elif key == Key.f6:
        active = False
        print("Key forwarding deactivated!")
    # Stop listener if escape is pressed
    elif key == Key.esc:
        return False

# Start the keyboard listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
