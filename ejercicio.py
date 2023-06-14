otros_cursos_min= 2.5
otros_cursos_max=7
otros_cursos_prom= 4
curso=1.5

#Diferencias de duracion 

diferencia_min=  100 -  curso/otros_cursos_min *100
diferencia_max=  100 -  curso *1000 // otros_cursos_max /10
diferencia_prom= 100 -  curso/otros_cursos_prom *100

print("La diferencia minima es: {}%".format(diferencia_min))
print("La diferencia maxima es: {}%".format(diferencia_max))
print("La diferencia promedio es: {}%".format(diferencia_prom))

diferencia_max=  100 -  curso * 100 // otros_cursos_max 
print("La diferencia maxima es: {}%".format(diferencia_max))    