
def factura_cliente(factura,propina):
    propina_total = factura * propina / 100
    return (
        f"Subtotal: {factura:.2f}\n"
        f"Propina: {propina}%\n"
        f"Total: {factura + propina_total:.2f}" 
    )

factura = float(input("Ingresa el total de la cuenta: "))

if factura <= 0:
    print("Error la factura debes de ser mayor que 0")
else:
    propina = int(input("Ingresa el porciento de la propina: "))
    resultado = factura_cliente(factura,propina)
    print(resultado)
