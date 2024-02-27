from sim_functions import execute, compare

#Parámetros de la simulación

n_0= 200 # Número inicial de asegurados
a_0= 100 # Capital inicial
v= 0.1 # Tasa de llegada de nuevos clientes
lamb= 23 # Tasa de reclamaciones
c= 20 # Ingresos por cliente
m= 0.1 # Tasa de retención
weib_a1= 5 # Parámetro de forma de la distribución de Weibull
weib_a2= 4
weib_a3= 3
weib_a4= 2
T= 100 # Duración de la simulación
std_threshold= 5 # Umbral de desviación estándar
labels = ['weib_a = 5', 'weib_a = 4', 'weib_a = 3', 'weib_a = 2']


#Ejecución de la simulación

execute(std_threshold, n_0, a_0, lamb, c, v, m, weib_a1, T, "Parámetro de forma de la distribución de Weibull", 5)
execute(std_threshold, n_0, a_0, lamb, c, v, m, weib_a2, T, "Parámetro de forma de la distribución de Weibull", 4)
execute(std_threshold, n_0, a_0, lamb, c, v, m, weib_a3, T, "Parámetro de forma de la distribución de Weibull", 3)
execute(std_threshold, n_0, a_0, lamb, c, v, m, weib_a4, T, "Parámetro de forma de la distribución de Weibull", 2)

#Comparar los diferentes casos prueba
compare(labels)