import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("servicios_web", pulp.LpMaximize)

# 2. Variables de decisión (enteras)
x1 = pulp.LpVariable("servidor_basico", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("servidor_avanzado", lowBound=0, cat='Integer')

# 3. Función Objetivo
model += 30 * x1 + 50 * x2, "Valor_Total"

# 4. Restricciones

# RAM
model +=  x1 + 2 * x2 <= 16, "RAM"

# vCPU
model += 3 * x1 + 2 * x2 <= 24, "vCPU"

# 5. Resolver
model.solve()

# 6. Mostrar resultados
print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"servidor_basico: {x1.varValue}")
print(f"servidor_avanzado: {x2.varValue}")
print(f"Valor Total: ${pulp.value(model.objective)}")