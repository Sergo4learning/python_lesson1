n=input("Введике поличество монет: ")
count=0
for i in range(int(n)):
    coin_side=input("Введике какой стороной лежит "+str(i)+" монета на столе (1-орёл, 0 - решка): ")
    if coin_side=="1" :
        count=count+1     
print("для того что б все монуты лежали одной стороной надо перевернуть "+str(min(count,int(n)-count))+" монет")
    