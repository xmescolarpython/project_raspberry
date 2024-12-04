import time
from picamera import PiCamera

# Crear una instància de PiCamera
camera = PiCamera()

# Configurar les propietats de la càmera (opcional)
camera.resolution = (1024, 768)  # Resolució de la imatge
camera.framerate = 30  # Nombre de fotogrames per segon

# Inicialitzar la càmera
print("Preparant la càmera...")
time.sleep(2)  # Temps per esperar que la càmera es prepari

# Capturar una imatge
print("Capturant la imatge...")
camera.capture('/home/pi/imatge.jpg')  # El camí on es guarda la imatge

print("Imatge capturada correctament.")

# Tanquem la càmera un cop hem acabat
camera.close()
