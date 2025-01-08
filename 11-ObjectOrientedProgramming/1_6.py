class Phone:
    def __init__(self, battery_level, volume_level, screen_status):
        self.battery_level = battery_level  # in percentage
        self.volume_level = volume_level    # 0 to 100 scale
        self.screen_status = screen_status  # On or Off

    def make_call(self, number):
        if self.battery_level > 0:
            print(f"Calling {number}...")
            self.battery_level -= 5
        else:
            print("Battery too low to make a call.")

    def send_message(self, number, message):
        if self.battery_level > 0:
            print(f"Sending message to {number}: {message}")
            self.battery_level -= 2
        else:
            print("Battery too low to send a message.")

    def play_music(self, song):
        if self.battery_level > 0 and self.screen_status == "On":
            print(f"Playing music: {song}")
            self.battery_level -= 3
        elif self.screen_status == "Off":
            print("Turn on the screen to play music.")
        else:
            print("Battery too low to play music.")

    def display_status(self):
        print(f"Battery Level: {self.battery_level}%")
        print(f"Volume Level: {self.volume_level}")
        print(f"Screen Status: {self.screen_status}")

my_phone = Phone(battery_level=50, volume_level=70, screen_status="On")
my_phone.display_status()
my_phone.make_call("123-456-7890")
my_phone.send_message("123-456-7890", "Hello!")
my_phone.play_music("Ultraviolence")
my_phone.display_status()
