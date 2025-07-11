import time
import machine

# The first GPIO pin connected to segment A (starts at GPIO2)
FIRST_GPIO= 2  

# Bit patterns for numbers 0 to 9 on 7-segment display
# Each hex value shows which segments (A to G) should light up and be ON to make a number
bits= [
    0x3f, # 0 => segments A,B,C,D,E,F
    0x06, # 1 => segments B,C
    0x5b, # 2 => segments A,B,G,E,D
    0x4f, # 3 => segments A,B,G,C,D
    0x66, # 4 => segments F,G,B,C
    0x6d, # 5 => segments A,F,G,C,D
    0x7d, # 6 => segments A,F,G,C,D,E
    0x07, # 7 => segments A,B,C
    0x7f, # 8 => all segments
    0x67  # 9 => segments A,B,C,D,F,G
]

# Set GPIO10, 11, 12 for the LEDs (Red, Yellow, Green) as Traffic light LEDs
leds= [machine.Pin(pin, machine.Pin.OUT) for pin in (10, 11, 12)]

# Function to show a number (0 to 9) on the 7-segment display
def display_number(num):
    # Set each segment pin (A to G) based on the pattern
    for i in range(7): # 7 segments (A to G)
        # Turn ON or OFF each segment depending on the bit pattern (bits[num])
        # The ~ (invert) is needed because segments light when GPIO is LOW
        machine.Pin(FIRST_GPIO + i, machine.Pin.OUT).value(~bits[num] & (1 << i))

# Function to run the main traffic light sequence with countdown display in a loop
def traffic_light_sequence():
    while True:
        # RED LIGHT: countdown from 5 to 1
        leds[0].on() # Red LED on
        for num in range(5, 0, -1): # Show each number for 1 second (5, 4, 3, 2, 1)
            display_number(num)
            time.sleep(1)
        leds[0].off() # Red LED off
        
        # YELLOW LIGHT: show 0
        leds[1].on() # Yellow LED on
        display_number(0)
        time.sleep(1) # Show 0 for 1 second
        leds[1].off() # Yellow LED off
        
        # GREEN LIGHT: countdown from 5 to 1
        leds[2].on()  # Green LED on  
        for num in range(5, 0, -1): # Show each number for 1 second (5, 4, 3, 2, 1)
            display_number(num)
            time.sleep(1)
        leds[2].off() # Green LED off

        # YELLOW LIGHT: show 0
        leds[1].on() # Yellow LED on  
        display_number(0)
        time.sleep(1) # Show 0 for 1 second
        leds[1].off() # Yellow LED off

# Start the program
if __name__ == "__main__":
    # Initialize all 7-segment pins as outputs
    for gpio in range(FIRST_GPIO, FIRST_GPIO + 7):
        machine.Pin(gpio, machine.Pin.OUT)
    
    # Start the traffic light sequence
    traffic_light_sequence()