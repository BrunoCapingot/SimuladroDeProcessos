from sqlite3.dbapi2 import paramstyle

from Factory.Processo import Processo
from random import randint
import ctypes
import mmap

class NRU(Processo):
    def executar(self):
        counter = 0
        self.sorted_swap_pages_for_ram()
        while not self.ram.empty():
            dt = self.ram.get()
            sorted_instruction = randint(0, 99)
            if dt['I'] == sorted_instruction:
                dt['R'] = 1
                if self.sorted_m():
                    dt['M'] = 1

            else:
                """Remove o primeiro elemento com r = 0 da lista e sorteia dvn outro elemento do swap"""
                self.subistituicao_de_elemento()
            counter += 1
            if counter == 10:
                counter = 0
                suport_list = list()
                while not self.ram.empty():
                    dt = self.ram.get()
                    dt['R'] = 0
                    suport_list.append(dt)
                while suport_list.__len__() >= 0:
                    self.ram.put(suport_list.pop(0))

        # del condiction_dict

    """for condicao in condiction_dict.keys():
                    if condiction_dict[condicao][0] == dt['R'] and condiction_dict[condicao][1] == dt['M']:
                        condiction_dict[condicao][2]()"""



    def subistituicao_de_elemento(self):
        while not self.ram.empty():
            dt = self.ram.get()
            if dt['R'] == 0:
                self.ram.put(self.swap[randint(0, 99)])
                break
            else:
                self.ram.put(dt)

    def sorted_m(self):
        return randint(0, 99) <= 30

    def sorted_swap_pages_for_ram(self, counter=0, suport_list=list()):
        while not self.ram.empty():
            dt = self.ram.get()
            suport_list.append(self.swap[randint(0, 99)])
            counter += 1

        while suport_list.__len__() > 0:
            self.ram.put(suport_list.pop(0))

        del counter
        del suport_list

    def classe_um(self):
        pass

    def classe_dois(self):
        pass

    def classe_tres(self):
        pass

    def classe_quatro(self):
        pass