try:
    from machine import Pin,I2C#bibliotecas
    import ssd1306
    #comfiguraçao do display
    i2c=I2C(0,scl=Pin(22),sda=Pin(21))
    oled=ssd1306.SSD1306_I2C(128,64,i2c)

    #ferramenta de uso para mostrar na tela
    def display(a,b,c):
        oled.text(f'{a}',c,b)
        oled.show()


    #ferramenta de uso para limpar a tela
    def display_clear():
        oled.fill(0)
        oled.show()

except:
    print("erro do drive gráfico")
    print("verificar código")
