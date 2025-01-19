from Factory.Processo import Processo
from ultralytics import YOLO
import cv2
import datetime
import logging
class YoloIdentificadorObjetoPorImagem(Processo):
    def executar(self):
        logging.getLogger("ultralytics").setLevel(logging.WARNING)
        model = YOLO("yolo11x.pt")
        results = model(r'C:\Users\CPGT\PycharmProjects\IA\IdentificadoresYM\imagem_7.jpg')
        annotated_frame = results[0].plot()
        cv2.imwrite(r'C:\Users\CPGT\PycharmProjects\IA\IdentificadoresYM\annoted_image.jpg', annotated_frame)
        while self.__dict__['cp'] <= self.__dict__['quantum']:
            cv2.imshow("Detecção YOLO", annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            self.__dict__['cp'] = datetime.datetime.now()