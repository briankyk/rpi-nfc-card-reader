# Linux Only / sudo required
# !/usr/bin/python
from evdev import *   #noqa
dev = InputDevice('/dev/input/event24')   #run "get_dev_info.py" to get the event id

print(dev)

for event in dev.read_loop():
    print ("timestamp, scancode, keycode, key_state")
    if event.type == ecodes.EV_KEY:   #noqa
        print(categorize(event))   #noqa
