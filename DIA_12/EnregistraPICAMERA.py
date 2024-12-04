import time
from picamera import PiCamera

# Crear una instància de PiCamera
camera = PiCamera()

# Configurar la càmera (opcional)
camera.resolution = (1280, 720)  # Resolució del vídeo
camera.framerate = 30  # Nombre de fotogrames per segon

# Inicialitzar la càmera
print("Preparant la càmera...")
time.sleep(2)  # Temps per esperar que la càmera es prepari

# Iniciar l'enregistrament de vídeo
print("Enregistrant el vídeo...")
camera.start_recording('/home/pi/video.h264')  # Especifica on guardar el vídeo
time.sleep(10)  # Gravar durant 10 segons

# Aturar l'enregistrament
print("Aturant el vídeo...")
camera.stop_recording()

# Tanquem la càmera
camera.close()
