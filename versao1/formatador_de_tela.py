try:
    import drive_oled_display128x64
    def formatarDisplay(a):
        cont=0
        for i in a:
            tamanho=len(i)
            for emular in range(0,tamanho):
                cont=cont+1
                if cont <= 14:
                    drive_oled_display128x64.display(i[emular],0,0)
                elif cont <= 28:
                    drive_oled_display128x64.display(i[emular],16,0)
                elif cont <= 42:
                    drive_oled_display128x64.display(i[emular],26,0)
                elif cont <= 56:
                    drive_oled_display128x64.display(i[emular],36,0)
                elif cont <= 70:
                    drive_oled_display128x64.display(i[emular],46,0)
                elif cont <= 84:
                    drive_oled_display128x64.display(i[emular],56,0)
except:
    print("erro na formatação de peças")
    print("verificar código")



