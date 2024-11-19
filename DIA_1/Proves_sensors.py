import time

# Exemple amb un LED al pin 17
led = LED(17)
try:
    led.encendre()
    time.sleep(1)
    led.apagar()
    time.sleep(1)
    led.canviar_estat()
    time.sleep(1)
finally:
    led.netejar()

# Exemple amb un sensor PIR al pin 18
pir = SensorPIR(18)
try:
    while True:
        if pir.detectar_moviment():
            print("Moviment detectat!")
        else:
            print("Cap moviment.")
        time.sleep(0.5)
finally:
    pir.netejar()

# Exemple amb una pantalla LCD
lcd = PantallaLCD(address=0x27, port=1)
try:
    lcd.escriure("Hola, món!", fila=0, columna=0)
    time.sleep(5)
    lcd.esborrar()
finally:
    lcd.apagar()