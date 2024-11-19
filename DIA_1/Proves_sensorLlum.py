import time

# Crea una instància del sensor
sensor_llum = SensorLlumBH1750(bus=1)  # Bus I2C 1

try:
    while True:
        # Llegeix la llum en lux
        llum = sensor_llum.llegir_llum()
        print(f"Llum detectada: {llum:.2f} lux")
        time.sleep(1)  # Llegeix cada segon
except KeyboardInterrupt:
    print("Aturant el programa.")
finally:
    sensor_llum.apagar()
    sensor_llum.tancar()