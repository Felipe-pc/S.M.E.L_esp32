import drive_oled_display128x64
import drive2_teclado_matriz6x5
import time
import t_arquivos
def Terminal():
    operacional=True
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

        #criar pasta(text)
        if resposta=='mkdir':
            arq=t_arquivos.t_arquivos()
            return arq

        #comando(endboot)
        if resposta=='endboot'
            operacional=False



if operacional==False:
    return False



