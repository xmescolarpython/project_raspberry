from Adafruit_ADS1x15 import ADS1115
import time

# Crea una instància de l'ADS1115
adc = ADS1115(busnum=1)

# Configura el guany (ajusta segons el rang del sensor, aquí 4.096V)
GAIN = 1

# Llegeix els valors dels canals A0 i A3
def read_sensors():
    water_level = adc.read_adc(0, gain=GAIN)  # A0
    soil_moisture = adc.read_adc(3, gain=GAIN)  # A3

    # Converteix a volts (16 bits, 4.096V màxim)
    water_voltage = water_level * 4.096 / 32768.0
    soil_voltage = soil_moisture * 4.096 / 32768.0

    return water_voltage, soil_voltage

def main():
    while True:
        # Llegeix els sensors
        water_voltage, soil_voltage = read_sensors()

        # Mostra els resultats
        print(f"Water Level Voltage: {water_voltage:.2f} V")
        print(f"Soil Moisture Voltage: {soil_voltage:.2f} V")
        print("=" * 30)

        # Petita pausa per alternar
        time.sleep(1)

if __name__ == "__main__":
    main()
