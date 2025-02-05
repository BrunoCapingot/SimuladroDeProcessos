class View:
    def __init__(self) -> None:
        pass

        """
        print('__LEN__ :: {}'.format(self.suport_list.__len__()))
        print('Q_SIZE :: {}'.format(self.ram.qsize()))
        print('SOMA :: {}'.format(self.ram.qsize()+self.suport_list.__len__()))
        print('POINTER_SIZE :: {}'.format(self.pointer))
        """

    def vw_zerando_bits_r(self):
        print('Zerando bits R')

    def vw_substituicao_de_pagina(self):
        print('Substituindo pagina')

    def vw_acess_page(self, N, I, D, R, M, T, EP):
        print('<<---Acess Page--->>')
        print(f"N :: {N} I :: {I} D :: {D} R :: {R}, M :: {M}, T :: {T} :: {EP}")


    def vw_swap(self, N, I, D, R, M, T):
        print('<<---Swap Lines--->>')
        print(f"N :: {N} I :: {I} D :: {D} R :: {R}, M :: {M}, T :: {T}")

    def vw_ram(self, N, I, D, R, M, T):
        print('<<---Ram Lines--->>')
        print(f"N :: {N} I :: {I} D :: {D} R :: {R}, M :: {M}, T :: {T}")

    def vw_finalize_process(self,pid, tp, nes, n_cpu, quantum, cp, ep):
        print("PROCESSO FINALIZADO")
        print(f"PID :: {pid} TP :: {tp} NES :: {nes} N_CPU :: {n_cpu}, QUANTUM :: {quantum} CP :: {cp} EP :: {ep}")



    def vw_add_process(self,pid, tp, nes, n_cpu, quantum, cp, ep):
        print("ADICIONANDO PROCESSO")
        print(f"PID :: {pid} TP :: {tp} NES :: {nes} N_CPU :: {n_cpu}, QUANTUM :: {quantum} CP :: {cp} EP :: {ep}")

    def vw_desblok_process(self,pid, tp, nes, n_cpu, quantum, cp, ep):
        print("DESBLOQUEANDO PROCESSO")
        print(f"PID :: {pid} TP :: {tp} NES :: {nes} N_CPU :: {n_cpu}, QUANTUM :: {quantum} CP :: {cp} EP :: {ep}")

    def vw_blocked_process(self,pid, tp, nes, n_cpu, quantum, cp, ep):
        print("BLOQUEANDO PROCESSO PARA E/S DE DADOS")
        print(f"PID :: {pid} TP :: {tp} NES :: {nes} N_CPU :: {n_cpu}, QUANTUM :: {quantum} CP :: {cp} EP :: {ep}")

    def mostrar_base_dados_carregadas(self, base_dict):
        print(base_dict)

    def mostrar_execucao(self,nome_processo:str):
        print('View :: Executanto processo ->> {}'.format(nome_processo))

