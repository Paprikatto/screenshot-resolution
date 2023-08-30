from plyer import notification
import keyboard
import mouse

first_click = None
second_click = None

def send_notification(resolution):
    notification_title = "Screenshot Taken"
    notification_message = f"Screenshot resolution: {resolution}"
    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=5  # Display the notification for 5 seconds
    )
    mouse.unhook_all()

def calculate_screenshot_size():
    global first_click
    global second_click
    x = abs(first_click[0] - second_click[0])
    y = abs(first_click[1] - second_click[1])

    send_notification(f"{x} x {y}")

def on_left_click(event):
    global first_click
    global second_click
    if isinstance(event, mouse.ButtonEvent):
        print(event)
        if event.event_type == 'down' and not first_click:
            first_click = mouse.get_position()
            print(f"first click {first_click}")
        if event.event_type == 'up' and not second_click:
            second_click = mouse.get_position()
            calculate_screenshot_size()



def start_mouse_tracking():
    global first_click
    global second_click
    print("start")
    mouse.hook(on_left_click)
    first_click = None
    second_click = None

keyboard.add_hotkey("win+shift+s", start_mouse_tracking)

try:
    print("Press Win + Shift + S to send a notification.")
    keyboard.wait("esc")  # Wait for the 'esc' key to exit the script
except KeyboardInterrupt:
    pass  # Handle Ctrl+C to exit gracefully
finally:
    keyboard.unhook_all()  # Unhook all hotkeys before exiting