import time
from picamera import PiCamera

class CameraPi:
    def __init__(self, resolution=(1024, 768), framerate=30):
        # Inicialització de la càmera amb la resolució i el framerate
        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        print("Càmera inicialitzada")

    def capture_image(self, image_path='/home/pi/imatge.jpg'):
        # Captura una imatge i la desa a la ruta especificada
        print("Capturant imatge...")
        self.camera.capture(image_path)
        print(f"Imatge capturada i desada a {image_path}")

    def record_video(self, video_path='/home/pi/video.h264', duration=10):
        # Enregistra un vídeo durant la durada especificada en segons
        print("Enregistrant vídeo...")
        self.camera.start_recording(video_path)
        time.sleep(duration)
        self.camera.stop_recording()
        print(f"Vídeo enregistrat a {video_path}")

    def close(self):
        # Tanca la càmera correctament
        self.camera.close()
        print("Càmera tancada")

# Exemple d'ús
if __name__ == "__main__":
    camera = CameraPi()  # Inicialitza la càmera
    camera.capture_image('/home/pi/imatge.jpg')  # Captura una imatge
    camera.record_video('/home/pi/video.h264', 5)  # Enregistra un vídeo de 5 segons
    camera.close()  # Tanca la càmera
