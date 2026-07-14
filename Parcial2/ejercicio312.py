def costo(x, y):
    return 2*x**2 + 3*y**2 + x*y - 40*x - 50*y + 700

def gradiente(x, y):
    df_dx = 4*x + y - 40
    df_dy = x + 6*y - 50
    return df_dx, df_dy

# El alumno ingresa el punto de partida
x = float(input("Valor inicial de x (sillas, en cientos): "))
y = float(input("Valor inicial de y (mesas, en cientos): "))
alpha = float(input("Tamaño de paso (alpha), ej. 0.1: "))
n_iteraciones = int(input("Número de iteraciones a mostrar: "))

print(f"\nInicio: x={x:.4f}, y={y:.4f}, costo={costo(x,y):.4f}\n")

for i in range(1, n_iteraciones + 1):
    df_dx, df_dy = gradiente(x, y)
    x = x - alpha * df_dx
    y = y - alpha * df_dy
    print(f"Iteración {i}: x={x:.4f}, y={y:.4f}, "
          f"grad=({df_dx:.4f}, {df_dy:.4f}), costo={costo(x,y):.4f}")

print(f"\nResultado tras {n_iteraciones} iteraciones: x={x:.4f}, y={y:.4f}, costo={costo(x,y):.4f}")
