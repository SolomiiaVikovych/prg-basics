class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        if self.is_on:
            if 1 <= new_channel_no <= len(self.channels):
                self.channel_no = new_channel_no
            else:
                print("Invalid channel number.")
        else:
            print("TV is off. Cannot change channel.")

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        if not self.channels:
            print("Channel list is empty.")
        else:
            print("Channel list:")
            for i, channel in enumerate(self.channels, start=1):
                print(f"{i}. {channel}")

    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def show_status(self):
        if self.is_on:
            channel_name = self.channels[self.channel_no - 1] if 1 <= self.channel_no <= len(self.channels) else "Unknown"
            print(f"TV is on, channel {self.channel_no} ({channel_name}), volume {self.volume}")
        else:
            print("TV is off")
