# Sending morse code signals through LED connected to the Raspi
# timing - start off with a variable time, change length of time for bit
# spacing - 
# set it high for two bits and low for two bits (each ltter is 1 bit)
# one bit between letters and two bits between words

import time;
import RPI.GPIO as GPIO

t = 0.5;	# seconds, time between symbols is 1 bit time, between letter is 3 bit time, figure out how long it takes
max_length = 20;
msg = "PRAVA SOS"


MORSECODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        }

class Safeguards:
	def __enter__(self):
		return self
	def __exit__(self, *rabc):
		GPIO.cleanup()
		print("Safe exit succeeded")
		return not any(rabc)

def prepare_pin(pin = 17):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)

def turn_high(pin):
	GPIO.output(pin, GPIO.HIGH)

def turn_low(pin):
	GPIO.output(pin, GPIO.LOW)

def encode_morse(word):
	morseword = ""
	for char in word:
		if char == " ":
			morseword += " "
		morseword += MORSECODE[char.upper()]
	return morseword

def delay(duration):
	time.sleep(duration)

def blink(pin = 17, duration = 1):
	prepare_pin(pin)

	for i in range(2):
		turn_high(pin)
		delay(duration)

	for i in range(2):
		turn_low(pin)
		delay(duration)

	for i in range(max_length):
		encodedmsg = encode_morse(msg)

		for char in encodedmsg:
			if char == " ":
				for i in range(2):
					turn_low(pin)
					delay(duration)

			if char == ".":
				turn_high(pin)
				delay(0.5*duration)

			if char == "-":
				turn_high(duration)
				delay(duration)


if __name__ == "__main__":
	with Safeguards():
		blink();