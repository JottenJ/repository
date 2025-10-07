import smbus2
import bme280
import time

I2C_BUS = 2          # På BeagleBone är det ofta /dev/i2c-2
BME280_ADDRESS = 0x76  # eller 0x77 beroende på modul

bus = smbus2.SMBus(I2C_BUS)
calibration_params = bme280.load_calibration_params(bus, BME280_ADDRESS)

try:
    while True:
        data = bme280.sample(bus, BME280_ADDRESS, calibration_params)
        print(f"Temp: {data.temperature:.2f} °C")
        print(f"Fukt: {data.humidity:.2f} %")
        print(f"Tryck: {data.pressure:.2f} hPa")
        print("-----")
        time.sleep(1)  # vänta 1 sekund
except KeyboardInterrupt:
    print("Avslutar mätning...")
