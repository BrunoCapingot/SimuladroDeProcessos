import random
from Factory.SubstituicaoDePaginas.NRU import NRU
from Factory.SubstituicaoDePaginas.CLOCK import CLOCK
from Factory.SubstituicaoDePaginas.FIFO import FIFO
from Factory.SubstituicaoDePaginas.FIFO_SC import FIFO_SC
from Factory.Processo import Processo
from queue import Queue


class Factory:
    def __init__(self):
        """
        def cadastro_site_inadiplentes(self, datalist, Model, View) -> list:
            return [ProcessoExemplo(nome='ProcessoExemplo', prioridade=int, datalist=datalist, Model=Model, View=View)]
        """
        self.ram_queue =Queue()
        self.swap_list = list()

    def get_nru(self):
        return NRU(pid=0, ep="PRONTO", cp=0, tp=0, n_cpu=0, quantum=0, nes=0, Ram=self.ram_queue, Swap=self.swap_list)

    def get_fifo(self):
        self.generate_matriz_swap()
        self.generate_matriz_ram()

        return [FIFO(Ram=self.ram_queue,Swap=self.swap_list)]

    def get_fifo_sc(self):
        self.generate_matriz_swap()
        self.generate_matriz_ram()
        return [FIFO_SC(Ram=self.ram_queue,Swap=self.swap_list)]

    def get_clock(self):
        self.generate_matriz_swap()
        self.generate_matriz_ram()
        return [CLOCK(Ram=self.ram_queue,Swap=self.swap_list)]

    def generate_matriz_ram(self):
        for linha in range(1, 10):
            self.ram_queue.put(self.swap_list[random.randint(0,99)])
        return self.ram_queue

    def generate_matriz_swap(self):
        for linha in range(100):
            self.swap_list.append(dict(N=linha, I=linha+1, D=random.randint(1,50), R=0, M=0, T=random.randint(100,9999), EP=0))
        return self.swap_list

    def generete_process_list(self):
        process_list = list()
        for number_processo in range(0,1000):
            process_list.append(Processo(pid=number_processo, tp=0, nes=0, n_cpu=0, quantum=1000, cp=1, ep="PRONTO"))
        return process_list


