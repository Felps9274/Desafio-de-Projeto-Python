saldo = 0
deposito = 0
saque = 0
saque_maximo = 500
limite_de_saques = 3
extrato = ''
opcao = -1

mais_operacao = '''
Deseja realizar uma nova operação?
       1- Sim      2- Não        
'''

menu = '''
============== OPERAÇÕES =============
[1] DEPÓSITO - [2] SAQUE - [3] EXTRATO
               [0] SAIR 
======================================
'''

while opcao != 0:
    opcao = int(input(menu))
    if opcao == 1:
        deposito = float(input('Valor do depósito R$'))
        extrato += f'\nDepósito de R${deposito:.2f}'
        saldo += deposito
        print('DEPÓSITO REALIZADO COM SUCESSO!')
        opcao = int(input(mais_operacao))
        if opcao == 1:
            continue
        elif opcao != 2:
            print('opção inválida! retornando ao menu...')
            continue
        else:
            break
    elif opcao == 2:
        if limite_de_saques <= 0:
                print('Limite de saques diário atingido! Retorne em 24h')
                continue
        saque = float(input('Digite o valor do saque R$'))
        if saque <= saque_maximo:
            if saque <= saldo:
                extrato += f'\nSaque de R${saque:.2f}'
                saldo -= saque
                limite_de_saques -= 1
                print('SAQUE REALIZADO COM SUCESSO, RETIRE AS CÉDULAS NO LOCAL INDICADO -->')
                opcao = int(input(mais_operacao))
                if opcao == 1:
                    continue
                elif opcao != 2:
                    print('opção inválida! retornando ao menu...')
                    continue
                else:
                    break
            else:
                print('SALDO INSUFICIENTE!')
                continue
        else:
            print(f'Valor acima do valor máximo para saque (MAX R${saque_maximo:.2f})')
            continue
    elif opcao == 3:
        if extrato == '':
            print('NENHUMA OPERAÇÃO REALIZADA!')
            continue
        else:
            print(f'''========== EXTRATO ==========={extrato}\n\nSaldo atual R${saldo:.2f}''')
            opcao = int(input(mais_operacao))
            if opcao == 1:
               continue
            elif opcao != 2:
               print('opção inválida! retornando ao menu...')
               continue
            else:
               break
    else:
        opcao = 0

print('Operação Finalizada! Obrigado por nos escolher!')


