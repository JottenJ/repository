#styra ett relé med beaglebone

här är alla pins på beagle boarden 
![Bbg_header_1](https://github.com/user-attachments/assets/2eda1d80-4660-4c61-8039-6266a0e13e94)
relén ska kopplas til pinnarna 1, 2 och 12
- SDA → Data
- SCL → Klocka
- VCC → 3.3V
- GND → Jord

skriv  dethär i terminalen 
sudo apt-get install python3-smbus i2c-tools


här är python koden
rätt form till koden finns i en annan fil

import gpiod
import time

chip = gpiod.Chip('gpiochip0')
line = chip.get_line(28)
line.request(consumer="led", type=gpiod.LINE_REQ_DIR_OUT)

while True:
    line.set_value(1)
    time.sleep(1)
    line.set_value(0)
    time.sleep(1)


