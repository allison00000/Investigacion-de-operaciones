import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMinimize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Almacenamiento Estándar", lowBound=0, upBound=40, cat='Integer')
x2 = pulp.LpVariable("Almacenamiento Premium", lowBound=0, upBound=30, cat='Integer')

# 3. Función Objetivo
model += 20 * x1 + 60 * x2, "Costo_Total"

# 4. Restricciones
model +=  x1 + 3 * x2 >= 15, "IOSP"
model += 2 * x1 + 2 * x2 >= 14, "Disponibilidad"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Almacenamiento Estándar: {x1.varValue}")
print(f"Almacenamiento Premium: {x2.varValue}")
print(f"Costo Mensual de almacenamiento: ${pulp.value(model.objective)}")

#source .venv/bin/activate