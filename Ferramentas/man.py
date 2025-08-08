import drive2_teclado_matriz6x5
import drive_oled_display128x64
import time
introdução="este é o manual do sistema sobre qual comando esta em duvida ?"

drive_oled_display128x64.formatar_display(introdução)
time.sleep(4)
drive_oled_display128x64.display_clear()
