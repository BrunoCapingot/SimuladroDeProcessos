from queue import Queue
from random import randint

class CLOCK:
    def __init__(self, Ram: Queue, Swap: list):
        self.ram = Ram
        self.swap = Swap
        self.suport_list = list()
        self.pointer = 0
        self.q_size = self.ram.qsize()+self.suport_list.__len__()
        self.counter = 0

    def executar(self, View):
        for _ in range(0, 100):
            dt = self.ram.get()
            self.suport_list.append(dt)
            pagina_sorteada = self.buscar_pagina_na_fila()
            if pagina_sorteada:
                View.vw_acess_page(**pagina_sorteada)
                self.atualizar_bits(pagina=pagina_sorteada)
                self.ram.put(pagina_sorteada)
            else:
                self.substitui_pagina()
                View.vw_substituicao_de_pagina()

            if self.pointer == self.q_size:
                self.pointer = 0

            self.counter += 1
            if self.counter == 10:
                View.vw_zerando_bits_r()
                self.zerar_bits_r()
                self.counter = 0

    def buscar_pagina_na_fila(self):
        pagina_encontrada = None
        # Usando a lista de apoio (suport_list) para armazenar as páginas da RAM sem consumi-las
        for i, dt in enumerate(self.ram.queue):
            if i == self.pointer:
                pagina_encontrada = dt
                break
        self.transferir_suport_list_for_ram_queue()
        return pagina_encontrada

    def zerar_bits_r(self):
        while not self.ram.empty():
            dt = self.ram.get()
            dt['R'] = 0
            self.avancar_ponteiro()
            self.suport_list.append(dt)

        self.transferir_suport_list_for_ram_queue()

    def avancar_ponteiro(self):
        if self.pointer == self.q_size:
            self.pointer = 0
        else:
            self.pointer += 1

    def substitui_pagina(self):
        while not self.ram.empty():
            dt = self.ram.get()
            if dt['R'] == 0:
                dt['R'] = 1
                nova_pagina = self.swap[randint(0, 99)]
                self.ram.put(nova_pagina)
                break
            else:
                self.avancar_ponteiro()
                dt['EP'] += 1

        self.transferir_suport_list_for_ram_queue()


    def atualizar_bits(self, pagina):
        pagina['R'] = 1
        if self.sorted_m():
            pagina['M'] = 1
            pagina['D'] += 1

    def transferir_suport_list_for_ram_queue(self):
        while self.suport_list:
            self.ram.put(self.suport_list.pop(0))

    def sorted_m(self)->bool:
        if randint(1,100) >= 50: return True

    def verifica_pagina_sorteada(self,sorted_instruction) -> dict:
        while not self.ram.empty():
            dt = self.ram.get()
            if dt['I'] == sorted_instruction:
                while self.suport_list:
                    self.ram.put(self.suport_list.pop(0))
                return  dt
            self.suport_list.append(dt)


