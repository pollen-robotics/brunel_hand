import serial


class BrunelHand(object):
    def __init__(self, port, baudrate=57600):
        self.serial = serial.Serial(port, baudrate)

        # Clean usage message if present
        if self.serial.in_waiting:
            self.serial.flushInput()
