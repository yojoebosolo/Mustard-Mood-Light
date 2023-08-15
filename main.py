import machine
import neopixel
from machine import Pin
import time

np = neopixel.NeoPixel(machine.Pin(0), 16, bpp=4)


class ColourPin:
    def __init__(self, pin_num, colour):
        self.pin_num = pin_num
        self.colour = colour
        self.obj = Pin(pin_num, Pin.IN, Pin.PULL_UP)
    def print_out(self):
        print(f"pin: {self.pin_num} colour: {self.colour} value: {self.obj()}")
    def get_value(self):
        return self.obj()
        

def get_led_value(list):
    if list[0].get_value() == 0:
        return 255
    elif list[1].get_value() == 0:
        return 145
    else:
        return 0
    

def compare(led_colour):
    different = False
    for i in range(0,4):
        #print(led_colour[i], np.__getitem__(0)[i])
        
        if led_colour[i] < np.__getitem__(0)[i]:
            led_colour[i] = np.__getitem__(0)[i] - 5
            different = True
        elif led_colour[i] > np.__getitem__(0)[i]:
            led_colour[i] = np.__getitem__(0)[i] + 5
            different = True
            
    return led_colour, different
        

def set_led(led_colour):
    np.fill(led_colour)
    np.write()

all_pins = [{"red": [14,13]}, {"green": [12,11]}, {"blue": [10, 9]}, {"white": [8,7]}]
all_objs = []  # just used for convenience for printing


for dict in all_pins:
    for colour, list in dict.items():

        # converts the dict-list of pins into a dict-list of objects per colour
        for i in range(len(list)):
            list[i] = (ColourPin(list[i], colour))
            all_objs.append(list[i])


while True:
    led_colour = []
    for dict in all_pins:
        for colour, list in dict.items():
            # get LED brightness value for each colour
            led_colour.append(get_led_value(list))
 
    led_colour, different = compare(led_colour)
    if different is True:
        set_led(led_colour)
    
    time.sleep(0.005)


#for obj in all_objs:
#    print("obj...")
#    obj.print_out()

print("done")


