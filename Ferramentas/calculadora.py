try:
    import drive_oled_display128x64
    import drive2_teclado_matriz6x5
    import time



        #variaveis
    memoriaent=[]
    soma=0
    subitracao=0
    multiplicacao=0
    divisao=0
    #laumcher
    drive_oled_display128x64.display_clear()
    drive_oled_display128x64.display('indique a operador',0,0)
    drive_oled_display128x64.display(' + | - | * | /',16,0)
    resposta=drive2_teclado_matriz6x5.teclado()
    #soma

    drive_oled_display128x64.display_clear()
    drive_oled_display128x64.display('digiti um',0,0)
    drive_oled_display128x64.display('numero',16,0)
    drive_oled_display128x64.display('>>>',26,0)
    resposta1=drive2_teclado_matriz6x5.teclado(False,True)
    drive_oled_display128x64.display_clear()
    drive_oled_display128x64.display('digiti outro',0,0)
    drive_oled_display128x64.display('numero',16,0)
    drive_oled_display128x64.display(f'>>> {resposta1}',26,0)
    drive_oled_display128x64.display('>>>',36,0)
    resposta2=drive2_teclado_matriz6x5.teclado(False,True)
    drive_oled_display128x64.display_clear()
    if resposta=='+':
        soma=resposta1+resposta2
        drive_oled_display128x64.display(f'{soma}',16,0)
        time.sleep(5)
    elif resposta=='-':
        soma=resposta1-resposta2
        drive_oled_display128x64.display(f'{soma}',16,0)
        time.sleep(5)
    elif resposta=='*':
        soma=resposta1*resposta2
        drive_oled_display128x64.display(f'{soma}',16,0)
        time.sleep(5)
    elif resposta=='/':
        soma=resposta1/resposta2
        drive_oled_display128x64.display(f'{soma}',16,0)
        time.sleep(5)

except:
    print("erro na calculadora")
    print("verificar código")









