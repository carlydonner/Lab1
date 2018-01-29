Wiring: RGB LED: Wire the R,G and B pins of the LED to PWM (~) pins on the Arduino, and the (-) pin on the LED to ground. Potentiometer: Wire the potentiometer so that it is powered by 5V, grounded on the ground pin, and the middle pin connects to an Analog pin on the Arduino which can be pins A0-A5 Joystick: Connect +5V to the corresponding pin on the joystick and connect ground to GND. Then connect VRx, VRy, and SW respectively to different Analog pins on the Arduino

File Descriptions:

rgb_controller: This is a c file that reads in the values of the joystick and potentiometer and converts them to fit in the range from 0-255 and adjusts according to the gamma scale so that differences in color are more easily seen by humans. The red, green, blue values are sent via Analog to light up the LED to a certain color, and are also printed on the screen. Upload this to the Arduino before taking the other steps

lab1pygame.py: This python file establishes a serial connection with the arduino and reads in the red, green, blue values that the Arduino prints out. It separates each value and converts it from a string to an integer, and then creates a rectangle using pygame that is the same color as the LED.
