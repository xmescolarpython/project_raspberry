import time
import board
import Adafruit_ADS1x15
import adafruit_dht

# Crear una instància del ADC ADS1115
ADC = Adafruit_ADS1x15.ADS1115(busnum = 1)

# Adreça I2C del ADS1115 (per defecte 0x48)
ADS1115_ADDRESS = 0x48

# Canals del ADC
WATER_SENSOR_CHANNEL = 3  # A3 per al sensor d'aigua
SOIL_SENSOR_CHANNEL = 0   # A0 per al sensor d'humitat de terra

# Guany del ADC (rang de tensió d'entrada)
GAIN = 1  # ±4.096V

# Calibració del sensor d'aigua
MIN_ADC_VALUE_WATER = 0    # Valor mínim en condicions seques
MAX_ADC_VALUE_WATER = 26068  # Valor màxim submergit en aigua

# Calibració del sensor d'humitat de terra
MIN_ADC_VALUE_SOIL = 0      # Valor mínim en condicions seques
MAX_ADC_VALUE_SOIL = 25500    # Valor màxim en condicions humides

# Inicialitza el dispositiu d'humitat i temperatura DHT11 al pin GPIO4
dhtDevice = adafruit_dht.DHT11(board.D4)


def llegir_percentatge(adc_value, min_val, max_val):
    """
    Converteix el valor digitalitzat a un percentatge.
    :param adc_value: Valor digital del ADC.
    :param min_val: Valor mínim del sensor.
    :param max_val: Valor màxim del sensor.
    :return: Percentatge calculat (0-100%).
    """
    percentatge = (adc_value - min_val) / (max_val - min_val) * 100
    return max(0, min(100, percentatge))  # Assegurar que el valor està entre 0 i 100

try:
    while True:
        # Llegir el canal A3 (sensor d'aigua)
        water_value = ADC.read_adc(WATER_SENSOR_CHANNEL, gain=GAIN)
        water_percentage = llegir_percentatge(water_value, MIN_ADC_VALUE_WATER, MAX_ADC_VALUE_WATER)

        # Llegir el canal A0 (sensor d'humitat de terra)
        soil_value = ADC.read_adc(SOIL_SENSOR_CHANNEL, gain=GAIN)
        soil_percentage = llegir_percentatge(soil_value, MIN_ADC_VALUE_SOIL, MAX_ADC_VALUE_SOIL)

        # Llegit el pin 4 (sensor d'humitat i termperatura)  
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        if temperature_c is not None and humidity is not None:
            print(f"Temperatura: {temperature_c:.1f}°C")
            print(f"Humitat: {humidity:.1f}%")
        else:
            print("Error en la lectura del sensor. Intentant de nou...")
        time.sleep(2.0)

        # Mostrar els resultats
        print(f"Sensor Aigua (A3): {water_value} ({water_percentage:.2f}%)")
        print(f"Sensor Humitat Terra (A0): {soil_value} ({soil_percentage:.2f}%)")

        # Pausa d'1 segon entre lectures
        time.sleep(1)

except KeyboardInterrupt:
    print("Lectura aturada per l'usuari.")
