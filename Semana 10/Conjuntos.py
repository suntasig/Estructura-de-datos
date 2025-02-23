# Generación de conjuntos ficticios de ciudadanos
def generar_ciudadanos(cantidad, prefijo='Ciudadano'):
    return {f"{prefijo} {i+1}" for i in range(cantidad)}

# Conjunto de 500 ciudadanos
ciudadanos = generar_ciudadanos(500)

# Conjunto de 75 ciudadanos vacunados con Pfizer
vacunados_pfizer = generar_ciudadanos(75, 'Pfizer')

# Conjunto de 75 ciudadanos vacunados con Astrazeneca
vacunados_astrazeneca = generar_ciudadanos(75, 'Astrazeneca')

# 1. Listado de ciudadanos que no se han vacunado
no_vacunados = ciudadanos - vacunados_pfizer - vacunados_astrazeneca

# 2. Listado de ciudadanos que han recibido las dos vacunas (intersección de los conjuntos)
vacunados_dos_vacunas = vacunados_pfizer & vacunados_astrazeneca

# 3. Listado de ciudadanos que solamente han recibido la vacuna de Pfizer
solo_pfizer = vacunados_pfizer - vacunados_astrazeneca

# 4. Listado de ciudadanos que solamente han recibido la vacuna de Astrazeneca
solo_astrazeneca = vacunados_astrazeneca - vacunados_pfizer

# Imprimir los resultados
print("Ciudadanos que no se han vacunado:")
print(no_vacunados)
print("\nCiudadanos que han recibido las dos vacunas:")
print(vacunados_dos_vacunas)
print("\nCiudadanos que solamente han recibido la vacuna de Pfizer:")
print(solo_pfizer)
print("\nCiudadanos que solamente han recibido la vacuna de Astrazeneca:")
print(solo_astrazeneca)
