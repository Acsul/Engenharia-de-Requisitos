import os

# Como estudante eu quero que tenha atualização em tempo real para saber
# onde há vagas disponíveis.
#

class Estacionamento:
    def __init__(self, total_vagas):
        self.total_vagas = total_vagas
        # Dicionário de vagas: {numero_vaga: placa_do_carro ou None}
        self.vagas = {i: None for i in range(1, total_vagas + 1)}
        # Dicionário de cadastros: {placa: nome_dono}
        self.carros_cadastrados = {}

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

        # Verifica se o carro já está em outra vaga
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
    # Limpa a tela do terminal (funciona em Linux/macOS e Windows)
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    estacionamento = Estacionamento(total_vagas=10) # Define 10 vagas como padrão

    while True:
        print("\n" + "="*30)
        print(" SISTEMA DE ESTACIONAMENTO ")
        print("="*30)
        print("1. Cadastrar Carro")
        print("2. Menu de Vagas (Ocupar / Desocupar)")
        print("0. Sair")
        print("="*30)
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            limpar_tela()
            print("--- CADASTRAR CARRO ---")
            placa = input("Digite a placa do carro: ")
            dono = input("Digite o nome do dono: ")
            estacionamento.cadastrar_carro(placa, dono)
            
        elif opcao == '2':
            limpar_tela()
            estacionamento.listar_vagas_disponiveveis()

            while True:
                print("\n--- MENU DE VAGAS ---")
                print("1. Ocupar Vaga")
                print("2. Desocupar Vaga")
                print("3. Listar placa e donos")
                print("0. Voltar ao Menu Principal")
                
                sub_opcao = input("Escolha uma opção: ")
                
                if sub_opcao == '1':
                    try:
                        vaga = int(input("\nDigite o número da vaga que deseja ocupar: "))
                        placa = input("Digite a placa do carro: ")
                        estacionamento.ocupar_vaga(vaga, placa)
                        # Atualiza a visualização das vagas após ocupar
                        estacionamento.listar_vagas_disponiveveis()
                    except ValueError:
                        print("\n[!] Por favor, digite um número válido para a vaga.")
                
                elif sub_opcao == '2':
                    try:
                        vaga = int(input("\nDigite o número da vaga que deseja desocupar: "))
                        estacionamento.desocupar_vaga(vaga)
                        # Atualiza a visualização das vagas após desocupar
                        estacionamento.listar_vagas_disponiveveis()
                    except ValueError:
                        print("\n[!] Por favor, digite um número válido para a vaga.")

                elif sub_opcao == '3':
                    estacionamento.listar_carros_cadastrados()
                        
                elif sub_opcao == '0':
                    limpar_tela()
                    break
                else:
                    print("\n[!] Opção inválida no submenu.")

        elif opcao == '0':
            limpar_tela()
            print("Saindo do sistema...")
            break
            
        else:
            print("\n[!] Opção inválida. Tente novamente.")

if __name__ == "__main__":
    limpar_tela()
    main()