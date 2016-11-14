import RPi.GPIO as GPIO
from RPLCD import CharLCD
lcd = CharLCD(pin_rs=7, pin_rw=None, pin_e=8, pins_data=[25,24,23,18],numbering_mode=GPIO.BCM, cols=20, rows=4)
lcd._set_cursor_pos([0,0])
lcd.write_string("HELLO WORLD")
lcd.close()


