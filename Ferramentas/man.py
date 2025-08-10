import drive2_teclado_matriz6x5
import drive_oled_display128x64
import time
introdução="este é o manual do sistema sobre qual comando esta em duvida ?"

drive_oled_display128x64.formatar_display(introdução)
time.sleep(4)
drive_oled_display128x64.display_clear()
drive_oled_display128x64.display(">>>",16,0)
resposta=drive2_teclado_matriz6x5.teclado()

#endboot
if resposta=="endboot":
    drive_oled_display128x64.formatar_display("endboot encerra o sistema")

#mk arquivo
if resposta=="mk arquivo":
    drive_oled_display128x64.formatar_display("mk arquivo cria arquivos .txt")

#mk arquivo py
if resposta=="mk arquivo":
    drive_oled_display128x64.formatar_display("mk arquivo py cria arquivo .py")

#cat txt
if resposta=="cat txt":
    drive_oled_display128x64.formatar_display("cat txt permite ler arquivos .txt")

#cat py
if resposta=="cat py":
    drive_oled_display128x64.formatar_display("cat py permite ler arquivos .py")

#python
if resposta=="python":
    drive_oled_display128x64.formatar_display("python permite execultar arquivos .py")
