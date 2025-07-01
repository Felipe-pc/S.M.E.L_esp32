try:
    #aquivos temporarios
    import drive_oled_display128x64#drive padrão
    import drive2_teclado_matriz6x5#drive padrão
    def t_arquivo():
        diretorio=dict()
        diretorio0=[]
        drive_oled_display128x64.display_clear()
        drive_oled_display128x64.display('nome do arq',0,0)
        resposta0=drive2_teclado_matriz6x5.teclado()
        while True:
            drive_oled_display128x64.display_clear()
            resposta=drive2_teclado_matriz6x5.teclado()
            drive_oled_display128x64.display(resposta,0,0)
            if resposta=='fim':
                diretorio={resposta0:diretorio0[:]}
                break
            diretorio0.append(resposta)
    return diretorio
except:
    print("erro do criador de arquivo temporarios")
    print("verificar código")
