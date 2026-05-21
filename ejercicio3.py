import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Inspeccion basica", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Inspeccion profunda", lowBound=0, cat='Integer')

# 3. Función Objetivo
model += 2 * x1 + 5 * x2, "seguridad total"

# 4. Restricciones
model +=   x1 + 3 * x2 <= 18, "firewall"
model +=  x1 +  x2 <=8, "RAM"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"PC: {x1.varValue}")
print(f"Lap: {x2.varValue}")
print(f"Seguridad Maxima : ${pulp.value(model.objective)}")

#source .venv/bin/activate