import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMinimize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Modelo 3D de personajes", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Modelo 3D de Escenarios", lowBound=0, cat='Integer')

# 3. Función Objetivo
model += 80 * x1 + 60 * x2, "Valor Total"

# 4. Restricciones
model +=  2 * x1 + x2 <= 12, "GPUP"
model += 2 * x1 + 2 * x2 <= 14, "VRAM"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Modelo 3D de personajes: {x1.varValue}")
print(f"Modelo 3D de Escenarios: {x2.varValue}")
print(f" Valor total: ${pulp.value(model.objective)}")

#source .venv/bin/activate