import drive2_teclado_matriz6x5
import drive_oled_display128x64
import time
introdução="este é o manual do sistema e estes sao os principais comandos disponiveis por padrao no sistema: cat txt , cat py , mk arquivo txt , mk arquivo py , python , endboot"

drive_oled_display128x64.formatar_display(introdução)
time.sleep(4)
