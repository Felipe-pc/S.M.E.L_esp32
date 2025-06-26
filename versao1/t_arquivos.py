#aquivos temporarios
import drive_oled_display128x64
import drive2_teclado_matriz6x5
diretorio=[]
def t_arquivo():
    drive_oled_display128x64.display_clear()
    while True:
        resposta=drive2_teclado_matriz6x5.teclado()
        drive_oled_display128x64.display_clear()
        drive_oled_display128x64.display(resposta,0,0)
        if resposta=='fim':
            break
        diretorio.append(resposta)
return diretorio
