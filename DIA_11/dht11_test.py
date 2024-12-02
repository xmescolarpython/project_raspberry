import time
import board
import adafruit_dht

# Inicialitza el dispositiu DHT11 al pin GPIO4
dhtDevice = adafruit_dht.DHT11(board.D4)

try:
    while True:
        # Llegeix la temperatura i la humitat
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        if temperature_c is not None and humidity is not None:
            print(f"Temperatura: {temperature_c:.1f}°C")
            print(f"Humitat: {humidity:.1f}%")
        else:
            print("Error en la lectura del sensor. Intentant de nou...")
        time.sleep(2.0)
except KeyboardInterrupt:
    print("\nLectura del sensor aturada.")
except Exception as error:
    dhtDevice.exit()
    raise error
