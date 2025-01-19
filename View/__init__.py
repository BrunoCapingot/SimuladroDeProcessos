class View:
    def __init__(self) -> None:
        pass

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

