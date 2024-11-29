import Adafruit_DHT
import time

# Configuració del tipus de sensor i del pin GPIO
SENSOR = Adafruit_DHT.DHT11
GPIO_PIN = 22  # Pin GPIO22 per a SIGNAL

def read_dht11():
    """
    Llegeix la temperatura i la humitat del sensor DHT11.
    """
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, GPIO_PIN)
    
    if humidity is not None and temperature is not None:
        print(f"Temperatura: {temperature:.1f}°C")
        print(f"Humitat: {humidity:.1f}%")
    else:
        print("Error en la lectura del sensor. Intentant de nou...")

if __name__ == "__main__":
    print("Iniciant lectura del sensor DHT11...")
    try:
        while True:
            read_dht11()
            time.sleep(2)  # Espera 2 segons entre lectures
    except KeyboardInterrupt:
        print("\nLectura del sensor aturada.")
