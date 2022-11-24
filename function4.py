def sum(number1,number2):
    toplam = number1 + number2
    return toplam

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

print("Standart toplama:",number1+number2)
print("Fonksiyonlu toplama:",sum(number1,number2))