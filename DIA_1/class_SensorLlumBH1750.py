import smbus2
import time

class SensorLlumBH1750:
    """Classe per gestionar el sensor de llum BH1750 via I2C."""
    # Adreça I2C del sensor
    BH1750_ADDRESS = 0x23

    # Modes de mesura
    POWER_DOWN = 0x00  # Apaga el sensor
    POWER_ON = 0x01    # Encén el sensor
    RESET = 0x07       # Reinicia el sensor
    CONTINUOUS_HIGH_RES_MODE = 0x10  # Mode d'alta resolució contínua

    def __init__(self, bus=1):
        """
        Inicialitza el sensor de llum BH1750.
        :param bus: Número del bus I2C (1 per a Raspberry Pi moderna).
        """
        self.bus = smbus2.SMBus(bus)
        self.address = self.BH1750_ADDRESS
        self._configurar_sensor()

    def _configurar_sensor(self):
        """Encén el sensor i el configura en mode d'alta resolució contínua."""
        self.bus.write_byte(self.address, self.POWER_ON)
        time.sleep(0.02)  # Temps per assegurar que s'inicia correctament
        self.bus.write_byte(self.address, self.CONTINUOUS_HIGH_RES_MODE)
        time.sleep(0.2)  # Temps per estabilitzar-se en mode d'alta resolució

    def llegir_llum(self):
        """
        Llegeix la intensitat de la llum en lux.
        :return: Valor de llum (lux) com a float.
        """
        data = self.bus.read_i2c_block_data(self.address, self.CONTINUOUS_HIGH_RES_MODE, 2)
        valor = (data[0] << 8) | data[1]  # Combina els dos bytes llegits
        lux = valor / 1.2  # Escala segons el factor del sensor
        return lux

    def apagar(self):
        """Apaga el sensor per estalviar energia."""
        self.bus.write_byte(self.address, self.POWER_DOWN)

    def tancar(self):
        """Tanca la comunicació amb el bus I2C."""
        self.bus.close()