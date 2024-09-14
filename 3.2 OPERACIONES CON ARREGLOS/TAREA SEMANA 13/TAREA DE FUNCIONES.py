# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)

temperaturas = [
    [  # Ciudad 1
        [  # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 50},
            {"day": "Miércoles", "temp": 42},
            {"day": "Jueves", "temp": 57},
            {"day": "Viernes", "temp": 50},
            {"day": "Sábado", "temp": 68},
            {"day": "Domingo", "temp": 52}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 87},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 62},
            {"day": "Jueves", "temp": 69},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 96},
            {"day": "Domingo", "temp": 82}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 54},
            {"day": "Jueves", "temp": 48},
            {"day": "Viernes", "temp": 81},
            {"day": "Sábado", "temp": 39},
            {"day": "Domingo", "temp": 70}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 49},
            {"day": "Martes", "temp": 38},
            {"day": "Miércoles", "temp": 50},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 42},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 51}
        ]
    ],
    [  # Ciudad 2
        [  # Semana 1
            {"day": "Lunes", "temp": 42},
            {"day": "Martes", "temp": 49},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 65},
            {"day": "Domingo", "temp": 45}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 108},
            {"day": "Martes", "temp": 96},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 41},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 91}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 41},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 52},
            {"day": "Sábado", "temp": 66},
            {"day": "Domingo", "temp": 60}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 44},
            {"day": "Martes", "temp": 71},
            {"day": "Miércoles", "temp": 59},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 54},
            {"day": "Sábado", "temp": 47},
            {"day": "Domingo", "temp": 30}
        ]
    ],
    [  # Ciudad 3
        [  # Semana 1
            {"day": "Lunes", "temp": 59},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 49},
            {"day": "Jueves", "temp": 51},
            {"day": "Viernes", "temp": 68},
            {"day": "Sábado", "temp": 57},
            {"day": "Domingo", "temp": 52}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 49},
            {"day": "Martes", "temp": 1},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 67},
            {"day": "Sábado", "temp": 81},
            {"day": "Domingo", "temp": 61}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 51},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 75},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 49},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 73}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 82},
            {"day": "Martes", "temp": 40},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 59},
            {"day": "Viernes", "temp": 76},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 60}
        ]
    ]
]


# Función para calcular el promedio
def calcular_promedio(temperaturas, ciudad_idx):
    ciudad = temperaturas[ciudad_idx]  # Acceder a la ciudad usando el índice proporcionado
    suma_temperaturas = 0
    total_dias = 0

    # Recorrer las semanas
    for semana in ciudad:
        for dia in semana:
            suma_temperaturas += dia["temp"]
            total_dias += 1

    # Calcular el promedio
    promedio = suma_temperaturas / total_dias
    return promedio


# Menú interactivo
while True:
    print("Selecciona una ciudad:")
    print("1 - Ciudad 1")
    print("2 - Ciudad 2")
    print("3 - Ciudad 3")
    print("4 - Salir")

#seleccione la ciudad
    opcion = input("Ingrese una opción: ")

    if opcion == "1": #calculo del promedio total de las temperaturas de la cuidad 1
        promedio = calcular_promedio(temperaturas, 0)
        print(f'El promedio total de temperatura de la Ciudad 1 es: {promedio:.2f}°F')
    elif opcion == "2": #calculo del promedio total de las temperaturas de la cuidad 2
        promedio = calcular_promedio(temperaturas, 1)
        print(f'El promedio total de temperatura de la Ciudad 2 es: {promedio:.2f}°F')
    elif opcion == "3": #calculo del promedio total de las temperaturas de la cuidad 3
        promedio = calcular_promedio(temperaturas, 2)
        print(f'El promedio total de temperatura de la Ciudad 3 es: {promedio:.2f}°F')
    elif opcion == "4": #saliendo del menu
        print("Saliendo...")
        break
    else: #en caso que ingrese otra opcion
        print("Opción no válida, intenta de nuevo.")
















