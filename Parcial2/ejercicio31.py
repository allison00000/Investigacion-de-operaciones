from scipy.optimize import minimize

def costo(v):
    x, y = v
    return 2*x**2 + 3*y**2 + x*y - 40*x - 50*y + 700

iteracion = [0]

def mostrar_avance(v):
    iteracion[0] += 1
    print(f"Iteración {iteracion[0]}: x={v[0]:.4f}, y={v[1]:.4f}, costo={costo(v):.4f}")

resultado = minimize(costo, x0=[0, 0], method='CG', callback=mostrar_avance)
print("\nResultado final:", resultado.x, resultado.fun)

# Actividad en clase: Interpretar el valor de resultado.x y resultado.fun. ¿Qué representan? ¿Cuál es el costo mínimo alcanzado?
# Comprar y explicar la diferencia con los métodos de  BFGS.
# En el ejercicio 312, que pasa si pone un valor inicial de x y y muy grande, por ejemplo 1000, 1000? ¿Qué pasa con el costo? ¿Se puede mejorar el resultado?
# ¿Qué pasa si se pone un valor inicial de x y y muy pequeño, por ejemplo 0.1, 0.1? ¿Se puede mejorar el resultado?
