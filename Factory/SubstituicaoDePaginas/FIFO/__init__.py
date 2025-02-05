from queue import Queue
from random import randint

class FIFO:
    def __init__(self, Ram: Queue, Swap: list):
        self.ram = Ram
        self.swap = Swap
        self.suport_list = list()


    def executar(self, View):
        counter = 0
        for _ in range(0,100):
            sorted_instruction = randint(0, 99)
            pagina = self.verifica_pagina_sorteada(sorted_instruction=sorted_instruction)
            if pagina:
                View.vw_acess_page(**pagina)
                self.atualizar_bits(pagina=pagina)
                self.ram.put(pagina)

            else:
                self.substitui_pagina()
                View.vw_substituicao_de_pagina()
            counter +=1
            if counter == 10:
                View.vw_zerando_bits_r()
                self.zerar_bits_r()
                counter = 0

    def zerar_bits_r(self):
        while not self.ram.empty():
            dt = self.ram.get()
            dt['R'] = 0
            self.suport_list.append(dt)
        while self.suport_list:
            self.ram.put(self.suport_list.pop(0))


    def substitui_pagina(self):
        while not self.ram.empty():
            dt = self.ram.get()
            if dt['R'] == 0:
                dte = self.swap[randint(1, 99)]
                self.ram.put(dte)
                break
            else:
                self.suport_list.append(dt)
        while self.suport_list:
            self.ram.put(self.suport_list.pop(0))

    def atualizar_bits(self, pagina):
        pagina['R'] = 1
        if self.sorted_m():
            pagina['M'] = 1
            pagina['D'] += 1

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


