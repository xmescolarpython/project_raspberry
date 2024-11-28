"""
This Raspberry Pi code was developed by newbiely.com
This Raspberry Pi code is made available for public use without any restriction
For comprehensive instructions and wiring diagrams, please visit:
https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-water-sensor
"""
import time
import Adafruit_ADS1x15
import spidev

class SensorHumitatTerraYI69:
    """
    Classe per gestionar el sensor d'humitat de terra YI-69 mitjançant un MCP3008 ADC.
    """

    def __init__(self, canal=0, bus=0, device=0):
        """
        Inicialitza la connexió amb el MCP3008 i el sensor YI-69.
        :param canal: Canal de l'ADC al qual està connectat el sensor (0-7).
        :param bus: Bus SPI (per defecte és 0).
        :param device: Dispositiu SPI (per defecte és 0).
        """
        self.canal = canal
        self.bus = bus
        self.device = device
        
        # Inicialització de l'ADC MCP3008
        self.spi = spidev.SpiDev()
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz = 1350000  # Configuració de la velocitat SPI

    def llegir_analogic(self):
        """
        Llegeix un valor analògic de l'ADC.
        :return: Valor digitalitzat (0-1023).
        """
        # Enviar la comanda per llegir del canal seleccionat
        request = [1, (8 + self.canal) << 4, 0]
        resposta = self.spi.xfer2(request)
        
        # Convertir la resposta de l'ADC (10 bits)
        resultat = ((resposta[1] & 3) << 8) + resposta[2]
        return resultat

    def llegir_humitat(self):
        """
        Llegeix el valor de humitat del sensor YI-69.
        :return: Valor de la humitat en un rang de 0 a 100.
        """
        # Llegeix el valor analògic
        valor_analogic = self.llegir_analogic()
        
        # Convertir el valor a percentatge de humitat (0-100%)
        # Considerant que el sensor té un rang de 0 (sec) a 1023 (molt humit).
        humitat = (valor_analogic / 1023.0) * 100
        return humitat

    def tancar(self):
        """Tanca la connexió SPI amb l'ADC."""
        self.spi.close()


# Create an ADS1115 ADC instance
ADC = Adafruit_ADS1x15.ADS1115(busnum = 1)

# Specify the ADC channel (0-3) based on your connection
ADC_CHANNEL = 3 # A3 of ADS1115 module
Y69_CHANNEL = 0 # A0 of Y69 module

# Set the gain (input voltage range) for your application
GAIN = 1  # Gain of 1 corresponds to +/-4.096V

# Define the conversion factor for water level calculation
MIN_ADC_VALUE = 0 # 14134  # Replace with the minimum ADC value for your sensor
MAX_ADC_VALUE = 26068 # 25470 # Replace with the maximum ADC value for your sensor

max_adc,min_adc = ADC.read_adc(ADC_CHANNEL, gain=GAIN),ADC.read_adc(ADC_CHANNEL, gain=GAIN)
max_YI69, min_YI69 = ADC.read_adc(Y69_CHANNEL, gain=GAIN), ADC.read_adc(Y69_CHANNEL, gain=GAIN)

# Define the conversion factor for soil moisture calculation
MIN_MOISTURE_VALUE = 0 # Replace with the minimum SOIL MOISTURE value for your sensor
MAX_MOISTURE_VALUE = 300 # Replace with the maximum SOIL MOISTURE value for your sensor

# Define a Soil Moisture Sensor
YI69 = SensorHumitatTerraYI69()

try:
    while True:
        # Read the raw ADC value
         adc_value = ADC.read_adc(ADC_CHANNEL, gain=GAIN)
         YI69_value = YI69.llegir_humitat() 
         
         if max_adc < adc_value:
              max_adc = adc_value
         if min_adc > adc_value:
              min_adc = adc_value
         print(adc_value, max_adc, min_adc)

         if max_YI69 < YI69_value:
              max_YI69 = YI69_value
         if min_YI69 > YI69_value:
              min_YI69 = YI69_value 
         print(YI69_value, max_YI69, min_YI69)

	 # Convert the raw ADC value to a water level percentage
         water_level = (adc_value - MIN_ADC_VALUE) / (MAX_ADC_VALUE - MIN_ADC_VALUE) * 100 
         moisture_level = (YI69_value - MIN_MOISTURE_VALUE) /  (MAX_MOISTURE_VALUE - MIN_MOISTURE_VALUE) * 100 

         print(f"ADC Value: {adc_value} | Water Level: {water_level:.2f}% | YI69 Value: {YI69_value} | Moisture Level: {moisture_level:.2f}")

         time.sleep(1)  # Wait for a second before the next reading

except KeyboardInterrupt:
     print("\nLectura aturada per l'usuari.")

#finally:
#	Y69_value.tancar()

