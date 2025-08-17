print("criando main ...")
arquivo=open("main.py",'a')
criar="""import drive_oled_display128x64
import drive2_teclado_matriz6x5
import Terminal
import time
import criador_de_arquivos
operacional=True
drive_oled_display128x64.display('iniciando...',0,0)
time.sleep(1)
drive_oled_display128x64.display('boot...',16,0)
drive_oled_display128x64.display('S.M.E.L',26,0)
time.sleep(1)
drive_oled_display128x64.display_clear()
while operacional:
    comando=Terminal.terminal()

    #comando de encerar
    if comando == 'endboot':
        operacional=False
        drive_oled_display128x64.display_clear()
        drive_oled_display128x64.display('encerando...',0,0)
        time.sleep(2)
        drive_oled_display128x64.display_clear()
"""
arquivo.write(criar)
arquivo.close()
print("main pronto.")
print("criando Terminal...")
arquivo=open("Terminal.py",'a')
criar="""import drive_oled_display128x64
import drive2_teclado_matriz6x5
import time
import criador_de_arquivos
def terminal():
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


        #comando(endboot)
        if resposta=='endboot':
            operacional=False
            prioridade=0


        #criar arquivos.txt
        if resposta=='mk arquivo':
            drive_oled_display128x64.display_clear()
            criador_de_arquivos.criar_arquivo()


        #criar arquivos .py
        if resposta=='mk arquivo py':
            drive_oled_display128x64.display_clear()
            criador_de_arquivos.criar_arquivo(True)


        #mostrar arquivo .txt
        if resposta=='cat txt':
            drive_oled_display128x64.display_clear()
            criador_de_arquivos.exibir_arquivos()


        #mostrar arquivo .py
        if resposta=='cat py':
            drive_oled_display128x64.display_clear()
            criador_de_arquivos.exibir_arquivos(True)


        #execultat python
        if resposta=='python':
            drive_oled_display128x64.display_clear()
            criador_de_arquivos.execultar_python()

#encerrar
    if operacional==False and prioridade==0:
        return 'endboot'

"""

arquivo.write(criar)
arquivo.close()
print("Terminal pronto.")
print("criando drive de grafico...")
arquivo=open("drive_oled_display128x64.py",'a')
criar="""try:
    from machine import Pin,I2C#bibliotecas
    import ssd1306
    import time
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
    def formatar_display(a):
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
                        time.sleep(8)
                        display_clear()
                        chave1=0
                        cont=0
except:
    print("erro do drive gráfico")
    print("verificar código")
"""

arquivo.write(criar)
arquivo.close()
print("drive grafico pronto.")
print("criando drive de teclado...")
arquivo=open("drive2_teclado_matriz6x5.py",'a')
criar="""from machine import Pin
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
                         '0','=','.','(','enter','+','[','%',')','delet','_',']','!','"','troca']


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
                    drive_oled_display128x64.formatar_display(lista_final_numero)

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
                    drive_oled_display128x64.formatar_display(lista_final)

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



"""
arquivo.write(criar)
arquivo.close()
print("drive de teclado pronto.")
print("criando criador e execultor de arquivos...")
arquivo=open("criador_de_arquivos.py",'a')
criar="""#criar arquivos
import drive_oled_display128x64#drive padrão
import drive2_teclado_matriz6x5#drive padrão
import time

def criar_arquivo(a=False):
    escrita=True
    if a==True:
        drive_oled_display128x64.formatar_display('nessa opcao voce esta criando arquivos .py ')
        time.sleep(6)
        drive_oled_display128x64.display_clear()
        drive_oled_display128x64.formatar_display('para comesar um nova linha pressione espaso  depois enter e fim para fechar')
        time.sleep(6)
        resposta=drive2_teclado_matriz6x5.teclado()
        resposta=resposta+'.py'
        arquivo=open(resposta,'a')
        arquivo.close()
        while escrita:
            arquivo=open(resposta,'a')
            adiciona=drive2_teclado_matriz6x5.teclado()
            if adiciona=='fim':
                break
            arquivo.write(adiciona)
            if adiciona==' ':
                arquivo.write(f"\\n")
            arquivo.close()
    else:
        drive_oled_display128x64.formatar_display('nessa opcao voce esta criando um arquivo .txt')
        time.sleep(6)
        drive_oled_display128x64.display_clear()
        drive_oled_display128x64.formatar_display('para comesar um nova linha pressione espaso depois enter e fim para fechar')
        time.sleep(6)
        resposta=drive2_teclado_matriz6x5.teclado()
        resposta=resposta+'.txt'
        arquivo=open(resposta,'a')
        arquivo.close()
        while escrita:
            arquivo=open(resposta,'a')
            adiciona=drive2_teclado_matriz6x5.teclado()
            if adiciona=='fim':
                break
            arquivo.write(adiciona)
            if adiciona==' ':
                arquivo.write(f"\\n")
            arquivo.close()



def exibir_arquivos(a=False):
    if a==True:
        resposta=drive2_teclado_matriz6x5.teclado()
        resposta=resposta+'.py'
        arquivo=open(resposta,'r')
        arquivo2=arquivo.read()
        drive_oled_display128x64.formatar_display(arquivo2)
        time.sleep(6)
        arquivo.close()

    else:
        resposta=drive2_teclado_matriz6x5.teclado()
        resposta=resposta+'.txt'
        arquivo=open(resposta,'r')
        arquivo2=arquivo.read()
        drive_oled_display128x64.formatarDisplay(arquivo2)
        time.sleep(6)
        arquivo.close()


def execultar_python():
    resposta=drive2_teclado_matriz6x5.teclado()
    arquivo=open(resposta,'r')
    execultar=arquivo.read()
    exec(execultar)
"""
arquivo.write(criar)
arquivo.close()
print("concluido.")

