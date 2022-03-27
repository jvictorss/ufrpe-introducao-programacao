"""Write a Python program to convert temperatures to and from celsius,
fahrenheit. [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and
f = temperature in fahrenheit ] Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius"""

tipoConversao = input("Insira que conversão quer fazer: Se Celsius para Fahrenheit digite F, caso contrário, C: ")

if tipoConversao == "F":
    celsius = int(input("Insira os graus Celsius, apenas em número: "))
    fahrenheit = (9 * celsius + (32*5)) / 5
    print(f"{celsius} graus Celsius dá {fahrenheit} graus Fahrenheit.")
elif tipoConversao == "C":
    fahrenheit = int(input("Insira os graus Fahrenheit, apenas em número: "))
    celsius = (5 * (fahrenheit - 32)) / 9
    print(f"{fahrenheit} graus Fahrenheit dá {celsius} graus Celsius.")