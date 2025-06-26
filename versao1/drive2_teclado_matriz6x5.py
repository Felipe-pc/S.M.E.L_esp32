from machine import Pin
def teclado(a=True):
    #pinos de envio de sinal do teclado
    Pin_envio1=Pin(13,Pin.IN,Pin.PULL_DOWN)
    Pin_envio2=Pin(12,Pin.IN,Pin.PULL_DOWN)
    Pin_envio3=Pin(14,Pin.IN,Pin.PULL_DOWN)
    Pin_envio4=Pin(27,Pin.IN,Pin.PULL_DOWN)
    Pin_envio5=Pin(26,Pin.IN,Pin.PULL_DOWN)
    Pin_envio6=Pin(25,pin.IN,Pin.PULL_DOWN)
    #pinos de entra de sinal do teclado
    Pin_entrada1=Pin(15,Pin.OUT)
    Pin_entrada2=Pin(2,Pin.OUT)
    Pin_entrada3=Pin(4,Pin.OUT)
    Pin_entrada4=Pin(5,Pin.OUT)
    Pin_entrada5=Pin(18,Pin.OUT)
    #varialveis
    operacional=True
    alfabeto=[]
    numero=[]
    inverter=False
    delei=0.2
    while operacional:
        Pin_entrada1.Value(1)
        Pin_entrada2.Value(1)
        Pin_entrada3.Value(1)
        Pin_entrada4.Value(1)
        Pin_entrada5.Value(1)
        #leituras

        #coluna 1 linha 1 a 5

        if Pin_entrada1.Value()==1 and Pin_envio1.Value()==1:
            if a==False:
                numero.append(1)
            elif inverter==True:
                alfabeto.append('1')
            else:
                alfabeto.append('a')
            time.sleep(delei)
        elif Pin_entrada2.Value()==1 and Pin_envio1.Value()==1:
            if a==False:
                numero.append(4)
            elif inverter==True:
                alfabeto.append('4')
            else:
                alfabeto.append('g')
            time.sleep(delei)
        elif Pin_entrada3.Value()==1 and Pin_envio1.Value()==1:
            if a==False:
                numero.append(7)
            elif inverter==True:
                alfabeto.append('7')
            else:
                alfabeto.append('m')
            time.sleep(delei)
        elif Pin_entrada4.Value()==1 and Pin_envio1.Value()==1:
            if inverter==True:
                alfabeto.append('<')
            else:
                alfabeto.append('s')
            time.sleep(delei)
        elif Pin_entrada5.Value()==1 and Pin_envio1.Value()==1:
            if inverter==True:
                alfabeto.append('/')
            else:
                alfabeto.append('y')
            time.sleep(delei)
        #coluna 2 linha 1 a 5

        if Pin_entrada1.Value()==1 and Pin_envio2.Value()==1:
            if a==False:
                numero.append(2)
            elif inverter==True:
                alfabeto.append('2')
            else:
                alfabeto.append('b')
            time.sleep(delei)
        elif Pin_entrada2.Value()==1 and Pin_envio2.Value()==1:
            if a==False:
                numero.append(5)
            elif inverter==True:
                alfabeto.append('5')
            else:
                alfabeto.append('h')
            time.sleep(delei)
        elif Pin_entrada3.Value()==1 and Pin_envio2.Value()==1:
            if a==False:
                numero.append(8)
            elif inverter==True:
                alfabeto.append('8')
            else:
                alfabeto.append('n')
            time.sleep(delei)
        elif Pin_entrada4.Value()==1 and Pin_envio2.Value()==1:
            if inverter=True:
                alfabeto.append('>')
            else:
                alfabeto.append('t')
            time.sleep(delei)
        elif Pin_entrada5.Value()==1 and Pin_envio2.Value()==1:
            if inverter=True:
                alfabeto.append("*")
            else:
                alfabeto.append('z')
            time.sleep(delei)

        #coluna 3 linha 1 a 5


        if Pin_entrada1.Value()==1 and Pin_envio3.Value()==1:
            if a==False:
                numero.append(3)
            elif inverter==True:
                alfabeto.append('3')
            else:
                alfabeto.append('c')
            time.sleep(delei)
        elif Pin_entrada2.Value()==1 and Pin_envio3.Value()==1:
            if a==False:
                numero.append(6)
            elif inverter==True:
                alfabeto.append('6')
            else:
                alfabeto.append('i')
            time.sleep(delei)
        elif Pin_entrada3.Value()==1 and Pin_envio3.Value()==1:
            if a==False:
                numero.append(9)
            elif inverter==True:
                alfabeto.append('9')
            else:
                alfabeto.append('o')
            time.sleep(delei)
        elif Pin_entrada4.Value()==1 and Pin_envio3.Value()==1:
            if inverter=True:
                alfabeto.append('-')
            else:
                alfabeto.append('u')
            time.sleep(delei)
        elif Pin_entrada5.Value()==1 and Pin_envio3.Value()==1:
            if inverter=True:
                alfabeto.append(' ')
            else:
                alfabeto.append(' ')
            time.sleep(delei)

        #coluna 4 linha 1 a 5

        if Pin_entrada1.Value()==1 and Pin_envio4.Value()==1:
            if a==False:
                numero.append(0)
            elif inverter==True:
                alfabeto.append('0')
            else:
                alfabeto.append('d')
            time.sleep(delei)
        elif Pin_entrada2.Value()==1 and Pin_envio4.Value()==1:
            if inverter==True:
                alfabeto.append('=')
            else:
                alfabeto.append('j')
            time.sleep(delei)
        elif Pin_entrada3.Value()==1 and Pin_envio4.Value()==1:
            if inverter==True:
                alfabeto.append('.')
            else:
                alfabeto.append('p')
            time.sleep(delei)
        elif Pin_entrada4.Value()==1 and Pin_envio4.Value()==1:
            if inverter==True:
                alfabeto.append('(')
            else:
                alfabeto.append('v')
            time.sleep(delei)
        elif Pin_entrada5.Value()==1 and Pin_envio4.Value()==1:
            operacional=False  #enter
            time.sleep(delei)

        #coluna 5 linha 1 a 5

        if Pin_entrada1.Value()==1 and Pin_envio5.Value()==1:
            if inverter==True:
                alfabeto.append('+')
            else:
                alfabeto.append('e')
            time.sleep(delei)
        elif Pin_entrada2.Value()==1 and Pin_envio5.Value()==1:
            if inverter==True:
                alfabeto.append('[')
            else:
                alfabeto.append('k')
            time.sleep(delei)
        elif Pin_entrada3.Value()==1 and Pin_envio5.Value()==1:
            if inverter==True:
                alfabeto.append('%')
            else:
                alfabeto.append('q')
            time.sleep(delei)
        elif Pin_entrada4.Value()==1 and Pin_envio5.Value()==1:
            if inverter==True:
                alfabeto.append(')')
            else:
                alfabeto.append('w')
            time.sleep(delei)
        elif Pin_entrada5.Value()==1 and Pin_envio5.Value()==1:
            tamanho=len(alfabeto)
            tamanho=tamanho-1
            alfabeto.remove(tamanho)
            time.sleep(delei)

        #coluna 6 linha 1 a 5

        if Pin_entrada1.Value()==1 and Pin_envio6.Value()==1:
            if inverter==True:
                alfabeto.append('?')
            else:
                alfabeto.append('f')
            time.sleep(delei)
        elif Pin_entrada2.Value()==1 and Pin_envio6.Value()==1:
            if inverter==True:
                alfabeto.append(']')
            else:
                alfabeto.append('l')
            time.sleep(delei)
        elif Pin_entrada3.Value()==1 and Pin_envio6.Value()==1:
            if inverter==True:
                alfabeto.append('!')
            else:
                alfabeto.append('r')
            time.sleep(delei)
        elif Pin_entrada4.Value()==1 and Pin_envio6.Value()==1:
            if inverter==True:
                alfabeto.append('~')
            else:
                alfabeto.append('x')
            time.sleep(delei)
        elif Pin_entrada5.Value()==1 and Pin_envio6.Value()==1:
            if inverter == True:
                inverter=False
            else:
                inverter=True
            time.sleep(delei)

#envio de informação
if a==False:
    return numero
else:
    return alfabeto


