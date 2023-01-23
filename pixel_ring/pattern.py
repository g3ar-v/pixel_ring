"""
LED pattern like Echo
"""

import time

# TODO add typing for class
PIXEL_DOT = 4
PIXEL_NUMBER = 12
class Echo(object):
    brightness = 24 * 8

    def __init__(self, show, number=12):
        self.pixels_number = number
        self.pixels = [0] * PIXEL_DOT * number

        if not callable(show):
            raise ValueError('show parameter is not callable')

        self.show = show
        self.stop = False

    def wakeup(self, direction=0):
        position = int((direction + 15) /
                       (360 / self.pixels_number)) % self.pixels_number

        pixels = [0, 255, 63, 0] * self.pixels_number
        pixels[position * PIXEL_DOT + 2] = 132

        self.show(pixels)

    def listen(self):
        pixels = [0, 255, 63, 0] * self.pixels_number

        self.show(pixels)

    def think(self):
        half_brightness = int(self.brightness / 2)
        pixels = [0, 255, 63, 0, 0, 255, 132, 0] * self.pixels_number

        while not self.stop:
            self.show(pixels)
            time.sleep(0.2)
            pixels = pixels[-PIXEL_DOT:] + pixels[:-PIXEL_DOT]
    
    def update(self, value):
        pass

    def speak(self):
        step = int(16)
        position = int(105)
        while not self.stop:
            pixels = [0, 255, 210 - position, 0] * self.pixels_number
            self.show(pixels)
            time.sleep(0.01)
            if position <= 63:
                step = 42
                time.sleep(0.4)
            elif position >= 105:
                step = - 42
                time.sleep(0.4)

            position += step

    def off(self):
        self.show([0] * PIXEL_DOT * 12)


class GoogleHome(object):
    def __init__(self, show):
        self.basis = [0] * PIXEL_DOT * 12
        self.basis[0 * PIXEL_DOT + 1] = 8
        self.basis[3 * PIXEL_DOT + 1] = 4
        self.basis[3 * PIXEL_DOT + 2] = 4
        self.basis[6 * PIXEL_DOT + 2] = 8
        self.basis[9 * PIXEL_DOT + 3] = 8

        self.pixels = self.basis

        if not callable(show):
            raise ValueError('show parameter is not callable')

        self.show = show
        self.stop = False

    def wakeup(self, direction=0):
        position = int((direction + 90 + 15) / 30) % 12

        basis = self.basis[position*-PIXEL_DOT:] + self.basis[:position*-PIXEL_DOT]

        pixels = [v * 25 for v in basis]
        self.show(pixels)
        time.sleep(0.1)

        pixels = pixels[-PIXEL_DOT:] + pixels[:-PIXEL_DOT]
        self.show(pixels)
        time.sleep(0.1)

        for i in range(2):
            new_pixels = pixels[-PIXEL_DOT:] + pixels[:-PIXEL_DOT]

            self.show([v/2+pixels[index]
                      for index, v in enumerate(new_pixels)])
            pixels = new_pixels
            time.sleep(0.1)

        self.show(pixels)
        self.pixels = pixels

    def listen(self):
        pixels = self.pixels
        for i in range(1, 25):
            self.show([(v * i / 24) for v in pixels])
            time.sleep(0.01)

    def think(self):
        pixels = self.pixels

        while not self.stop:
            pixels = pixels[-PIXEL_DOT:] + pixels[:-PIXEL_DOT]
            self.show(pixels)
            time.sleep(0.2)

        t = 0.1
        for i in range(0, 5):
            pixels = pixels[-PIXEL_DOT:] + pixels[:-PIXEL_DOT]
            self.show([(v * (4 - i) / 4) for v in pixels])
            time.sleep(t)
            t /= 2

        self.pixels = pixels

    def speak(self):
        pixels = self.pixels
        step = 1
        brightness = 5
        while not self.stop:
            self.show([(v * brightness / 24) for v in pixels])
            time.sleep(0.02)

            if brightness <= 5:
                step = 1
                time.sleep(0.4)
            elif brightness >= 24:
                step = -1
                time.sleep(0.4)
            brightness += step

    def update(self, value):
        pass

    def off(self):
        self.show([0] * 4 * 12)


class Trevor(object):

    brightness = 24 * 8

    def __init__(self, show):
        self.pixel_number = 12

        self.pixels = [0] * PIXEL_DOT * self.pixel_number

        if not callable(show):
            raise ValueError('show parameter is not callable')

        self.show = show
        self.stop = False

    def wakeup(self, direction=0):
        position = int((direction + 15) /
                       (360 / self.pixel_number)) % self.pixel_number

        pixels = [0, 255, 140, 0] * self.pixel_number
        pixels[position * PIXEL_DOT + 2] = 83
        pixels[position * PIXEL_DOT + 3] = 25

        self.show(pixels)

    def listen(self):
        pixels = [0, 255, 140, 0] * self.pixel_number

        self.show(pixels)

    def think(self):
        direction = 0
        green = 83
        blue = 25
        position = int((direction + 15) /
                       (360 / self.pixel_number)) % self.pixel_number

        pixels = [0, 255, 140, 0] * PIXEL_DOT * self.pixel_number
        pixels[position * PIXEL_DOT + 2] = blue
        pixels[position * PIXEL_DOT + 3] = green

        while not self.stop:
            if position == 12:
                position = 0
                if green == 83 and blue == 25:
                    green = 140
                    blue = 0
                else:
                    green = 83
                    blue = 25
            self.show(pixels)
            pixels[position * PIXEL_DOT + 2] = green
            pixels[position * PIXEL_DOT + 3] = blue
            position += 1
            time.sleep(0.020)

    def speak(self):
        while not self.stop:
            pixels = [0, 255, 140, 0] * self.pixel_number
            self.show(pixels)
            time.sleep(0.5)
            pixels = [0, 255, 83, 25] * self.pixel_number
            self.show(pixels)
            time.sleep(0.5)

    def update(self, value):
        pass

    def off(self):
        self.show([0] * PIXEL_DOT * 12)

class Status(object):
    """ A class that to show status for different skills on mycroft"""
    def __init__(self,show):
        self.pixels = [0, 255, 140, 0] * PIXEL_NUMBER
        self.position = 0
        if not callable(show):
            raise ValueError('show parameter is not callable')
        self.show = show
        self.stop = False
    
    def wakeup(self, direction=0):
        pass

    def listen(self):
        pass

    def think(self):
        pass

    def speak(self):
        pass

    def update(self, value):
        """ Update the status of the skill giving a number between 0 and 12"""
        for position in range(value):
            self.pixels[position * PIXEL_DOT + 2] = 83
            self.pixels[position * PIXEL_DOT + 3] = 25
        self.show(self.pixels)

    def off(self):
        self.show([0] * PIXEL_DOT * PIXEL_NUMBER)