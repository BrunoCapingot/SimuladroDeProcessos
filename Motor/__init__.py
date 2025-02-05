import random
from datetime import datetime
from random import randint
from queue import Queue

class Motor:
    def __init__(self, View):
        self.fila_de_execucao = Queue()
        self.fila_de_dados = Queue()
        self.view = View
        self.suport_list = list()

    def preparar_execucao(self, execution_list: list, data_list: list) -> None:
        while not execution_list.__len__() == 0:
            self.fila_de_execucao.put(execution_list.pop())
        while not data_list.__len__() == 0:
            self.fila_de_dados.put(data_list.pop())
            #self.view.vw_add_process(pid=pre_processo.__dict__['pid'],tp=pre_processo.__dict__['tp'],nes=pre_processo.__dict__['nes'],
            #    n_cpu=pre_processo.__dict__['n_cpu'],quantum=pre_processo.__dict__['quantum'],cp=pre_processo.__dict__['cp'],
            #    ep=pre_processo.__dict__['ep']


    def executar_motor(self):
        while not self.fila_de_execucao.empty():
            dt = self.fila_de_execucao.get()
            dt.executar(View = self.view)