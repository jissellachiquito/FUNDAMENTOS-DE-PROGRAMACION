# Funcion para calcular descuento
def calcular_descuento(monto_total, porcentaje_descuento=12):
# Calcular el monto del descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Primer monto calculado
monto1 = 1050  # El primer monto total de la compra
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1
print(f"Primera compra: Primer monto total = ${monto1}, Descuento = ${descuento1:.2f}, Monto final = ${monto_final1:.2f}")

# Segundo monto calculado
monto2 = 2560  # El segundo monto total de la compra
porcentaje_descuento2 = 25  # Ejemplo de otro porcentaje de descuento
descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
monto_final2 = monto2 - descuento2
print(f"Segunda compra: Segundo monto total = ${monto2}, Descuento = ${descuento2:.2f}, Monto final = ${monto_final2:.2f}")



