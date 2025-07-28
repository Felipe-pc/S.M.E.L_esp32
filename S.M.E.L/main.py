
import drive_oled_display128x64
import drive2_teclado_matriz6x5
import Terminal
import time
import criador_de_arquivos
operacional=True
drive_oled_display128x64.display('iniciando...',0,0)
time.sleep(1)
drive_oled_display128x64.display('boot...',16,0)
drive_oled_display128x64.display('S.M.E.L',26,0)
time.sleep(1)
drive_oled_display128x64.display_clear()
while operacional:
    comando=Terminal.terminal()

    #comando de encerar
    if comando == 'endboot':
        operacional=False
        drive_oled_display128x64.display_clear()
        drive_oled_display128x64.display('encerando...',0,0)
        time.sleep(2)
        drive_oled_display128x64.display_clear()




