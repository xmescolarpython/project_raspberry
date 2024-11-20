import spidev
import time

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