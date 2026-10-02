# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Blink USR3 LED at 5 Hz
--------------------------------------------------------------------------
License:
Copyright 2026 YOUR NAME HERE

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
--------------------------------------------------------------------------
Description:
  Uses the Adafruit BBIO library to blink the USR3 LED at 5 Hz
  (5 full on/off cycles per second). Press Ctrl+C to stop.
--------------------------------------------------------------------------
"""
import time
import Adafruit_BBIO.GPIO as GPIO

LED = "USR3"
FREQUENCY_HZ = 5
HALF_PERIOD = 1.0 / (2 * FREQUENCY_HZ)   # 0.1 s on, 0.1 s off

if __name__ == "__main__":
    GPIO.setup(LED, GPIO.OUT)
    try:
        while True:
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(HALF_PERIOD)
            GPIO.output(LED, GPIO.LOW)
            time.sleep(HALF_PERIOD)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.output(LED, GPIO.LOW)
        GPIO.cleanup()
