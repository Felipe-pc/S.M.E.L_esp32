try:
    import drive_oled_display128x64
    import drive2_teclado_matriz6x5
    import Terminal
    import time
    import t_arquivos
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
            drive_oled_display128x64.display('encerando...',0,0)
            time.sleep(2)
            drive_oled_display128x64.display_clear()

        #criar arquivo
        elif comando== 'mkdir':
            arquivo=t_arquivos.arquivo()
            diretorio_temporarios.append(arquivo)
        #ir para arquivo

        elif comando=='cd':
            drive_oled_display128x64.display_clear()
            drive_oled_display128x64.display('digiti o',0,0)
            drive_oled_display128x64.display('numero do',16,0)
            drive_oled_display128x64.display('arquivo',26,0)
            chamada=drive2_teclado_matriz6x5.teclado(False)
            try:
                drive_oled_display128x64.display_clear()
                drive_oled_display128x64.formatarDisplay(diretorio_temporarios[chamada])
                time.sleep(12)
            except:
                print("diretorio inesistente")
                drive_oled_display128x64.display('diretorio',0,0)
                drive_oled_display128x64.display('inesistente',16,0)
                time.sleep(3)

        #deletar arquivo
        elif comando=='rm':
            drive_oled_display128x64.display_clear()
            drive_oled_display128x64.display('digiti o',0,0)
            drive_oled_display128x64.display('numero do',16,0)
            drive_oled_display128x64.display('arquivo',26,0)
            drive_oled_display128x64.display('aser',36,0)
            drive_oled_display128x64.display('deletado',46,0)
            chamada=drive2_teclado_matriz6x5.teclado(False)
            try:
                drive_oled_display128x64.display_clear()
                diretorio_temporarios.remove(diretorio_temporarios[chamada])
                drive_oled_display128x64.display('removido',0,0)
                time.sleep(2)
            except:
                drive_oled_display128x64.display_clear()
                print("diretorio inesistente")
                drive_oled_display128x64.display('diretorio',0,0)
                drive_oled_display128x64.display('inesistente',16,0)

        #listagem de arquivos
        elif comando=='ls':
            drive_oled_display128x64.display_clear()
            tamanho=len(diretorio_temporarios)
            for pasta in range(0,tamanho):
                listagem.append(diretorio_temporarios[pasta][0])
            drive_oled_display128x64.formatarDisplay(listagem)
            listagem=[]
            time.sleep(8)

except ImportError:
    print("erro nos driver principais")
    print("imposivel execultar o sistema")


