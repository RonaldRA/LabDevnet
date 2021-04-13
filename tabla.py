print("Programa de prueba")
print("\t\tTABLA")

Dic={}
Dic['Andres']=(1,2)
Dic['Beatriz']=(3,4)
Dic['Carlos']=(5,6)

#formato de table
Mark = '+---------------+----------+----------+'
Row = '\n| Nombre        | Latitud  | Longitud |\n'
print(Mark+Row+Mark)
for i in Dic.keys():
    print("| {0:<13} | {1:<8.4f} | {2:<8.4f} |".format(i,Dic[i][0],Dic[i][1]))
print(Mark)
print('\nby master branch')
print('\n\n\t### Fin de Programa ###')

