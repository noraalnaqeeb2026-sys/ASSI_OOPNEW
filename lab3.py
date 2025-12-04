# HW3 - AirConditioner 

class AirConditioner:
    def __init__(self):
        self._temperature = 24
        self.__state = "off"
        self.mode = "cool"

    def turn_on(self):
        self.__state = "on"
        print("AC is now ON")

    def turn_off(self):
        self.__state = "off"
        print("AC is now OFF")

    def set_mode(self, mode):
        if mode in ["cool", "heat", "auto"]:
            self.mode = mode
        else:
            print("Invalid mode")

    def increase_temp(self):
        self._temperature += 1

    def decrease_temp(self):
        self._temperature -= 1

    def get_status(self):
        print(f"State: {self.__state}, Mode: {self.mode}, Temp: {self._temperature}")
        

ac = AirConditioner()
ac.turn_on()
ac.set_mode("heat")
ac.increase_temp()
ac.get_status()
ac.turn_off()
