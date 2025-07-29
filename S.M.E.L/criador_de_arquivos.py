#criar arquivos
import drive_oled_display128x64#drive padrão
import drive2_teclado_matriz6x5#drive padrão
import time

def criar_arquivo(a=False):
    escrita=True
    if a==True:
        drive_oled_display128x64.formatar_display('nessa opcao voce esta criando arquivos .py ')
        time.sleep(6)
        drive_oled_display128x64.display_clear()
        drive_oled_display128x64.formatar_display('para comesar um nova linha pressione espaso  depois enter e fim para fechar')
        time.sleep(6)
        resposta=drive2_teclado_matriz6x5.teclado()
        resposta=resposta+'.py'
        arquivo=open(resposta,'a')
        arquivo.close()
        while escrita:
            arquivo=open(resposta,'a')
            adiciona=drive2_teclado_matriz6x5.teclado()
            if adiciona=='fim':
                break
            arquivo.write(adiciona)
            if adiciona==' ':
                arquivo.write(f"\n")
            arquivo.close()
    else:
        drive_oled_display128x64.formatar_display('nessa opcao voce esta criando um arquivo .txt')
        time.sleep(6)
        drive_oled_display128x64.display_clear()
        drive_oled_display128x64.formatar_display('para comesar um nova linha pressione espaso depois enter e fim para fechar')
        time.sleep(6)
        resposta=drive2_teclado_matriz6x5.teclado()
        resposta=resposta+'.txt'
        arquivo=open(resposta,'a')
        arquivo.close()
        while escrita:
            arquivo=open(resposta,'a')
            adiciona=drive2_teclado_matriz6x5.teclado()
            if adiciona=='fim':
                break
            arquivo.write(adiciona)
            if adiciona==' ':
                arquivo.write(f"\n")
            arquivo.close()



def exibir_arquivos(a=False):
    if a==True:
        resposta=drive2_teclado_matriz6x5.teclado()
        resposta=resposta+'.py'
        arquivo=open(resposta,'r')
        arquivo2=arquivo.read()
        drive_oled_display128x64.formatar_display(arquivo2)
        time.sleep(6)
        arquivo.close()

    else:
        resposta=drive2_teclado_matriz6x5.teclado()
        resposta=resposta+'.txt'
        arquivo=open(resposta,'r')
        arquivo2=arquivo.read()
        drive_oled_display128x64.formatarDisplay(arquivo2)
        time.sleep(6)
        arquivo.close()


def execultar_python():
    resposta=drive2_teclado_matriz6x5.teclado()
    arquivo=open(resposta,'r')
    execultar=arquivo.read()
    exec(execultar)
