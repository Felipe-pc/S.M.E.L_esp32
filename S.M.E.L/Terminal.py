import drive_oled_display128x64
import drive2_teclado_matriz6x5
import time
import criador_de_arquivos
def terminal():
    operacional=True
    prioridade=0
    while operacional:
        #entrada
        resposta=''
        respostaVisual=''
        drive_oled_display128x64.display_clear()
        drive_oled_display128x64.display('>>> ',0,0)
        resposta=drive2_teclado_matriz6x5.teclado()
        drive_oled_display128x64.display_clear()
        respostaVisual='>>> '+resposta
        drive_oled_display128x64.display(respostaVisual,0,0)

        #parametro de comando(depuraçao)
        tamanho=len(resposta)
        if respostaVisual == 4 or resposta ==0:
            drive_oled_display128x64.display('Erro:linha esta',16,0)
            drive_oled_display128x64.display('vazia',26,0)
            time.sleep(4)


        #comando(endboot)
        if resposta=='endboot':
            operacional=False
            prioridade=0


        #criar arquivos.txt
        if resposta=='mk arquivo':
            drive_oled_display128x64.display_clear()
            criador_de_arquivos.criar_arquivo()


        #criar arquivos .py
        if resposta=='mk arquivo py':
            drive_oled_display128x64.display_clear()
            criador_de_arquivos.criar_arquivo(True)


        #mostrar arquivo .txt
        if resposta=='cat txt':
            drive_oled_display128x64.display_clear()
            criador_de_arquivos.exibir_arquivos()


        #mostrar arquivo .py
        if resposta=='cat py':
            drive_oled_display128x64.display_clear()
            criador_de_arquivos.exibir_arquivos(True)


        #execultat python
        if resposta=='python':
            drive_oled_display128x64.display_clear()
            criador_de_arquivos.execultar_python()

#encerrar
    if operacional==False and prioridade==0:
        return 'endboot'



