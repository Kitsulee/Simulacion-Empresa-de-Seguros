import numpy as np
import matplotlib.pyplot as plt

comparative = []

def simulate_insurance_company(n_0, a_0, lamb, c, v, m, weib_a, T):
    t = 0
    n = n_0
    a = a_0
    a_array = [a_0]

    while t < T and a >= 0:
        # Generar reclamaciones de los asegurados existentes
        claims = np.random.normal(lamb, scale=1.0, size=n)
        claim_costs = np.random.gamma(weib_a, scale=1.0, size=n)

        # Calcular los ingresos y gastos de la compañía
        income = n * c
        expenses = np.sum(claims * claim_costs)

        # Generar nuevos clientes
        new_customers = np.random.poisson(v)

        # Calcular la tasa de retención de los asegurados existentes
        retention_rates = np.random.uniform(0, m, size=n)
        retention = np.sum(retention_rates < 1)

        # Actualizar el número de asegurados y el capital de la compañía
        n = retention + new_customers
        a += income - expenses
        a_array.append(a)

        # Incrementar el tiempo
        t += 1

    return t, a_array

def estimate_bankruptcy_time(std_threshold, n_0, a_0, lamb, c, v, m, weib_a, T):
    results = []
    iter_count = 0
    amount_array = []

    while len(results) < 30 or np.std(results) > std_threshold:
        bankruptcy_time, amounts = simulate_insurance_company(n_0, a_0, lamb, c, v, m, weib_a, T)
        results.append(bankruptcy_time)
        amount_array.append(amounts)
        iter_count += 1

    mean = np.mean(results)
    std = np.std(results)

    return mean, std, iter_count, amount_array

def plot_ex_dis(variable, value, amounts):
    for i in range(len(amounts)):
        plt.plot(amounts[i])
    plt.xlabel('Time')
    plt.ylabel('Capital')
    plt.title(f'Grafico para {variable} = {value}')
    plt.show()

def execute_dis(std_threshold, n_0, a_0, lamb, c, v, m, weib_a, T, varible_name, variable_value):
    
    mean, std, iter_count,amounts= estimate_bankruptcy_time(std_threshold, n_0, a_0, lamb, c, v, m, weib_a, T)

    #Graficar el capital de la compañía en cada iteración
    plot_ex_dis(varible_name, variable_value, amounts)
    
    grafic=[]

    maxlen=np.max([len(x) for x in amounts])

    for i in range(maxlen):
        temp=[]
        for j in range(len(amounts)):
            if i<len(amounts[j]):
                temp.append(amounts[j][i])
        grafic.append(np.mean(temp))

    comparative.append(grafic)

    print("Mean: ", mean)
    print("Standard deviation: ", std)
    print("Iterations: ", iter_count)

def compare_dis():
    for i in range(len(comparative)):
        plt.plot(comparative[i])
    plt.xlabel('Time')
    plt.ylabel('Capital')
    plt.title('Comparación de los diferentes casos prueba')
    plt.show()
