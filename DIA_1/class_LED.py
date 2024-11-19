import RPi.GPIO as GPIO

class LED:
    def __init__(self, pin):
        """
        Inicialitza el LED configurant el pin com a sortida.
        :param pin: Número del pin GPIO on està connectat el LED.
        """
        self.pin = pin
        GPIO.setmode(GPIO.BCM)  # Utilitza el mode BCM (numeració GPIO)
        GPIO.setup(self.pin, GPIO.OUT)  # Configura el pin com a sortida

    def encendre(self):
        """Encén el LED."""
        GPIO.output(self.pin, GPIO.HIGH)

    def apagar(self):
        """Apaga el LED."""
        GPIO.output(self.pin, GPIO.LOW)

    def canviar_estat(self):
        """Canvia l'estat actual del LED (encès/apagat)."""
        estat_actual = GPIO.input(self.pin)
        GPIO.output(self.pin, not estat_actual)

    def netejar(self):
        """Allibera els recursos del pin."""
        GPIO.cleanup(self.pin)