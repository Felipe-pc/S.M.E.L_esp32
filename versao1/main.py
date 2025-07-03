try:
    import drive_oled_display128x64
    import drive2_teclado_matriz6x5
    import Terminal
    import time
    import t_arquivos
    import formatador_de_tela
    operacional=True
    drive_oled_display128x64.display('iniciando...',0,0)
    time.sleep(1)
    drive_oled_display128x64.display('boot...',16,0)
    drive_oled_display128x64.display('V1 LTS',26,0)
    time.sleep(1)
    drive_oled_display128x64.display_clear()
    diretorio_temporarios=[]
    while operacional:
        comando=Terminal.terminal()
        #comando de encerar
        if comando == 'endboot':
            operacional=False
            drive_oled_display128x64.display_clear()
        #criar arquivo
        elif comando== 'mkdir':
            arquivo=t_arquivos.arquivo()
            diretorio_temporarios.append(arquivo)
        #ir para arquivo
        elif comando=='cd':
            drive_oled_display128x64.display('digiti o',0,0)
            drive_oled_display128x64.display('numero do',16,0)
            drive_oled_display128x64.display('arquivo',26,0)
            chamada=drive2_teclado_matriz6x5.teclado()
            try:
                drive_oled_display128x64.display_clear()
                formatdor_de_tela.formatarDisplay(diretorio_temporarios[chamada])
            except:
                print("diretorio inesistente")
                drive_oled_display128x64.display('diretorio',0,0)
                drive_oled_display128x64.display('inesistente',16,0)
        #deletar arquivo
        elif comando=='rm':
            drive_oled_display128x64.display('digiti o',0,0)
            drive_oled_display128x64.display('numero do',16,0)
            drive_oled_display128x64.display('arquivo',26,0)
            drive_oled_display128x64.display('aser',36,0)
            drive_oled_display128x64.display('deletado',46,0)
            chamada=drive2_teclado_matriz6x5.teclado()
            try:
                drive_oled_display128x64.display_clear()
                diretorio_temporarios.remove(diretorio_temporarios[chamada])
            except:
                drive_oled_display128x64.display_clear()
                print("diretorio inesistente")
                drive_oled_display128x64.display('diretorio',0,0)
                drive_oled_display128x64.display('inesistente',16,0)

except ImportError:
    print("erro nos driver principais")
    print("imposivel execultar o sistema")


