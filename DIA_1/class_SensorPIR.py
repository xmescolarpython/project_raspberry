import RPi.GPIO as GPIO

class SensorPIR:
    def __init__(self, pin):
        """
        Inicialitza el sensor PIR configurant el pin com a entrada.
        :param pin: Número del pin GPIO on està connectat el sensor PIR.
        """
        self.pin = pin
        GPIO.setmode(GPIO.BCM)  # Utilitza el mode BCM (numeració GPIO)
        GPIO.setup(self.pin, GPIO.IN)  # Configura el pin com a entrada

    def detectar_moviment(self):
        """
        Detecta moviment amb el sensor PIR.
        :return: True si es detecta moviment, False en cas contrari.
        """
        return GPIO.input(self.pin) == GPIO.HIGH

    def netejar(self):
        """Allibera els recursos del pin."""
        GPIO.cleanup(self.pin)