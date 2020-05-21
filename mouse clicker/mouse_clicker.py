from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import time
import threading

start_stop_key = KeyCode(char='e')
exit_key = KeyCode(char='q')
delay = 0.5
button = Button.left

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.program_running = True
        self.running = False

    def stop_clicking(self):
        self.running = False

    def start_clicking(self):
        self.running = True

    def exit(self):
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


print("Program is running")
with Listener(on_press=on_press) as listener:
    listener.join()
