import numpy as np
import serial

finger_to_code = {
    'thumb': 'F0',
    'index': 'F1',
    'middle': 'F2',
    # Both ring and pinky are connected to the same motor
    'ring': 'F3',
    'pinky': 'F3',
}


class BrunelHand(object):
    def __init__(self, port, baudrate=57600):
        self._serial = serial.Serial(port, baudrate)

        # Clean usage message if present
        if self._serial.in_waiting:
            self._serial.flushInput()

        self.fingers = []
        for name in finger_to_code.keys():
            f = Finger(name, self)
            setattr(self, name, f)
            self.fingers.append(f)

    def move_finger(self, finger_name, flexness):
        flexness = np.clip(flexness, 0, 255)
        finger_name = finger_to_code[finger_name]

        self._send('{} P{}'.format(finger_name, flexness))

    def _send(self, msg):
        self._serial.write('{}\n'.format(msg).encode())


class Finger(object):
    def __init__(self, name, hand):
        self._name = name
        self._hand_delegate = hand

    @property
    def flex(self):
        return self._flex

    @flex.setter
    def flex(self, f):
        self._flex = f
        self._hand_delegate.move_finger(self._name, self._flex)


if __name__ == '__main__':
    import time

    hand = BrunelHand('/dev/tty.usbmodem14111')

    for _ in range(3):
        hand.index.flex = 0
        time.sleep(2)
        hand.index.flex = 100
        time.sleep(2)
