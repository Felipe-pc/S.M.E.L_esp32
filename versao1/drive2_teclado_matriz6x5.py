from machine import Pin
import drive_oled_display128x64
import time
def teclado(alterar=True,intero=False):

    #pinos de envio de sinal do teclado
    Pin_envio1=Pin(13,Pin.IN,Pin.PULL_DOWN)#pino digital (coluna) 13
    Pin_envio2=Pin(12,Pin.IN,Pin.PULL_DOWN)#pino digital (coluna) 12
    Pin_envio3=Pin(14,Pin.IN,Pin.PULL_DOWN)#pino digital (coluna) 14
    Pin_envio4=Pin(27,Pin.IN,Pin.PULL_DOWN)#pino digital (coluna) 27
    Pin_envio5=Pin(26,Pin.IN,Pin.PULL_DOWN)#pino digital (coluna) 26
    Pin_envio6=Pin(25,Pin.IN,Pin.PULL_DOWN)#pino digital (coluna) 25

    #pinos de entra de sinal do teclado
    Pin_entrada1=Pin(15,Pin.OUT)#pino digital (linha) 15
    Pin_entrada2=Pin(2,Pin.OUT)#pino digital (linha) 2
    Pin_entrada3=Pin(4,Pin.OUT)#pino digital (linha) 4
    Pin_entrada4=Pin(5,Pin.OUT)#pino digital (linha) 5
    Pin_entrada5=Pin(18,Pin.OUT)#pino digital (linha) 18

    #listas
    lista_final=[]
    lista_final_numero=[]
    interos=[]
    #variaveis
    junta=''
    saidaIntero=0
    saidastream=''
    cont=0
    operacional=True
    atualizado=0
    atualiza=0
    while operacional:
        if cont == 0 or cont == 5 or cont == 10 or cont == 15 or cont == 20 or cont == 25:
            Pin_entrada1.value(1)
            Pin_entrada2.value(0)
            Pin_entrada3.value(0)
            Pin_entrada4.value(0)
            Pin_entrada5.value(0)
        elif cont == 1 or cont == 6 or cont == 11 or cont == 16 or cont == 21 or cont == 26:
            Pin_entrada1.value(0)
            Pin_entrada2.value(1)
            Pin_entrada3.value(0)
            Pin_entrada4.value(0)
            Pin_entrada5.value(0)
        if cont == 2 or cont == 7 or cont == 12 or cont == 17 or cont == 22 or cont == 27:
            Pin_entrada1.value(0)
            Pin_entrada2.value(0)
            Pin_entrada3.value(1)
            Pin_entrada4.value(0)
            Pin_entrada5.value(0)
        if cont == 3 or cont == 8 or cont == 13 or cont == 18 or cont == 23 or cont == 28:
            Pin_entrada1.value(0)
            Pin_entrada2.value(0)
            Pin_entrada3.value(0)
            Pin_entrada4.value(1)
            Pin_entrada5.value(0)
        if cont == 4 or cont == 9 or cont == 14 or cont == 19 or cont == 24 or cont == 29:
            Pin_entrada1.value(0)
            Pin_entrada2.value(0)
            Pin_entrada3.value(0)
            Pin_entrada4.value(0)
            Pin_entrada5.value(1)
        #manual
        lista_de_instrução=[
            Pin_entrada1.value()==1 and Pin_envio1.value()==1,
            Pin_entrada2.value()==1 and Pin_envio1.value()==1,
            Pin_entrada3.value()==1 and Pin_envio1.value()==1,
            Pin_entrada4.value()==1 and Pin_envio1.value()==1,
            Pin_entrada5.value()==1 and Pin_envio1.value()==1,
            Pin_entrada1.value()==1 and Pin_envio2.value()==1,
            Pin_entrada2.value()==1 and Pin_envio2.value()==1,
            Pin_entrada3.value()==1 and Pin_envio2.value()==1,
            Pin_entrada4.value()==1 and Pin_envio2.value()==1,
            Pin_entrada5.value()==1 and Pin_envio2.value()==1,
            Pin_entrada1.value()==1 and Pin_envio3.value()==1,
            Pin_entrada2.value()==1 and Pin_envio3.value()==1,
            Pin_entrada3.value()==1 and Pin_envio3.value()==1,
            Pin_entrada4.value()==1 and Pin_envio3.value()==1,
            Pin_entrada5.value()==1 and Pin_envio3.value()==1,
            Pin_entrada1.value()==1 and Pin_envio4.value()==1,
            Pin_entrada2.value()==1 and Pin_envio4.value()==1,
            Pin_entrada3.value()==1 and Pin_envio4.value()==1,
            Pin_entrada4.value()==1 and Pin_envio4.value()==1,
            Pin_entrada5.value()==1 and Pin_envio4.value()==1,
            Pin_entrada1.value()==1 and Pin_envio5.value()==1,
            Pin_entrada2.value()==1 and Pin_envio5.value()==1,
            Pin_entrada3.value()==1 and Pin_envio5.value()==1,
            Pin_entrada4.value()==1 and Pin_envio5.value()==1,
            Pin_entrada5.value()==1 and Pin_envio5.value()==1,
            Pin_entrada1.value()==1 and Pin_envio6.value()==1,
            Pin_entrada2.value()==1 and Pin_envio6.value()==1,
            Pin_entrada3.value()==1 and Pin_envio6.value()==1,
            Pin_entrada4.value()==1 and Pin_envio6.value()==1,
            Pin_entrada5.value()==1 and Pin_envio6.value()==1,]


        lista_de_alfabetica=['a','g','m','s','y','b','h','n','t','z','c','i','o','u',' ',
                            'd','j','p','v','enter','e','k','q','w','delet','f','l','r','x','troca']

        lista_de_numero=['1','4','7','<','/','2','5','8','>','*','3','6','9','-',' ',
                         '0','=','.','(','enter','+','[','%',')','delet','?',']','!','"','troca']


        if lista_de_instrução[cont]:
            time.sleep(0.1)
            if alterar==False:
                atualiza=atualiza+1
                lista_final_numero.append(lista_de_numero[cont])
                if lista_de_numero[cont]=='enter':
                    operacional=False
                    lista_final_numero.remove('enter')

                if lista_de_numero[cont]=='delet':
                    tamanhoBs1=len(lista_final_numero)
                    tamanhoBs1=tamanhoBs1-2
                    lista_final_numero.remove(lista_final_numero[tamanhoBs1])
                    lista_final_numero.remove('delet')

                if lista_de_numero[cont]=='troca':
                    alterar=True
                    lista_final_numero.remove('troca')

                if atualiza > atualizado:
                    atualizado=atualiza
                    drive_oled_display128x64.display_clear()
                    drive_oled_display128x64.formatarDisplay(lista_final_numero)

            else:
                isso=lista_de_alfabetica[cont]
                lista_final.append(isso)
                atualiza=atualiza+1
                if lista_de_alfabetica[cont]=='enter':
                    operacional=False
                    lista_final.remove('enter')

                if lista_de_alfabetica[cont]=='delet':
                    tamanhoBs=len(lista_final)
                    tamanhoBs=tamanhoBs-2
                    lista_final.remove(lista_final[tamanhoBs])
                    lista_final.remove('delet')

                if lista_de_alfabetica[cont]=='troca':
                    alterar=False
                    lista_final.remove('troca')

                if atualiza > atualizado:
                    atualizado=atualiza
                    drive_oled_display128x64.display_clear()
                    drive_oled_display128x64.formatarDisplay(lista_final)

            time.sleep(0.1)
        cont=cont+1
        if cont == 30:
            cont=0

    tamanhoFim=len(lista_final_numero)
    for i2 in range(0,tamanhoFim):
        if lista_final_numero[i2]=='0':
            interos.append(0)
        elif lista_final_numero[i2]=='1':
            interos.append(1)
        elif lista_final_numero[i2]=='2':
            interos.append(2)
        elif lista_final_numero[i2]=='3':
            interos.append(3)
        elif lista_final_numero[i2]=='4':
            interos.append(4)
        elif lista_final_numero[i2]=='5':
            interos.append(5)
        elif lista_final_numero[i2]=='6':
            interos.append(6)
        elif lista_final_numero[i2]=='7':
            interos.append(7)
        elif lista_final_numero[i2]=='8':
            interos.append(8)
        elif lista_final_numero[i2]=='9':
            interos.append(9)

    if alterar==False and intero==True:
        for i in interos:
            saidaIntero=saidaIntero+i
        return saidaIntero
    else:
        for i in lista_final:
            junta=junta+i
        for i2 in lista_final_numero:
            junta=junta+i2
        return junta





