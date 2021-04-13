a=10
for i in range(a):
    print(i, end=' ')
print('\n')

lista=[i for i in range(5)]
if [3,4] in lista:
    print('Mis numeros')
else:
    print('No se ubica')

Dic={}
Dic[1]='uno'
Dic[2]='dos'

print(Dic)

#formato de table
Mark = '+---------------+----------+----------+'
Row = '\n| Ciudad        | Latitud  | Longitud |\n'
print(Mark+Row+Mark)
for i in DB.keys():
    print("| {0:<13} | {1:<8.4f} | {2:<8.4f} |".format(i,DB[i][0],DB[i][1]))
print(Mark,'\n\n\n')

print('programa modificado Devent branch')

