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
    print('\033[1;37m-=\033[0m' * 28 )

    print('\033[1;32mADICIONAR ESTADO\033[0m: ')
    estado = str(input()).strip().upper()

    print('\033[1;32mADICIONAR MUNICÍPIO\033[0m: ')
    municipio = str(input()).strip().upper()
        
    sleep(1)
    
    print('O "ESTADO" E O "MUNICÍPIO" SELECIONADOS, RESPECTIVAMENTE, SÃO: \033[1;33m{}\033[0m E \033[1;33m{}\033[0m.'.format(estado, municipio))
    juntos = estado + ' ' + municipio
    #geopy(juntos)
menu()
