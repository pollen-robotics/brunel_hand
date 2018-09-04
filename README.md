# Python library for controlling the Brunel hand by Open Bionics

[![Build Status](https://www.travis-ci.org/pollen-robotics/brunel_hand.svg?branch=master)](https://www.travis-ci.org/pollen-robotics/brunel_hand)

## Installation

From Pypi:

```pip install brunel_hand```

From the source:

```pip install -e ./```

## Usage example

```python

from brunel_hand import BrunelHand


hand = BrunelHand('/dev/tty.usbmodem14111')
hand.open()

for f in hand.fingers:
    f.flex = 100
    time.sleep(2)
    print(hand.get_finger_position())
    f.flex = 0
    time.sleep(2)
    print(hand.get_finger_position())

for _ in range(3):
    hand.close()
    time.sleep(2)
    print(hand.get_finger_position())
    hand.open()
    time.sleep(2)
    print(hand.get_finger_position())
```
