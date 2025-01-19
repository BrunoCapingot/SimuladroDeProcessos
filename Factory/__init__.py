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


