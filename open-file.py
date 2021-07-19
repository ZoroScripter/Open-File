import os
import time

#\033[1;30m Branco
#\033[1;31m Vermelho
#\033[1;32m Verde
#\033[1;33m Amarelo
#\033[1;34m Azul
#\033[1;35m Roxo
#\033[1;36m Ciano
#\033[1;37m Cinza Claro

os.system("clear")
print("\033[1;34m")
os.system("figlet Open File")
#Opções!
print("""\033[1;31m
//======================\

[1] Somar               l
[2] Multiplicar         l
[3] Install openssh     l
[4] Install update      l
[5] Install upgrade     l
[6] Install git         l
[7] Install python      l
[8] Install python2     l
[9] Install python3     l
[10] Install php        l
[11] Install nano       l
[12] Creditos           l
[13] Sair               l
//======================\
""")
op = input("Digite a opção: ")


if op == "1":
    os.system("clear")
    n1 = int(input("Digite o premeiro numero: "))
    n2 = int(input("Segundo numero: "))
    res = n1+n2
    os.system("clear")
    print("Gerando resultados...")
    time.sleep(3)
    print("O resultado entre {}+{} = {}".format(n1, n2, res))
    time.sleep(7)
    os.system("python3 open-file.py")
elif op == "2":
    os.system("clear")
    n1 = int(input("Digite o premeiro numero: "))
    n2 = int(input("Segundo numero: "))
    res = n1*n2
    os.system("clear")
    print("Gerando resultados...")
    time.sleep(3)
    print("O resultado entre {}+{} = {}".format(n1, n2, res))
    time.sleep(7)
    os.system("python3 open-file.py")
elif op == "3":
    os.system("clear")
    os.system("pkg install ssh")
    os.system("python3 open-file.py")
elif op == "4":
    os.system("clear")
    os.system("pkg update")
    os.system("python3 open-file.py")
elif op == "5":
    os.system("clear")
    os.system("pkg upgrade")
    os.system("python3 opem-file.py")
elif op == "6":
    os.system("clear")
    os.system("pkg install git")
    os.system("python3 opem-file.py")
elif op == "7":
    os.system("clear")
    os.system("pkg install python")
    os.system("python3 opem-file.py")
elif op == "8":
    os.system("clear")
    os.system("pkg install python2")
    os.system("python3 opem-file.py")
elif op == "9":
    os.system("clear")
    os.system("pkg install python3")
    os.system("python3 opem-file.py")
elif op == "10":
    os.system("clear")
    os.system("pkg install php")
    os.system("python3 opem-file.py")
elif op == "11":
    os.system("clear")
    os.system("pkg install nano")
    os.system("python3 opem-file.py")
elif op == "12":
    os.system("clear")
    time.sleep(0.35)
    print("=×=×=×=×=×=×=×=×=×=×=")
    time.sleep(0.35)
    print("\033[1;35m Creador:")
    time.sleep(0.35)
    print("ZoroScipter!")
    time.sleep(0.35)
    print("Apoiadores:")
    time.sleep(0.35)
    print("Columbiaxxxs")
    time.sleep(0.35)
    print("W4li")
    time.sleep(5)
    os.system("python3 open-file.py")
elif op == "13":
    os.system("clear")
    print("Saindo!....")
    time.sleep(4)
    exit()
else:
    os.system("python3 open-file.py")