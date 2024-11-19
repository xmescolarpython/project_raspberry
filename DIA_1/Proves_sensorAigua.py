import time

sensor = SensorAigua(pin=18)  # Pin GPIO 18

try:
    while True:
        if sensor.detecta_aigua():
            print("Aigua detectada!")
        else:
            print("Cap aigua detectada.")
        time.sleep(1)
finally:
    sensor.netejar()