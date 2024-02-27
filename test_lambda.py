from sim_functions import execute, compare
from extra_distribution_functions import execute_dis, compare_dis

#Parámetros de la simulación

n_0= 200 # Número inicial de asegurados
a_0= 100 # Capital inicial
v= 0.1 # Tasa de llegada de nuevos clientes
lamb1 = 25 # Tasa de reclamaciones
lamb2 = 23
lamb3 = 22
lamb4 = 20
c= 20 # Ingresos por cliente
m= 0.1 # Tasa de retención
weib_a= 5 # Parámetro de forma de la distribución de Weibull
T= 100 # Duración de la simulación
std_threshold= 5 # Umbral de desviación estándar
labels = ['lamb = 25', 'lamb = 23', 'lamb = 22', 'lamb = 20']

#Ejecución de la simulación

execute(std_threshold, n_0, a_0, lamb1, c, v, m, weib_a, T, "Lambda", 25)
execute(std_threshold, n_0, a_0, lamb2, c, v, m, weib_a, T, "Lambda", 23)
execute(std_threshold, n_0, a_0, lamb3, c, v, m, weib_a, T, "Lambda", 22)
execute(std_threshold, n_0, a_0, lamb4, c, v, m, weib_a, T, "Lambda", 20)

#Comparar los diferentes casos prueba
compare(labels)

execute_dis(std_threshold, n_0, a_0, lamb1, c, v, m, weib_a, T, "Lambda", 25)
execute_dis(std_threshold, n_0, a_0, lamb2, c, v, m, weib_a, T, "Lambda", 23)
execute_dis(std_threshold, n_0, a_0, lamb3, c, v, m, weib_a, T, "Lambda", 22)
execute_dis(std_threshold, n_0, a_0, lamb4, c, v, m, weib_a, T, "Lambda", 20)

compare_dis()

