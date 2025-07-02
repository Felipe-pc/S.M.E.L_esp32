try:
    import drive_oled_display128x64
    def formatarDisplay(a):
        cont=0
        chave1=0
        for i in a:
            tamanho=len(i)
            for emular in range(0,tamanho):
                if cont <= 84 and chave1==0:
                    drive_oled_display128x64.display(i[emular],0,cont)
                    cont=cont+6
                    if cont ==84:
                        chave1=chave1+1
                        cont=0
                elif cont <= 168 and chave1==1:
                    drive_oled_display128x64.display(i[emular],16,cont)
                    cont=cont+6
                    if cont ==162:
                        chave1=chave1+1
                        cont=0
                elif cont <= 252 and chave1==2:
                    drive_oled_display128x64.display(i[emular],26,cont)
                    cont=cont+6
                    if cont ==252:
                        chave1=chave1+1
                        cont=0
                elif cont <= 336 and chave1==3:
                    drive_oled_display128x64.display(i[emular],36,cont)
                    cont=cont+6
                    if cont ==336:
                        chave1=chave1+1
                        cont=0
                elif cont <= 420 and chave1==4:
                    drive_oled_display128x64.display(i[emular],46,cont)
                    cont=cont+6
                    if cont ==420:
                        chave1=chave1+1
                        cont=0
                elif cont <= 504 and chave1==5:
                    drive_oled_display128x64.display(i[emular],56,cont)
                    cont=cont+6
                    if cont ==504:
                        chave1=chave1+1
                        cont=0
except:
    print("erro na formatação de peças")
    print("verificar código")



