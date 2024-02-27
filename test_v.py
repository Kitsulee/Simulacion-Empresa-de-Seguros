from sim_functions import execute, compare

#Parámetros de la simulación

n_0= 200 # Número inicial de asegurados
a_0= 100 # Capital inicial
v1= 0.1 # Tasa de llegada de nuevos clientes
v2= 1 
v3= 2
v4= 3
lamb= 23 # Tasa de reclamaciones
c= 20 # Ingresos por cliente
m= 0.1 # Tasa de retención
weib_a= 5 # Parámetro de forma de la distribución de Weibull
T= 100 # Duración de la simulación
std_threshold= 5 # Umbral de desviación estándar

execute(std_threshold, n_0, a_0, lamb, c, v1, m, weib_a, T, "Tasa de llegada de nuevos clientes", 0.1)
execute(std_threshold, n_0, a_0, lamb, c, v2, m, weib_a, T, "Tasa de llegada de nuevos clientes", 1)
execute(std_threshold, n_0, a_0, lamb, c, v3, m, weib_a, T, "Tasa de llegada de nuevos clientes", 2)
execute(std_threshold, n_0, a_0, lamb, c, v4, m, weib_a, T, "Tasa de llegada de nuevos clientes", 3)

#Comparar los diferentes casos prueba
compare()