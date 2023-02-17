print("-----------------------------------------------------")
a = float(input("Podaj Wartość a: "))
b = float(input("Podaj Wartość b: "))
znak = input("Podaj Znak Wyrażenia: ")
print("-----------------------------------------------------")

suma = 0

if znak == '-':
    print("Wybrano Obliczenie Różnicy Kwardatu")
    suma = a**2 - 2 * a * b + b**2
    print("Różnica Wyrażenia Wynosi: " , suma)
if znak == '+':
    print("Wybrano Obliczenie Sumy Kwadratu")
    suma = a**2 + 2*a*b + b**2
    print("Suma Wyrażenia Wynosi: " , suma) 

#if znak =='({a} + {b})({a} - {b})':
#    print('Wybrano Róznce Dwóch Kwadratów')
#    suma = a**2 - b**2
#    print("Różnica Wyrażenia Wynosi: " , suma)    
    
if znak != '-' or znak != '+':
    print("Podano Zły Znak Wyrażenia")
    exit
