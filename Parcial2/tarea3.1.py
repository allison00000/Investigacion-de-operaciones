from scipy.optimize import minimize

# Función de utilidad (a maximizar)
def utilidad(x, y):
    return -x**2 - y**2 - x*y + 65*x + 75*y - 500

# scipy solo minimiza, así que minimizamos el negativo de la utilidad
def utilidad_negativa(v):
    x, y = v
    return -utilidad(x, y)

limites = [(0, None), (0, None)]  # x >= 0, y >= 0
iteracion = [0]

def mostrar_avance(v):
    iteracion[0] += 1
    x, y = v
    print(f"Iteración {iteracion[0]}: x={x:.4f}, y={y:.4f}, utilidad={utilidad(x,y):.4f}")

resultado = minimize(utilidad_negativa, x0=[0, 0], method='SLSQP',
                      callback=mostrar_avance, bounds=limites)

x_opt, y_opt = resultado.x
utilidad_opt = -resultado.fun

print(f"\nBotellas chicas óptimas: {x_opt:.2f} (miles/día)")
print(f"Botellas grandes óptimas: {y_opt:.2f} (miles/día)")
print(f"Utilidad máxima: ${utilidad_opt:,.2f}")
