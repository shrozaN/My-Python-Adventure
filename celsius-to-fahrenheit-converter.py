celsius = int(input())

def conv(c):
    converte = (celsius * 9 ) / 5 + 32 #Calculating..
    return converte

fahrenheit = conv(celsius)
print(fahrenheit)
