# lcd
Manage lcd screen (without i2c)

# Wiring
You can use whichever pins you want for the lcd screen.
* Pins : http://pinout.xyz

## LCD --> Cable
* Yellow --> RS
* Green --> EN
* Blue --> D4
* Brown --> D6
* Orange --> D7
* Black (GND) --> VSS
* Black (GND) --> RW
* Red (5V) --> A
* Red (5V) --> VDD

## Contrast/Luminosity 
You need to put a trimpot or a resistor on (500ohms should be enough) or you won't be able
to read text on the lcd screen.
* K  (Luminosity) ---> Resistor (500ohm) / Trimpot 10K --> GND
* V0 (Contrast) ---> Resistor (500ohm) / Trimpot 10K  --> GND

## Cable --> Raspberry Pi
* Yellow --> 7
* Green --> 8
* Blue --> 25
* Purple --> 24
* Brown --> 23
* Orange --> 18
