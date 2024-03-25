import time
import configparser
import cv2
import threading

config_file = "config.cfg"

def load_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config

thread = threading.Thread(target=load_config, args=(config_file,))
thread.daemon = True
thread.start()

def webcam():
    cap = cv2.VideoCapture(0)
    while True:
        config = load_config(config_file)
        setting1 = config["AppConfig"]["setting1"]
        ret, frame = cap.read()
        if ret:
            if setting1 == str(1):
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            else:
                frame = frame
            teks = config.get('AppConfig', 'setting1')
            posisi = (50, 50)  # Koordinat x dan y di mana teks akan ditambahkan
            font = cv2.FONT_HERSHEY_SIMPLEX
            skala_font = 1
            warna = (0, 0, 255)  # Warna teks dalam format BGR (merah dalam contoh ini)
            ketebalan = 2
            cv2.putText(frame, teks, posisi, font, skala_font, warna, ketebalan)
            cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    webcam()

    
   
  
