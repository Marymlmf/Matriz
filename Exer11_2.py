mat = []
for i in range(5):
    mat.append( [0] * 3 )
#Entrada dos dados
for i in range(3):
    for j in range(3):
        mat[i][j] = int(input("Entre com o valor de mat[%d],[%d]: "%(i,j)))
#Mostra a matriz        
for i in range(3):
    for j in range(3):
        print("%5d|"%mat[i][j], end = '')       
    print("\n")
#Soma de cada linha
for i in range(3):
    soma = 0
    for j in range(3):
        soma = soma + mat[i][j]      
    print("A soma da linha %d = %d"%(i,soma))
#Soma de cada coluna
for j in range(3):
    soma = 0
    for i in range(3):
        soma = soma + mat[i][j]      
    print("A soma da coluna %d = %d"%(j,soma))

#Soma da segunda linha
soma = 0
for i in range(3):
    soma = soma + mat[i][j]      
print("A soma da segunda linha = %d"%soma)

#Soma da terceira coluna
soma = 0
for j in range(3):
    soma = soma + mat[i][j]      
print("A soma da terceira coluna = %d"%soma)

#Soma de diagonal principal
soma = 0
for i in range(3):
    for j in range(3):
        if i == j:
            soma = soma + mat[i][j]      
print("A soma da diagonal principal = %d"%soma)

#Soma diagonal secundaria
soma = 0
for i in range(0,3,1):
    for j in range(0,3,1):
        if (i+j == 2):
            soma = soma + mat[i][j]
print("A soma da diagonal secundaria = %d"%soma)

#Soma todos
soma = 0;
for i in range(0,3,1):
    for j in range(0,3,1):
        soma = soma + mat[i][j]
print("A soma total = %d"%soma)