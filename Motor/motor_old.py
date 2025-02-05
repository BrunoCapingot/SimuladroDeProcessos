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
            #)


    def desblok_process(self):
        return randint(1, 100) <= 30

    def e_s_chance(self):
        return randint(1, 100) <= 1

    def executar_motor_os(self):
        lista = list()
        while not self.fila_de_execucao.empty():
            processo = self.fila_de_execucao.get()
            if processo.__dict__['ep'] == 'PRONTO':
                processo.__dict__['ep'] = 'EXECUTANDO'
                processo.__dict__['quantum'] = 1000
                self.view.vw_add_process(**processo.__dict__)
            while processo.__dict__['quantum'] > processo.__dict__['cp']:
                processo.__dict__['tp'] += 1
                processo.__dict__['cp'] = processo.__dict__['tp'] + 1
                ###SE FAZ ENTRADA OU SAIDA DE DADOS###
                if self.e_s_chance():
                    processo.__dict__['ep'] = 'BLOQUEADO'
                    processo.__dict__['nes'] += 1
                    self.view.vw_blocked_process(**processo.__dict__)
                    self.fila_de_execucao.put(processo)
                    break

                ###SE NAO FAZ ENTRADA OU SAIDA DE DADOS E FINALIZA SEU QUANTUM SENDO ASSIM, EXECUÇÃO###
                if processo.__dict__['cp'] <= processo.__dict__['quantum'] and processo.__dict__['ep'] != 'BLOQUEADO' and processo.__dict__['ep'] != 'PRONTO':
                    processo.__dict__['ep'] = 'PRONTO'
                    processo.__dict__['n_cpu'] += 1
                    self.fila_de_execucao.put(processo)

                ###SE O PROCESSO ESTA BLOQUEADO, TEM 30% DE CHANCE PRA LIBERAR ELE E VOLTAR O ESTADO PRA PRONTO PARA SER EXECUTADO DNV###
                if processo.__dict__['ep'] == 'BLOQUEADO':
                    if self.desblok_process():
                        processo.__dict__['ep'] = 'PRONTO'
                        self.view.vw_desblok_process(**processo.__dict__)
                        self.fila_de_execucao.put(processo)

                if processo.__dict__['cp'] >= processo.__dict__['quantum']:  # print(f"{processo.__dict__['pid']} FINALIZADO: {processo.__dict__}")
                    processo.__dict__['ep'] = 'FINALIZADO'
                    self.view.vw_finalize_process(**processo.__dict__)
                    lista.append(processo)

        for processo in lista:
            print(f"PID {processo.__dict__['pid']} :: TP {processo.__dict__['tp']} :: CP {processo.__dict__['cp']} :: NES {processo.__dict__['nes']} :: EP {processo.__dict__['ep']} :: N_CPU {processo.__dict__['n_cpu']} ::  QUANTUM {processo.__dict__['quantum']}")