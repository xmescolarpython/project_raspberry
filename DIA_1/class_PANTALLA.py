from RPLCD.i2c import CharLCD

class PantallaLCD:
    def __init__(self, address, port):
        """
        Inicialitza la pantalla LCD connectada via I2C.
        :param address: Adreça I2C de la pantalla (per exemple, 0x27).
        :param port: Port I2C (normalment 1 per Raspberry Pi).
        """
        self.lcd = CharLCD('PCF8574', address, port=port)

    def escriure(self, text, fila=0, columna=0):
        """
        Escriu text a la pantalla LCD en una posició concreta.
        :param text: Text a escriure.
        :param fila: Número de la fila (0-1 per a una pantalla de 2 línies).
        :param columna: Número de la columna inicial (0-15 per a 16 columnes).
        """
        self.lcd.cursor_pos = (fila, columna)
        self.lcd.write_string(text)

    def esborrar(self):
        """Esborra tot el contingut de la pantalla."""
        self.lcd.clear()

    def apagar(self):
        """Apaga la retroil·luminació de la pantalla."""
        self.lcd.backlight_enabled = False

    def encendre(self):
        """Encén la retroil·luminació de la pantalla."""
        self.lcd.backlight_enabled = True