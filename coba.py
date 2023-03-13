n=int (input("masukan angka"))
for x in range(2,n):
    if n%x == 0:
        print(f"{n} adalah bukan bilangan prima")
        break
else:
    print (f"{n} adalah bilangan prima")