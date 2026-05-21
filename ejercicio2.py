import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("PC", lowBound=0, upBound=60, cat='Integer')
x2 = pulp.LpVariable("Lap", lowBound=0, upBound=60, cat='Integer')

# 3. Función Objetivo
model += 2000 * x1 + 4000 * x2, "Costo_Total"

# 4. Restricciones
model +=   x1 +  x2 <= 60, "microprocesadores"
model +=  x1 + 3 * x2 <=100, "horas"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"PC: {x1.varValue}")
print(f"Lap: {x2.varValue}")
print(f"Costo Maximo : ${pulp.value(model.objective)}")

#source .venv/bin/activate