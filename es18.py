# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

fileSize = input("\nHow big is the file to be downloaded(Mb)? ")
internetSpeed = input("\nWhat is the speed of your internet(Mbps)? ")
downloadTime = (float(fileSize) / float(internetSpeed)) * 60
print("\nApproximate download time: {}min".format(downloadTime))
