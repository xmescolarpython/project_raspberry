import time

# Crea una instància del sensor al pin GPIO 4
sensor = SensorDHT11(pin=4)

try:
    while True:
        # Llegeix les dades
        temperatura = sensor.llegir_temperatura()
        humitat = sensor.llegir_humitat()
        
        if temperatura is not None and humitat is not None:
            print(f"Temperatura: {temperatura:.1f} °C, Humitat: {humitat:.1f} %")
        else:
            print("Error llegint dades del sensor.")
        
        time.sleep(2)  # Llegeix cada 2 segons
except KeyboardInterrupt:
    print("Programa aturat.")