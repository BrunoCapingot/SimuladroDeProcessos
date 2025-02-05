

class Processo:
    def __init__(self, pid, tp, nes, n_cpu, quantum, cp, ep, Ram, Swap):#, prioridade, data_dict, Model, View
        self.pid = pid
        self.tp = tp
        self.cp = cp
        self.nes = nes
        self.ep = ep
        self.n_cpu = n_cpu
        self.quantum = quantum
        self.ram = Ram
        self.swap = Swap
        #self.data_dict = process_data
        #self.prioridade = prioridade
        #self.model = Model
        #self.view = View



    def executar(self):
        pass
