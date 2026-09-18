# Importa a classe e a função do arquivo estacionamento.py
from estacionamento import Estacionamento, limpar_tela

def main():
    limpar_tela()
    estacionamento = Estacionamento(total_vagas=10) 

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
                        estacionamento.listar_vagas_disponiveveis()
                    except ValueError:
                        print("\n[!] Por favor, digite um número válido para a vaga.")
                
                elif sub_opcao == '2':
                    try:
                        vaga = int(input("\nDigite o número da vaga que deseja desocupar: "))
                        estacionamento.desocupar_vaga(vaga)
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
            print("Salvando as informações do sistema...")
            estacionamento.salvar_dados()
            print("Sistema encerrado com segurança. Até logo!")
            break
            
        else:
            print("\n[!] Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()