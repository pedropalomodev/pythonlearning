n1 = float(input('Primeiro algorismo: '))
n2 = float(input('Segundo algorismo: '))
end = True
i = int(1)

while end == True:
    n1 = n1*i
    n2 = n2*i
    if n1==n2:
        print(n1,n2)
        end = False
    i += 1




