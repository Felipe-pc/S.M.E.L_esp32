try:
    #aquivos temporarios
    import drive_oled_display128x64#drive padrão
    import drive2_teclado_matriz6x5#drive padrão
    import time
    def arquivo():

        diretorio0=[]
        drive_oled_display128x64.display_clear()
        drive_oled_display128x64.display('nome do arq',0,0)
        resposta0=drive2_teclado_matriz6x5.teclado()
        diretorio0.append(resposta0)
        while True:
            drive_oled_display128x64.display_clear()
            resposta=drive2_teclado_matriz6x5.teclado()
            drive_oled_display128x64.display(resposta,0,0)
            time.sleep(2)
            if resposta=='fim':
                break
            diretorio0.append(resposta)
    return diretorio0
except:
    print("erro do criador de arquivo temporarios")
    print("verificar código")
