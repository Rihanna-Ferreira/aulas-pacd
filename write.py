with open ('texto.txt' , 'w') as souza:
    souza.write("ola mundo!?\n")
    listas = ['Python' , 'é' , 'legal!']
    souza.writelines(listas)