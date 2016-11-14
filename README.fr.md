[English](https://github.com/pigetnet/lcd)

# lcd
Gérer un écran LCD (sans i2c)
(Il vous faut piget pour utiliser les scripts : https://github.com/pigetnet/core )

![Photo lcd](https://github.com/pigetnet/lcd/raw/master/doc/lcd_photo.JPG)

# Dépendances
RPLCD : https://github.com/dbrgn/RPLCD (Documentation en anglais disponible sur ce lien)

# Components
Utiliser ces mots-clés pour trouver les composants
* Resistor pack 240pcs : 2,50€
* LCD 16x2 : 1,50€
* Female headers 50pcs : 2,95€
* Cable 30awg 8-color: 5.37€

# Wiring
Vous pouvez utiliser n'importe quel broches pour relier votre écran LCD.
* Pins/Broches : http://pinout.xyz

## LCD --> Cables
* Yellow --> RS
* Green --> EN
* Blue --> D4
* Brown --> D6
* Orange --> D7
* Black (GND) --> VSS
* Black (GND) --> RW
* Red (5V) --> A
* Red (5V) --> VDD

## Contraste/Luminosité
Il faut utiliser un trimpot ou une résistance sinon il sera impossible de lire
le texte sur votre écran LCD
* K  (Luminosité) ---> Résistance (1kohm) / Trimpot 10K --> GND
* V0 (Contraste) ---> Résistance (2kohm) / Trimpot 10K  --> GND

## Cable --> Raspberry Pi
* Yellow --> 7
* Green --> 8
* Blue --> 25
* Purple --> 24
* Brown --> 23
* Orange --> 18

## Schéma
Je vous conseille d'utiliser une stripboard à part pour gérer le 5V/GND et les résistances/trimpot (voir photo)
![Gpio](https://github.com/pigetnet/lcd/raw/master/doc/lcd_wiring_gpio.png)
![Gnd](https://github.com/pigetnet/lcd/raw/master/doc/lcd_wiring_gnd.png)
![Vcc](https://github.com/pigetnet/lcd/raw/master/doc/lcd_wiring_vcc.png)
