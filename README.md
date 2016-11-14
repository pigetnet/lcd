[Version française](https://github.com/pigetnet/lcd/blob/master/README.fr.md)

# lcd
Manage lcd screen (without i2c)
(You need piget to use the scripts : https://github.com/pigetnet/core )

![Photo lcd](https://github.com/pigetnet/lcd/raw/master/doc/lcd_photo.JPG)

# Dependencies
RPLCD : https://github.com/dbrgn/RPLCD (Documentation available at this link)

# Components
Use theses keywords to find the components
* Resistor pack 240pcs : 2,50€
* LCD 16x2 : 1,50€
* Female headers 50pcs : 2,95€
* Cable 30awg 8-color: 5.37€

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
You need to put a trimpot or a resistor or you won't be able
to read text on the lcd screen.
* K  (Luminosity) ---> Resistor (1kohm) / Trimpot 10K --> GND
* V0 (Contrast) ---> Resistor (2kohm) / Trimpot 10K  --> GND

## Cable --> Raspberry Pi
* Yellow --> 7
* Green --> 8
* Blue --> 25
* Purple --> 24
* Brown --> 23
* Orange --> 18

## Schematics
You should make a separate stripboard to manage 5V/GND/Resistor/Trimpot (see photo)

![Gpio](https://github.com/pigetnet/lcd/raw/master/doc/lcd_wiring_gpio.png)
![Gnd](https://github.com/pigetnet/lcd/raw/master/doc/lcd_wiring_gnd.png)
![Vcc](https://github.com/pigetnet/lcd/raw/master/doc/lcd_wiring_vcc.png)
