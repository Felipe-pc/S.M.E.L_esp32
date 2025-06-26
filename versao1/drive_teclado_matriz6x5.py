from machine import Pin
import time

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

    tempo=0.1
    enter=True
    delete=False
    troca_para_numerico=False
    end=[]
    nember=[]
    nemberFinal=[]
    while enter:
        Pin_entrada1.Value(0)
        Pin_entrada2.Value(0)
        Pin_entrada3.Value(0)
        Pin_entrada4.Value(0)
        Pin_entrada5.Value(0)
        #linha 1º do teclado
        Pin_entrada1.Value(1)
        if Pin_envio1.Value()==1 and Pin_entrada1.Value()==1:
            end.append('a')
            time.sleep(0.2)
        if Pin_envio2.Value()==1 and Pin_entrada1.Value()==1:
            end.append('b')
            time.sleep(0.2)
        if Pin_envio3.Value()==1 and Pin_entrada1.Value()==1:
            end.append('c')
            time.sleep(0.2)
        if Pin_envio4.Value()==1 and Pin_entrada1.Value()==1:
            end.append('d')
            time.sleep(0.2)
        if Pin_envio5.Value()==1 and Pin_entrada1.Value()==1:
            end.append('e')
            time.sleep(0.2)
        if Pin_envio6.Value()==1 and Pin_entrada1.Value()==1:
            end.append('f')
            time.sleep(0.2)
        Pin_entrada1.Value(0)
        time.sleep(tempo)
        #linha 2º do teclado
        Pin_entrada2.Value(1)
        if Pin_envio1.Value()==1 and Pin_entrada2.Value()==1:
            end.append('g')
            time.sleep(0.2)
        if Pin_envio2.Value()==1 and Pin_entrada2.Value()==1:
            end.append('h')
            time.sleep(0.2)
        if Pin_envio3.Value()==1 and Pin_entrada2.Value()==1:
            end.append('i')
            time.sleep(0.2)
        if Pin_envio4.Value()==1 and Pin_entrada2.Value()==1:
            end.append('t')
            time.sleep(0.2)
        if Pin_envio5.Value()==1 and Pin_entrada2.Value()==1:
            end.append('k')
            time.sleep(0.2)
        if Pin_envio6.Value()==1 and Pin_entrada2.Value()==1:
            end.append('l')
            time.sleep(0.2)
        Pin_entrada2.Value(0)
        time.sleep(tempo)
        #linha 3º do teclado
        Pin_entrada3.Value(1)
        if Pin_envio1.Value()==1 and Pin_entrada3.Value()==1:
            end.append('m')
            time.sleep(0.2)
        if Pin_envio2.Value()==1 and Pin_entrada3.Value()==1:
            end.append('n')
            time.sleep(0.2)
        if Pin_envio3.Value()==1 and Pin_entrada3.Value()==1:
            end.append('o')
            time.sleep(0.2)
        if Pin_envio4.Value()==1 and Pin_entrada3.Value()==1:
            end.append('p')
            time.sleep(0.2)
        if Pin_envio5.Value()==1 and Pin_entrada3.Value()==1:
            end.append('q')
            time.sleep(0.2)
        if Pin_envio6.Value()==1 and Pin_entrada3.Value()==1:
            end.append('r')
            time.sleep(0.2)
        Pin_entrada3.Value(0)
        time.sleep(tempo)
        #linha 4º do teclado
        Pin_entrada4.Value(1)
        if Pin_envio1.Value()==1 and Pin_entrada4.Value()==1:
            end.append('s')
            time.sleep(0.2)
        if Pin_envio2.Value()==1 and Pin_entrada4.Value()==1:
            end.append('t')
            time.sleep(0.2)
        if Pin_envio3.Value()==1 and Pin_entrada4.Value()==1:
            end.append('u')
            time.sleep(0.2)
        if Pin_envio4.Value()==1 and Pin_entrada4.Value()==1:
            end.append('v')
            time.sleep(0.2)
        if Pin_envio5.Value()==1 and Pin_entrada4.Value()==1:
            end.append('w')
            time.sleep(0.2)
        if Pin_envio6.Value()==1 and Pin_entrada4.Value()==1:
            end.append('x')
            time.sleep(0.2)
        Pin_entrada4.Value(0)
        time.sleep(tempo)
        #linha 5º do teclado
        Pin_entrada5.Value(1)
        if Pin_envio1.Value()==1 and Pin_entrada5.Value()==1:
            end.append('y')
            time.sleep(0.2)
        if Pin_envio2.Value()==1 and Pin_entrada5.Value()==1:
            end.append('z')
            time.sleep(0.2)
        if Pin_envio3.Value()==1 and Pin_entrada5.Value()==1:
            end.append(' ')
            time.sleep(0.2)
        if Pin_envio4.Value()==1 and Pin_entrada5.Value()==1:
            enter=False
            time.sleep(0.2)
        if Pin_envio5.Value()==1 and Pin_entrada5.Value()==1:
            delete=True
            time.sleep(0.2)
        if Pin_envio6.Value()==1 and Pin_entrada5.Value()==1:
            troca_para_numerico=True
            time.sleep(0.2)
        Pin_entrada5.Value(0)
        time.sleep(tempo)
        #delete
        if delete==True:
            ultimo=0
            ultimo=len(end)
            ultimo=ultimo-1
            end.remove(end[ultimo])
            time.sleep(0.2)
            delete=False
        if troca_para_numerico==True:
                while enter:
                    Pin_entrada1.Value(0)
                    Pin_entrada2.Value(0)
                    Pin_entrada3.Value(0)
                    Pin_entrada4.Value(0)
                    Pin_entrada5.Value(0)
                    #linha 1º do teclado
                    Pin_entrada1.Value(1)
                    if Pin_envio1.Value()==1 and Pin_entrada1.Value()==1:
                        end.append('1')
                        nember.append(1)
                        time.sleep(0.2)
                    if Pin_envio2.Value()==1 and Pin_entrada1.Value()==1:
                        end.append('2')
                        nember.append(2)
                        time.sleep(0.2)
                    if Pin_envio3.Value()==1 and Pin_entrada1.Value()==1:
                        end.append('3')
                        nember.append(3)
                        time.sleep(0.2)
                    if Pin_envio4.Value()==1 and Pin_entrada1.Value()==1:
                        end.append('/')
                        time.sleep(0.2)
                    if Pin_envio5.Value()==1 and Pin_entrada1.Value()==1:
                        end.append('*')
                        time.sleep(0.2)
                    if Pin_envio6.Value()==1 and Pin_entrada1.Value()==1:
                        end.append('-')
                        time.sleep(0.2)
                    Pin_entrada1.Value(0)
                    time.sleep(tempo)
                    #linha 2º do teclado
                    Pin_entrada2.Value(1)
                    if Pin_envio1.Value()==1 and Pin_entrada2.Value()==1:
                        end.append('4')
                        nember.append(4)
                        time.sleep(0.2)
                    if Pin_envio2.Value()==1 and Pin_entrada2.Value()==1:
                        end.append('5')
                        nember.append(5)
                        time.sleep(0.2)
                    if Pin_envio3.Value()==1 and Pin_entrada2.Value()==1:
                        end.append('6')
                        nember.append(6)
                        time.sleep(0.2)
                    if Pin_envio4.Value()==1 and Pin_entrada2.Value()==1:
                        end.append('+')
                        time.sleep(0.2)
                    if Pin_envio5.Value()==1 and Pin_entrada2.Value()==1:
                        end.append('=')
                        time.sleep(0.2)
                    if Pin_envio6.Value()==1 and Pin_entrada2.Value()==1:
                        end.append('.')
                        time.sleep(0.2)
                    Pin_entrada2.Value(0)
                    time.sleep(tempo)
                    #linha 3º do teclado
                    Pin_entrada3.Value(1)
                    if Pin_envio1.Value()==1 and Pin_entrada3.Value()==1:
                        end.append('7')
                        nember.append(7)
                        time.sleep(0.2)
                    if Pin_envio2.Value()==1 and Pin_entrada3.Value()==1:
                        end.append('8')
                        nember.append(8)
                        time.sleep(0.2)
                    if Pin_envio3.Value()==1 and Pin_entrada3.Value()==1:
                        end.append('9')
                        nember.append(9)
                        time.sleep(0.2)
                    if Pin_envio4.Value()==1 and Pin_entrada3.Value()==1:
                        end.append('(')
                        time.sleep(0.2)
                    if Pin_envio5.Value()==1 and Pin_entrada3.Value()==1:
                        end.append(')')
                        time.sleep(0.2)
                    if Pin_envio6.Value()==1 and Pin_entrada3.Value()==1:
                        end.append('%')
                        time.sleep(0.2)
                    Pin_entrada3.Value(0)
                    time.sleep(tempo)
                    #linha 4º do teclado
                    Pin_entrada4.Value(1)
                    if Pin_envio1.Value()==1 and Pin_entrada4.Value()==1:
                        end.append('0')
                        nember.append(0)
                        time.sleep(0.2)
                    if Pin_envio2.Value()==1 and Pin_entrada4.Value()==1:
                        end.append(',')
                        time.sleep(0.2)
                    if Pin_envio3.Value()==1 and Pin_entrada4.Value()==1:
                        end.append('!')
                        time.sleep(0.2)
                    if Pin_envio4.Value()==1 and Pin_entrada4.Value()==1:
                        end.append('?')
                        time.sleep(0.2)
                    if Pin_envio5.Value()==1 and Pin_entrada4.Value()==1:
                        end.append('#')
                        time.sleep(0.2)
                    if Pin_envio6.Value()==1 and Pin_entrada4.Value()==1:
                        end.append('@')
                        time.sleep(0.2)
                    Pin_entrada4.Value(0)
                    time.sleep(tempo)
                    #linha 5º do teclado
                    Pin_entrada5.Value(1)
                    if Pin_envio1.Value()==1 and Pin_entrada5.Value()==1:
                        end.append('<')
                        time.sleep(0.2)
                    if Pin_envio2.Value()==1 and Pin_entrada5.Value()==1:
                        end.append('>')
                        time.sleep(0.2)
                    if Pin_envio3.Value()==1 and Pin_entrada5.Value()==1:
                        end.append(' ')
                        time.sleep(0.2)
                    if Pin_envio4.Value()==1 and Pin_entrada5.Value()==1:
                        enter=False
                        time.sleep(0.2)
                    if Pin_envio5.Value()==1 and Pin_entrada5.Value()==1:
                        delete=True
                        time.sleep(0.2)
                    if Pin_envio6.Value()==1 and Pin_entrada5.Value()==1:
                        troca_para_numerico=False
                        time.sleep(0.2)
                    Pin_entrada5.Value(0)
                    time.sleep(tempo)
                    #delete
                    if delete==True:
                        ultimo=0
                        ultimoN=0
                        ultimo=len(end)
                        ultimoN=len(nember)
                        ultimo=ultimo-1
                        ultimoN=ultimoN-1
                        end.remove(end[ultimo])
                        nember.remove(nember[ultimoN])
                        time.sleep(0.2)
                        delete=False
    linha=len(end)
    junta=''
    for i in end:
        junta=junta+i
    if a==True:
        return junta
    if a==False:
        nemberFinal.append(nember)
        return nemberFinal[0]



