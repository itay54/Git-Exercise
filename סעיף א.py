class analog_to_digital_converter:
    analog = ''
    
    def to_digital(self):
        digital_integer = int(self.analog, 2)  # Convert the binary string to an integer
        return 5 / 1023 * digital_integer

    def set_digital_value(self, analog_voltage): # binary with 10 digits
        self.analog = analog_voltage

