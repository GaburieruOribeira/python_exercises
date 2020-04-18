# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

# Make a program that asks for the size of a file to download (in MB) and the speed of an Internet link (in Mbps),
# calculate and inform the approximate time to download the file using this link (in minutes).

fileSize = input("\nHow big is the file to be downloaded(Mb)? ")
internetSpeed = input("\nWhat is the speed of your internet(Mbps)? ")
downloadTime = (float(fileSize) / float(internetSpeed)) * 60
print("\nApproximate download time: {}min".format(downloadTime))
