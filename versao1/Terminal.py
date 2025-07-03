try:
    import drive_oled_display128x64
    import drive2_teclado_matriz6x5
    import time
    import t_arquivos
    def Terminal():
        operacional=True
        prioridade=0
        while operacional:
            #entrada
            resposta=''
            respostaVisual=''
            drive_oled_display128x64.display_clear()
            drive_oled_display128x64.display('>>> ',0,0)
            resposta=drive2_teclado_matriz6x5.teclado()
            drive_oled_display128x64.display_clear()
            respostaVisual='>>> '+resposta
            drive_oled_display128x64.display(respostaVisual,0,0)

            #parametro de comando(depuraçao)
            tamanho=len(resposta)
            if respostaVisual == 4 or resposta ==0:
                drive_oled_display128x64.display('Erro:linha esta',16,0)
                drive_oled_display128x64.display('vazia',26,0)
                time.sleep(4)

            #criar pasta(text)
            if resposta=='mkdir':
                operacional=False
                prioridade=1

            #comando(endboot)
            if resposta=='endboot':
                operacional=False
                prioridade=0

            #pesquisa diretorio
            if resposta=='cd':
                operacional=False
                prioridade=2

            #deletar o diretorio
            if resposta=='rm':
                operacional=False
                prioridade=3

    #criar arquivos
        if operacional==False and prioridade==1:
            return 'mkdir'

    #encerrar
        elif operacional==False and prioridade==0:
            return 'endboot'

    #procurar arquivos
        elif operacional==False and prioridade==2:
            return 'cd'

    #deletar o diretorio
        elif operacional==False and prioridade==3:
            return 'rm'

except:
    print("terminal esta com erro")
    print("verificar código")

