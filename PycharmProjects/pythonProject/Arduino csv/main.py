import serial
import re

arduino_port = input("Digite a porta serial do arduino:")                    # Porta Serial do arduino
baud = int(input("Serial begin do arduino/ velocidade de transmissão:"))   # Baud rate, é um numeor inteiro
fileName = input("nome do arquivo a ser gerado:")                         # do csv file gerado, algo o tipo "data.csv"
try:
    ser = serial.Serial(arduino_port, baud)
    print("Connected to Arduino port:" + arduino_port)
    file = open(fileName, "a")
    print("Created file")

    #printa no terminal os valores

    getData = str(ser.readline())
    getData = re.sub("\s+", ",", getData.strip())
    data = getData[0:][:-2]
    print(data)


    file = open(fileName, "a")         #adiciona os dados ao arquivo
    file.write(data + "\\n")           #escreve os dados com uma nova linha no arquivo

    #fecha arquivo
    file.close()

except:
    print("ERRO, conferir dados informados.")
