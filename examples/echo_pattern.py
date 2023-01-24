"""
Control pixel ring on ReSpeaker 4 Mic Array

pip install pixel_ring gpiozero
"""

import time

from gpiozero import LED
from pixel_ring import apa102_pixel_ring as pixel_ring


if __name__ == "__main__":
    power = LED(5)
    power.on()

    pixel_ring = pixel_ring.PixelRing('echo')
    pixel_ring.set_brightness(10)
    # pixel_ring.change_pattern('google')
    pixel_ring.change_pattern('status')
    while True:
        try:
            # pixel_ring.wakeup()
            # pixel_ring.listen()
            # pixel_ring.think()
            # time.sleep(1)
            pixel_ring.update(6)
            time.sleep(3)
            pixel_ring.update(7)
            time.sleep(3)
            pixel_ring.update(8)
            time.sleep(3)
        except KeyboardInterrupt:
            break
    pixel_ring.off()
    power.off()
    time.sleep(1)
