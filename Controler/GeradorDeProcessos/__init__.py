from Factory.Processo import Processo
import datetime

class ProcessGenerator:
    def __init__(self):
        self.process_list = list()


    def __add__(self, nome_do_processo:str,prioridade_do_processo:int,data_dict:dict,Model,View,quantum,cp):
        self.process_list.append(Processo(nome=nome_do_processo,
                                      prioridade=prioridade_do_processo,
                                      data_dict=data_dict,
                                      Model=Model,
                                      View=View,
                                      quantum=quantum,
                                      cp=cp
                                      ))

    def __set__(self, process_list:list):
        self.process_list = process_list


    def __generate_process__(self,time_process:int):
        """
        Exemplo de processo para criação
        IdentificadorDeMao(nome='IdentificadorDeMao', prioridade=10, data_dict=data_dict, Model=Model, View=View,quantum=datetime.datetime.now()+datetime.timedelta(seconds=10),cp=datetime.datetime.now()),
        :return:
        """
        for index in range(2,self.process_list.__len__()+1):
            self.process_list[index-1].__dict__['quantum'] = datetime.datetime.now()+datetime.timedelta(seconds=time_process*index)
            self.process_list[index-1].__dict__['cp'] = datetime.datetime.now()
        return self.process_list
