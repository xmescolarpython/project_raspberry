"""
This Raspberry Pi code was developed by newbiely.com
This Raspberry Pi code is made available for public use without any restriction
For comprehensive instructions and wiring diagrams, please visit:
https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-water-sensor
"""
import time
import Adafruit_ADS1x15

# Create an ADS1115 ADC instance
ADC = Adafruit_ADS1x15.ADS1115(busnum = 1)

# Specify the ADC channel (0-3) based on your connection
ADC_CHANNEL = 0 # A3 of ADS1115 module

# Set the gain (input voltage range) for your application
GAIN = 1  # Gain of 1 corresponds to +/-4.096V

# Define the conversion factor for water level calculation
MIN_ADC_VALUE = 29724  # Replace with the minimum ADC value for your sensor
MAX_ADC_VALUE = 6839 # Replace with the maximum ADC value for your sensor

max,min = ADC.read_adc(ADC_CHANNEL, gain=GAIN),ADC.read_adc(ADC_CHANNEL, gain=GAIN)
try:
    while True:
        # Read the raw ADC value
        adc_value = ADC.read_adc(ADC_CHANNEL, gain=GAIN)
	Y69_value = SensorHumitatTerraYI69()
        
	if max < adc_value:
            max = adc_value
        if min > adc_value:
            min = adc_value
        print(adc_value, max, min)

        # Convert the raw ADC value to a water level percentage
        water_level = (adc_value - MIN_ADC_VALUE) / (MAX_ADC_VALUE - MIN_ADC_VALUE) * 100

        print(f"ADC Value: {adc_value} | Water Level: {water_level:.2f}% Y69 Value: {Y69_value} | Humitat del sol: {humitat:.2f}%")

        time.sleep(1)  # Wait for a second before the next reading

except KeyboardInterrupt:
     print("\nLectura aturada per l'usuari.")

finally:
	Y69_value.tancar()

