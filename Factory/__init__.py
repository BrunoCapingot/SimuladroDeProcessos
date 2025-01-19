import datetime


from Factory.YoloIdentificadorObjeto import YoloIdentificadorObjeto
from Factory.YoloIdentificadorObjetoPorImagem import YoloIdentificadorObjetoPorImagem
from Factory.YoloSegmentadorDeObjeto import YoloSegmentadorDeObjeto
from Factory.YoloIdentificadorPose import YoloIdentificadorPose
from Factory.YoloIdentificadorClassificador import YoloIdentificadorClassificador
from Factory.YoloTreinoRedeNeural import YoloTreinoRedeNeural
from Factory.YoloIdentificadorTreinoCustomizado import YoloIdentificadorTreinoCustomizado
from Factory.Processo import Processo


class Factory:
    def __init__(self):
        """
        def cadastro_site_inadiplentes(self, datalist, Model, View) -> list:
            return [ProcessoExemplo(nome='ProcessoExemplo', prioridade=int, datalist=datalist, Model=Model, View=View)]
        """

        pass


    def generete_process_list(self):
        process_list = list()
        for number_processo in range(0,1000):
            process_list.append(Processo(pid=number_processo, tp=0, nes=0, n_cpu=0, quantum=1000, cp=1, ep="PRONTO"))
        return process_list


    def treinar_rede_neural(self, data_dict: dict, Model, View) -> list:
        return [YoloTreinoRedeNeural(nome='YoloTreinoRedeNeural', prioridade=10, data_dict=data_dict, Model=Model, View=View,quantum=datetime.datetime.now()+datetime.timedelta(seconds=10),cp=datetime.datetime.now())]




    def executar_identificadores_yolo_customizado(self, data_dict:dict, Model, View) -> list:
        return [YoloIdentificadorTreinoCustomizado(nome='YoloIdentificadorTreinoCustomizado', prioridade=10, data_dict=data_dict, Model=Model, View=View, quantum=datetime.datetime.now() + datetime.timedelta(seconds=10), cp=datetime.datetime.now())]


    def executar_identificadores_yolo(self, data_dict:dict, Model, View) -> list:
        return [
            YoloIdentificadorObjeto(nome='YoloIdentificadorObjeto', prioridade=10, data_dict=data_dict, Model=Model, View=View,quantum=datetime.datetime.now()+datetime.timedelta(seconds=10),cp=datetime.datetime.now(), ep='PRONTO'),
            YoloIdentificadorClassificador(nome='YoloIdentificadorClassificador', prioridade=10, data_dict=data_dict, Model=Model, View=View, quantum=datetime.datetime.now() + datetime.timedelta(seconds=20), cp=datetime.datetime.now(), ep='PRONTO'),
            YoloSegmentadorDeObjeto(nome='YoloSegmentadorDeObjeto', prioridade=10, data_dict=data_dict, Model=Model, View=View,quantum=datetime.datetime.now()+datetime.timedelta(seconds=30),cp=datetime.datetime.now(), ep='PRONTO'),
            YoloIdentificadorPose(nome='YoloIdentificadorPose', prioridade=10, data_dict=data_dict, Model=Model, View=View,quantum=datetime.datetime.now()+datetime.timedelta(seconds=40),cp=datetime.datetime.now(), ep='PRONTO'),

            #YoloIdentificadorObjetoPorImagem(nome='YoloIdentificadorObjetoPorImagem', prioridade=10, data_dict=data_dict, Model=Model, View=View,quantum=datetime.datetime.now()+datetime.timedelta(seconds=10),cp=datetime.datetime.now()),

        ]


