import spidev
import time

class SensorHumitatTerraYI69:
  
    def __init__(self, canal=0, bus=0, device=0):
        self.canal = canal
        self.bus = bus
        self.device = device
        
        # Inicialitzacio de l'ADC MCP3008
        self.spi = spidev.SpiDev()
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz = 1350000  # Configuracio de la velocitat SPI

    def llegir_analogic(self):

        # Enviar la comanda per llegir del canal seleccionat
        request = [1, (8 + self.canal) << 4, 0]
        resposta = self.spi.xfer2(request)
        
        # Convertir la resposta de l'ADC (10 bits)
        resultat = ((resposta[1] & 3) << 8) + resposta[2]
        return resultat

    def llegir_humitat(self):
        # Llegeix el valor analogic
        valor_analogic = self.llegir_analogic()
        
        # Convertir el valor a percentatge de humitat (0-100%)
        # Considerant que el sensor te un rang de 0 (sec) a 1023 (molt humit).
        humitat = (valor_analogic / 1023.0) * 100
        return humitat

    def tancar(self):
        self.spi.close()

# Prova de la classe
if __name__ == "__main__":
    try:
        # Crear una instancia del sensor
        print("Prova obrir ")
        sensor = SensorHumitatTerraYI69()

        # Llegir i mostrar valors d'humitat cada segon
        print("Llegeixo valors d'humitat del sensor YI-69 (Ctrl+C per aturar).")
        while True:
            humitat = sensor.llegir_humitat()
            print(f"Humitat del sol: {humitat:.2f}%")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nLectura aturada per l'usuari.")
    finally:
        # Tancar la connexio SPI abans de sortir
        sensor.tancar()

