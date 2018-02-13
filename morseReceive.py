#
## Introducton to Python breadboarding
#
import time
import RPi.GPIO as GPIO

class Safeguards:
    def __enter__(self):
        return self
    def __exit__(self,*rabc):
        GPIO.cleanup()
        print("Safe exit succeeded")
        return not any(rabc)


def prepare_pin(pin=23):
    GPIO.setmode(GPIO.BCM)  #use Broadcom (BCM) GPIO numbers on breakout pcb

    GPIO.setup(pin,GPIO.IN) # allow pi to read levels

def read_pin(pin):
    return GPIO.input(pin)  # set 3.3V level on GPIO output

def delay(duration):            # sleep for duration seconds where duration is a float.
    time.sleep(duration)

def receive(blinks=40,duration=1,pin=23):
    prepare_pin(pin)
    message = []
    for i in range(blinks):
        message.append(read_pin(pin))
        delay(duration/2.)
    return message
def parse(message,duration=1):
    morse = ''
    if message[0:3] == [1,1,1,1]:
        cleaned = message[4::]
        x = 0
        for x <= len(cleaned):
            if cleaned[x]==1 && cleaned[x+1]==1:
                morse = morse + '-'
            elif cleaned[x]==1 && cleaned[x+1]==0:
                morse = morse + '.'
            elif cleaned[x]==0 && cleaned[x+1]==0:
                morse = morse + ' '
            x += 2
    else:
        raise('I started on the wrong bit. I is sorry. I will do better next time.')
    return morse

def text(morse):
    text = ''
    letters = morse.split(' ')
    for val in letters:
        uni=MORSE_CODE_DICT[letters(val)]
        text = text+uni
    return text



if __name__ == "__main__":
    with Safeguards():
       message = receive()
       morse = parse(message)
       out = text(morse)

bittime = 1
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
