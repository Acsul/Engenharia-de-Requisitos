import os
import json
import time

class Estacionamento:
    def __init__(self, total_vagas, arquivo_dados='dados_estacionamento.json'):
        self.total_vagas = total_vagas
        self.arquivo_dados = arquivo_dados
        self.vagas = {i: None for i in range(1, total_vagas + 1)}
        self.carros_cadastrados = {}
        
        self.carregar_dados()

    def carregar_dados(self):
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                    
                    self.total_vagas = dados.get('total_vagas', self.total_vagas)
                    self.carros_cadastrados = dados.get('carros_cadastrados', {})
                    
                    vagas_salvas = dados.get('vagas', {})
                    if vagas_salvas:
                        self.vagas = {int(num_vaga): placa for num_vaga, placa in vagas_salvas.items()}
                        
                print(f"\n[+] Dados recuperados do arquivo '{self.arquivo_dados}' com sucesso!")
                time.sleep(2)
            except Exception as e:
                print(f"\n[!] Erro ao tentar ler o arquivo salvo: {e}")
                time.sleep(2)

    def salvar_dados(self):
        dados_para_salvar = {
            'total_vagas': self.total_vagas,
            'carros_cadastrados': self.carros_cadastrados,
            'vagas': self.vagas
        }
        try:
            with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
                json.dump(dados_para_salvar, f, indent=4, ensure_ascii=False)
            print(f"[+] Dados salvos com sucesso em '{self.arquivo_dados}'!")
        except Exception as e:
            print(f"[!] Ocorreu um erro ao salvar os dados: {e}")

    def cadastrar_carro(self, placa, dono):
        placa = placa.upper()
        if placa in self.carros_cadastrados:
            print(f"\n[!] O carro com placa {placa} já está cadastrado.")
        else:
            self.carros_cadastrados[placa] = dono
            print(f"\n[+] Carro {placa} (Dono: {dono}) cadastrado com sucesso!")

    def listar_vagas_disponiveveis(self):
        print("\n--- Status das Vagas ---")
        vagas_livres = 0
        for num, placa in self.vagas.items():
            if placa is None:
                print(f"Vaga {num:02d}: [ LIVRE ]")
                vagas_livres += 1
            else:
                dono = self.carros_cadastrados.get(placa, "Desconhecido")
                print(f"Vaga {num:02d}: [ OCUPADA por {placa} - {dono} ]")
        
        print(f"\nTotal de vagas livres: {vagas_livres}/{self.total_vagas}")

    def listar_carros_cadastrados(self):
        print("\n--- Carros Cadastrados ---")
        if not self.carros_cadastrados:
            print("[!] Nenhum carro cadastrado no sistema ainda.")
        else:
            for placa, dono in self.carros_cadastrados.items():
                print(f"Placa: {placa} | Dono: {dono}")

    def ocupar_vaga(self, num_vaga, placa):
        placa = placa.upper()
        
        if num_vaga not in self.vagas:
            print("\n[!] Número de vaga inválido.")
            return

        if self.vagas[num_vaga] is not None:
            print(f"\n[!] A vaga {num_vaga} já está ocupada.")
            return

        if placa not in self.carros_cadastrados:
            print(f"\n[!] Placa {placa} não cadastrada. Cadastre o carro primeiro.")
            return

        if placa in self.vagas.values():
            print(f"\n[!] O carro {placa} já está ocupando uma vaga.")
            return

        self.vagas[num_vaga] = placa
        print(f"\n[+] Vaga {num_vaga} ocupada com sucesso pelo carro {placa}.")

    def desocupar_vaga(self, num_vaga):
        if num_vaga not in self.vagas:
            print("\n[!] Número de vaga inválido.")
            return

        if self.vagas[num_vaga] is None:
            print(f"\n[!] A vaga {num_vaga} já está livre.")
            return

        placa = self.vagas[num_vaga]
        self.vagas[num_vaga] = None
        print(f"\n[-] Vaga {num_vaga} desocupada. (Carro {placa} saiu).")


def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')