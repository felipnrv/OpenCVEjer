otros_cursos_min= 2.5
otros_cursos_max=7
otros_cursos_prom= 4
curso=1.5

#Diferencias de duracion 

diferencia_min=  100 -  curso/otros_cursos_min *100
diferencia_max=  100 -  curso/ otros_cursos_max *100
diferencia_prom= 100 -  curso/otros_cursos_prom *100
x = otros_cursos_prom/curso * 10

print("La diferencia minima es: {}%".format(diferencia_min))
print("La diferencia maxima es: {:.2f}%".format(diferencia_max))
print("La diferencia promedio es: {}%".format(diferencia_prom))
#100 -  curso *1000 // otros_cursos_max /10
print(x)



