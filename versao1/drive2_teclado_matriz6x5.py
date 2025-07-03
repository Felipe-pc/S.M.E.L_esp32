try:
    from machine import Pin
    import time
    def teclado(a=True):
        tecladoVirtual=False
        if tecladoVirtual==False:
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
            #varialveis
            operacional=True
            alfabeto=[]
            numero=[]
            inverter=False
            delei=0.2
            while operacional:
                Pin_entrada1.value(0)
                Pin_entrada2.value(0)
                Pin_entrada3.value(0)
                Pin_entrada4.value(0)
                Pin_entrada5.value(0)
                #leituras

                #coluna 1 linha 1 a 5
                Pin_entrada1.value(1)
                if Pin_entrada1.value()==1 and Pin_envio1.value()==1:
                    if a==False:
                        numero.append(1)
                    elif inverter==True:
                        alfabeto.append('1')
                    else:
                        alfabeto.append('a')
                    time.sleep(delei)
                    print('a')
                Pin_entrada1.value(0)
                Pin_entrada2.value(1)
                if Pin_entrada2.value()==1 and Pin_envio1.value()==1:
                    if a==False:
                        numero.append(4)
                    elif inverter==True:
                        alfabeto.append('4')
                    else:
                        alfabeto.append('g')
                    time.sleep(delei)
                    print('g')
                Pin_entrada2.value(0)
                Pin_entrada3.value(1)
                if Pin_entrada3.value()==1 and Pin_envio1.value()==1:
                    if a==False:
                        numero.append(7)
                    elif inverter==True:
                        alfabeto.append('7')
                    else:
                        alfabeto.append('m')
                    time.sleep(delei)
                    print('m')
                Pin_entrada3.value(0)
                Pin_entrada4.value(1)
                if Pin_entrada4.value()==1 and Pin_envio1.value()==1:
                    if inverter==True:
                        alfabeto.append('<')
                    else:
                        alfabeto.append('s')
                    time.sleep(delei)
                    print('s')
                Pin_entrada4.value(0)
                Pin_entrada5.value(1)
                if Pin_entrada5.value()==1 and Pin_envio1.value()==1:
                    if inverter==True:
                        alfabeto.append('/')
                    else:
                        alfabeto.append('y')
                    time.sleep(delei)
                    print('y')
                Pin_entrada5.value(0)
                Pin_entrada1.value(1)
                #coluna 2 linha 1 a 5

                if Pin_entrada1.value()==1 and Pin_envio2.value()==1:
                    if a==False:
                        numero.append(2)
                    elif inverter==True:
                        alfabeto.append('2')
                    else:
                        alfabeto.append('b')
                    time.sleep(delei)
                    print('b')
                Pin_entrada1.value(0)
                Pin_entrada2.value(1)
                if Pin_entrada2.value()==1 and Pin_envio2.value()==1:
                    if a==False:
                        numero.append(5)
                    elif inverter==True:
                        alfabeto.append('5')
                    else:
                        alfabeto.append('h')
                    time.sleep(delei)
                    print('h')
                Pin_entrada2.value(0)
                Pin_entrada3.value(1)
                if Pin_entrada3.value()==1 and Pin_envio2.value()==1:
                    if a==False:
                        numero.append(8)
                    elif inverter==True:
                        alfabeto.append('8')
                    else:
                        alfabeto.append('n')
                    time.sleep(delei)
                    print('n')
                Pin_entrada3.value(0)
                Pin_entrada4.value(1)
                if Pin_entrada4.value()==1 and Pin_envio2.value()==1:
                    if inverter==True:
                        alfabeto.append('>')
                    else:
                        alfabeto.append('t')
                    time.sleep(delei)
                    print('t')
                Pin_entrada4.value(0)
                Pin_entrada5.value(1)
                if Pin_entrada5.value()==1 and Pin_envio2.value()==1:
                    if inverter==True:
                        alfabeto.append("*")
                    else:
                        alfabeto.append('z')
                    time.sleep(delei)
                    print('z')
                Pin_entrada5.value(0)
                Pin_entrada1.value(1)

                #coluna 3 linha 1 a 5


                if Pin_entrada1.value()==1 and Pin_envio3.value()==1:
                    if a==False:
                        numero.append(3)
                    elif inverter==True:
                        alfabeto.append('3')
                    else:
                        alfabeto.append('c')
                    time.sleep(delei)
                    print('c')
                Pin_entrada1.value(0)
                Pin_entrada2.value(1)
                if Pin_entrada2.value()==1 and Pin_envio3.value()==1:
                    if a==False:
                        numero.append(6)
                    elif inverter==True:
                        alfabeto.append('6')
                    else:
                        alfabeto.append('i')
                    time.sleep(delei)
                    print('i')
                Pin_entrada2.value(0)
                Pin_entrada3.value(1)
                if Pin_entrada3.value()==1 and Pin_envio3.value()==1:
                    if a==False:
                        numero.append(9)
                    elif inverter==True:
                        alfabeto.append('9')
                    else:
                        alfabeto.append('o')
                    time.sleep(delei)
                    print('o')
                Pin_entrada3.value(0)
                Pin_entrada4.value(1)
                if Pin_entrada4.value()==1 and Pin_envio3.value()==1:
                    if inverter==True:
                        alfabeto.append('-')
                    else:
                        alfabeto.append('u')
                    time.sleep(delei)
                    print('u')
                Pin_entrada4.value(0)
                Pin_entrada5.value(1)
                if Pin_entrada5.value()==1 and Pin_envio3.value()==1:
                    if inverter==True:
                        alfabeto.append(' ')
                    else:
                        alfabeto.append(' ')
                    time.sleep(delei)
                    print(' ')
                Pin_entrada5.value(0)
                Pin_entrada1.value(1)
                #coluna 4 linha 1 a 5

                if Pin_entrada1.value()==1 and Pin_envio4.value()==1:
                    if a==False:
                        numero.append(0)
                    elif inverter==True:
                        alfabeto.append('0')
                    else:
                        alfabeto.append('d')
                    time.sleep(delei)
                    print('d')
                Pin_entrada1.value(0)
                Pin_entrada2.value(1)
                if Pin_entrada2.value()==1 and Pin_envio4.value()==1:
                    if inverter==True:
                        alfabeto.append('=')
                    else:
                        alfabeto.append('j')
                    time.sleep(delei)
                    print('j')
                Pin_entrada2.value(0)
                Pin_entrada3.value(1)
                if Pin_entrada3.value()==1 and Pin_envio4.value()==1:
                    if inverter==True:
                        alfabeto.append('.')
                    else:
                        alfabeto.append('p')
                    time.sleep(delei)
                    print('p')
                Pin_entrada3.value(0)
                Pin_entrada4.value(1)
                if Pin_entrada4.value()==1 and Pin_envio4.value()==1:
                    if inverter==True:
                        alfabeto.append('(')
                    else:
                        alfabeto.append('v')
                    time.sleep(delei)
                    print('v')
                Pin_entrada4.value(0)
                Pin_entrada5.value(1)
                if Pin_entrada5.value()==1 and Pin_envio4.value()==1:
                    operacional=False  #enter
                    time.sleep(delei)
                Pin_entrada5.value(0)
                Pin_entrada1.value(1)
                #coluna 5 linha 1 a 5

                if Pin_entrada1.value()==1 and Pin_envio5.value()==1:
                    if inverter==True:
                        alfabeto.append('+')
                    else:
                        alfabeto.append('e')
                    time.sleep(delei)
                    print('e')
                Pin_entrada1.value(0)
                Pin_entrada2.value(1)
                if Pin_entrada2.value()==1 and Pin_envio5.value()==1:
                    if inverter==True:
                        alfabeto.append('[')
                    else:
                        alfabeto.append('k')
                    time.sleep(delei)
                    print('k')
                Pin_entrada2.value(0)
                Pin_entrada3.value(1)
                if Pin_entrada3.value()==1 and Pin_envio5.value()==1:
                    if inverter==True:
                        alfabeto.append('%')
                    else:
                        alfabeto.append('q')
                    time.sleep(delei)
                    print('q')
                Pin_entrada3.value(0)
                Pin_entrada4.value(1)
                if Pin_entrada4.value()==1 and Pin_envio5.value()==1:
                    if inverter==True:
                        alfabeto.append(')')
                    else:
                        alfabeto.append('w')
                    time.sleep(delei)
                    print('w')
                Pin_entrada4.value(0)
                Pin_entrada5.value(1)
                if Pin_entrada5.value()==1 and Pin_envio5.value()==1:
                    tamanho=len(alfabeto)
                    tamanho=tamanho-1
                    alfabeto.remove(tamanho)
                    time.sleep(delei)
                Pin_entrada5.value(0)
                Pin_entrada1.value(1)

                #coluna 6 linha 1 a 5

                if Pin_entrada1.value()==1 and Pin_envio6.value()==1:
                    if inverter==True:
                        alfabeto.append('?')
                    else:
                        alfabeto.append('f')
                    time.sleep(delei)
                    print('f')
                Pin_entrada1.value(0)
                Pin_entrada2.value(1)
                if Pin_entrada2.value()==1 and Pin_envio6.value()==1:
                    if inverter==True:
                        alfabeto.append(']')
                    else:
                        alfabeto.append('l')
                    time.sleep(delei)
                    print('l')
                Pin_entrada2.value(0)
                Pin_entrada3.value(1)
                if Pin_entrada3.value()==1 and Pin_envio6.value()==1:
                    if inverter==True:
                        alfabeto.append('!')
                    else:
                        alfabeto.append('r')
                        print('r')
                    time.sleep(delei)
                Pin_entrada3.value(0)
                Pin_entrada4.value(1)
                if Pin_entrada4.value()==1 and Pin_envio6.value()==1:
                    if inverter==True:
                        alfabeto.append('~')
                    else:
                        alfabeto.append('x')
                    time.sleep(delei)
                    print('x')
                Pin_entrada4.value(0)
                Pin_entrada5.value(1)
                if Pin_entrada5.value()==1 and Pin_envio6.value()==1:
                    if inverter == True:
                        inverter=False
                    else:
                        inverter=True
                    time.sleep(delei)
                Pin_entrada5.value(0)
            #envio de informação
            if a==False:
                return numero[0]
            else:
                return alfabeto[0]
#opção tecladoVirtual
        else:
            while True:
                if a==True:
                    alfabeto=input('a ')
                    return alfabeto
                    break
                else:
                    numero=int(input("n "))
                    return numero
                    break
except:
    print("erro de drive teclado 2")
    print("verificar código")
