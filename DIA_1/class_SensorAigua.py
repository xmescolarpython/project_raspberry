import RPi.GPIO as GPIO

class SensorAigua:
    def __init__(self, pin):
        """
        Inicialitza el sensor d'aigua/humitat configurant el pin com a entrada.
        :param pin: Número del pin GPIO on està connectat el sensor.
        """
        self.pin = pin
        GPIO.setmode(GPIO.BCM)  # Mode BCM (numeració GPIO)
        GPIO.setup(self.pin, GPIO.IN)  # Configura el pin com a entrada

    def detecta_aigua(self):
        """
        Detecta la presència d'aigua o humitat alta.
        :return: True si es detecta aigua, False si no es detecta.
        """
        return GPIO.input(self.pin) == GPIO.HIGH

    def netejar(self):
        """Allibera els recursos del pin."""
        GPIO.cleanup(self.pin)