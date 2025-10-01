import smbus2
import bme280

# I2C‑buss (ofta 1 på Pi, 2 på BeagleBone)
port = 1
address = 0x76   # eller 0x77 beroende på modul

bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

data = bme280.sample(bus, address, calibration_params)

print(f"Temperatur: {data.temperature:.2f} °C")
print(f"Lufttryck:  {data.pressure:.2f} hPa")
print(f"Luftfukt:   {data.humidity:.2f} %")
