import os

class ADBController:
    def __init__(self, device_id):
        self.device_id = device_id

    def run(self, command):
        os.system(f"adb -s {self.device_id} {command}")

    def tap(self, x, y):
        try:
            x = int(x)
            y = int(y)
            self.run(f"shell input tap {x} {y}")
        except:
            print(f"Invalid tap: {x}, {y}")

    def input_text(self, text):
        text = str(text).replace(" ", "%s")
        self.run(f"shell input text {text}")

    def swipe(self, x1, y1, x2, y2):
        self.run(f"shell input swipe {x1} {y1} {x2} {y2}")