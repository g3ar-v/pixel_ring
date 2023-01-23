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

    pixel_ring = pixel_ring.PixelRing('status')
    pixel_ring.set_brightness(7)
    # pixel_ring.change_pattern('trevor')
    while True:
        try:
            pixel_ring.wakeup()
            pixel_ring.think()
            time.sleep(10)
        except KeyboardInterrupt:
            break
    pixel_ring.off()
    power.off()
    time.sleep(1)
