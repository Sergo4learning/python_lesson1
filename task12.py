# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# x(S-x)=P --> -x^2 + S*x - P = 0 -->  x^2 - S*x + P = 0 -->  Disk= S^2-4*1*P --> x = (S+-Disk^0.5)/2 --> x1=(S+(S^2-4*P)^0.5)/2;x2=(S-(S^2-4*P)^0.5)/2

Summa=int(input("Введите сумму чисел: "))
Proisv=int(input("Введите произведение чисел: "))
if Summa**2-4*Proisv > 0 :
    first_num1=(Summa+(Summa**2-4*Proisv)**0.5)/2
    second_num1=Summa-first_num1
    first_num2=(Summa-(Summa**2-4*Proisv)**0.5)/2
    second_num2=Summa-first_num2    
    print("Загаданные числа: "+str(first_num1)+", и "+str(second_num1))
if Summa**2-4*Proisv == 0 :
    first_num1=Summa/2
    second_num1=Summa-first_num1
    print("Загаданные числа: "+str(first_num1)+", и "+str(second_num1))
if Summa**2-4*Proisv < 0 :
    print("Таких чисел не существует")
