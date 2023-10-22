class analog_to_digital_converter:
    max_voltage = 0
    num_bits = 0
    analog = ''
    def __init__(self, max_voltage=5, num_bits=10):
        self.max_voltage = max_voltage
        self.num_bits = num_bits
        self.analog = ''

    def to_digital(self):
        digital_integer = int(self.analog, 2)  # Convert the binary string to an integer
        return (self.max_voltage / (2 ** self.num_bits - 1)) * digital_integer

    def set_digital_value(self, analog_voltage):
        self.analog = analog_voltage

