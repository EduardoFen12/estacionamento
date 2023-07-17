# ===================================================================================================


# FUNÇÕES:


def menu():

    resposta = ' '

    while resposta not in ['e', 's', 'l', 'f', 't']:
        
        resposta = input(''' 
        > > > ESTACIONAMENTO < < < 
        Selecione uma operação: 
        [e] - Entrada de carro 
        [s] - Saída de carro 
        [l] - Listar carros 
        [f] - Fechar estacionamento 
        [t] - Terminar Programa 
        > > > Informe uma operação: 
        ''' ).lower()

        if resposta not in ['e', 's', 'l', 'f', 't']:
            print("Resposta inválida!")

    return resposta


def ler_placa_valida(dicionario_estacionamento, nova=True):

    if nova:

        placa = input('Informe a placa: ')

        while placa in dicionario_estacionamento:

            placa = input("Placa inválida (já está no estacionamento) informe outra placa: ")

        return placa.upper()

    if not nova:

        placa = input('Informe a placa: ').upper()

        while placa not in dicionario_estacionamento:

            placa = input("Placa inválida (não está no estacionamento) informe outra placa: ")

        return placa



def entrada(dicionario_estacionamento, placa):

    hora = input("Informe a hora de entrada (use o formato HH:MM): ")
   
    dicionario_estacionamento[placa] = hora


def total_minutos(hora, placa, tarifa, diconario_estacionamento):
    
    dicionario_saida = {}
    m_entrada = int()
    m_saida = int()

    hm_entrada = diconario_estacionamento[placa]
    h_e, m_e = hm_entrada.split(":")
    h_s, m_s = hora.split(":")

    m_entrada = int(m_e) + (int(h_e) * 60)
    m_saida = int(m_s) + (int(h_s) * 60)

    total_minutos = m_saida - m_entrada
    valor_total = float(total_minutos) * tarifa

    dados = {}
    dados['total'] = valor_total
    dados['minutos'] = total_minutos
    dicionario_saida[placa] = dados

    diconario_estacionamento.pop(placa)   

    return dicionario_saida  


def listar_carros(dicionario_estacionamento):

    print("PLACA    ENTRADA")

    for chave in dicionario_estacionamento:

        print(f"{chave}  {dicionario_estacionamento[chave]}")


def calcula_valor_total(dicionario_saida):
    
    soma = 0

    for chave in dicionario_saida:

        soma += dicionario_saida[chave]['total']

    return soma


def calcula_tempo_medio(dicionario_saida):
    
    soma = 0
    media = 0

    for chave in dicionario_saida:

        soma += dicionario_saida[chave]['minutos']

    media = soma / len(dicionario_saida)

    return media


def fechar(dicionario_estacionamento, dicionario_saida):

    if len(dicionario_estacionamento) != 0:

        print("Não posso fechar, pois ainda tem carros no estacionamento")
        listar_carros(dicionario_estacionamento)

    else:

        print(f"Foram arrecadados R${calcula_valor_total(dicionario_saida):.2f}")
        print(f"Os clientes ficaram em média {calcula_tempo_medio(dicionario_saida):.2f} minutos")
        
        
# ===================================================================================================


# VARIÁVEIS:


tarifa = float(input("Informe a tarifa por minuto do estacionamento: "))

''' Exemplo do dicionário de entrada:
{ 
    'aaa1111': '14:00',
    'bbb2222': '14:30',
    'ccc3333': '21:30'
}
'''
estacionamento = {}

''' Exemplo do dicionário de saída
{
 'aaa1111': {'total': 7.2, 'minutos': 90},
 'bbb2222': {'total': 34.08, 'minutos': 426}, 
 'ccc3333': {'total': 9.6, 'minutos': 120}
}
'''
saida = {}


# ===================================================================================================


################# Programa Principal #################


resposta_menu = menu()

while resposta_menu != 't':

    match resposta_menu:

        case 'e':

            entrada(estacionamento, ler_placa_valida(estacionamento))
            resposta_menu = menu()

        case 's':

            placa = ler_placa_valida(estacionamento, False)

            hora_entrada = estacionamento[placa]
            hora_saida = input("Informe a hora de saida (use o formato HH:MM): ")

            saida = total_minutos(hora_saida, placa, tarifa, estacionamento)

            print(f"CARRO: {placa.upper()}")
            print(f"ENTRADA {hora_entrada} - SAIDA {hora_saida} = {saida[placa]['minutos']} minutos")
            print(f"TOTAL A PAGAR: R${saida[placa]['total']:.2f}")
            resposta_menu = menu()

        case 'l':

            listar_carros(estacionamento)
            resposta_menu = menu()
        
        case 'f':
            fechar(estacionamento, saida)
            resposta_menu = menu()

print("ENCERRANDO O PROGRAMA...")
