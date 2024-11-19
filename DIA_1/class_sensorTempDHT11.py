import Adafruit_DHT

class SensorDHT11:
    """
    Classe per gestionar el sensor DHT11, que mesura temperatura i humitat.
    """

    def __init__(self, pin):
        """
        Inicialitza el sensor DHT11.
        :param pin: Pin GPIO de la Raspberry Pi on està connectat el sensor.
        """
        self.sensor = Adafruit_DHT.DHT11
        self.pin = pin

    def llegir_dades(self):
        """
        Llegeix la temperatura i la humitat del sensor.
        :return: Tuple (temperatura en °C, humitat en %), o (None, None) si hi ha error.
        """
        humitat, temperatura = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humitat is not None and temperatura is not None:
            return temperatura, humitat
        else:
            return None, None

    def llegir_temperatura(self):
        """
        Llegeix només la temperatura del sensor.
        :return: Temperatura en °C, o None si hi ha error.
        """
        temperatura, _ = self.llegir_dades()
        return temperatura

    def llegir_humitat(self):
        """
        Llegeix només la humitat del sensor.
        :return: Humitat en %, o None si hi ha error.
        """
        _, humitat = self.llegir_dades()
        return humitat