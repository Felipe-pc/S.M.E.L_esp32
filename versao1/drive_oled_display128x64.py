try:
    from machine import Pin,I2C#bibliotecas
    import ssd1306
    #comfiguraçao do display
    i2c=I2C(0,scl=Pin(22),sda=Pin(21))
    oled=ssd1306.SSD1306_I2C(128,64,i2c)

    #ferramenta de uso para mostrar na tela
    def display(a,y,x):
        oled.text(f'{a}',x,y)
        oled.show()


    #ferramenta de uso para limpar a tela
    def display_clear():
        oled.fill(0)
        oled.show()


    #ferramenta de uso para formatar display para texto grades automaticamente
    def formatarDisplay(a):
        cont=0
        chave1=0
        for i in a:
            tamanho=len(i)
            for emular in range(0,tamanho):
                if cont <= 120 and chave1==0:
                    display(i[emular],0,cont)
                    cont=cont+6
                    if cont ==120:
                        chave1=chave1+1
                        cont=0
                elif cont <= 120 and chave1==1:
                    display(i[emular],16,cont)
                    cont=cont+6
                    if cont ==120:
                        chave1=chave1+1
                        cont=0
                elif cont <= 120 and chave1==2:
                    display(i[emular],26,cont)
                    cont=cont+6
                    if cont ==120:
                        chave1=chave1+1
                        cont=0
                elif cont <= 120 and chave1==3:
                    display(i[emular],36,cont)
                    cont=cont+6
                    if cont == 120:
                        chave1=chave1+1
                        cont=0
                elif cont <= 120 and chave1==4:
                    display(i[emular],46,cont)
                    cont=cont+6
                    if cont == 120:
                        chave1=chave1+1
                        cont=0
                elif cont <= 120 and chave1==5:
                    display(i[emular],56,cont)
                    cont=cont+6
                    if cont == 120:
                        chave1=chave1+1
                        cont=0
except:
    print("erro do drive gráfico")
    print("verificar código")
