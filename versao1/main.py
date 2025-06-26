try:
    import drive_oled_display128x64
    import drive2_teclado_matriz6x5
    import Terminal
    import time
    import t_arquivos
    operacional=True
    drive_oled_display128x64.display('iniciando…'0,0)
    time.sleep(1)
    drive_oled_display128x64.display('boot…'16,0)
    drive_oled_display128x64.display('V1.0.0'26,0)
    time.sleep(1)
    drive_oled_display128x64.display_clear()
    diretorio_temporarios=[]
    while operacional:
        arq=Terminal.terminal()
        endboot=Terminal.terminal()
        if endboot == False:
            operacional=False
            drive_oled_display128x64.display_clear()
        diretorio_temporarios.append(arq)
except ImportError:
    print("erro nos driver principais")
    print("imposivel execultar o sistema")


