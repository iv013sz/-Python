pages=100
stroke=50
symb=25
memory=symb*stroke*pages*4/1024/1024
disc=1.44
numbooks=disc//memory
print("Количество книг, помещающихся на дискету:", int(numbooks))
