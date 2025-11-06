#OBJETIVOS: CRIAR UM MENU INTERATIVO QUE CONTENHA:

#1° UMA VARIÁVEL QUE ARMAZENE ESTADO;
#2° UMA VARIÁVEL QUE ARMAZENE MUNICÍPIO;
#3° UMA VARIÁVEL QUE JUNTA AS OUTRAS VARIÁVEIS(INFORMAÇÕES).

from time import sleep



def menu():
    print('\033[1;37m-=\033[0m' * 15)
    print('\033[1;33mMENU INTERATIVO:\033[0m')
    print('\033[1;37m-=\033[0m' * 15)

    print('Bem-vindo(a) ao AppClimaBom!')
    print('O aplicaivo que mostra o clima na região que você quiser!')

    print('ADICIONAR ESTADO: ')
    estado = str(input())

    print('ADICIONAR MUNICÍPIO: ')
    municipio = str(input())
        
    sleep(2)
    
    print('O ESTADO E O MUNICÍPIO SELECIONADOS, RESPECTIVAMENTE, SÃO: {} E {}.'.format(estado, municipio))
    juntos = estado + ' ' + municipio
    #geopy(juntos)
menu()