# =====================================
# DATOS INICIALES
# =====================================

productos = {
    "1": {
        "nombre": "Espresso",
        "precio": 2500,
        "cafe": 18,
        "leche": 0
    },

    "2": {
        "nombre": "Cafe con leche",
        "precio": 3500,
        "cafe": 18,
        "leche": 150
    },

    "3": {
        "nombre": "Filtrado V60",
        "precio": 4000,
        "cafe": 20,
        "leche": 0
    },

    "4": {
        "nombre": "Bolsa de granos 250g",
        "precio": 12000,
        "cafe": 250,
        "leche": 0
    }
}

inventario = {
    "cafe": 5000,
    "leche": 10000
}

historial_ventas = []


# =====================================
# FUNCIONES
# =====================================

def mostrar_menu():

    print("\n" + "=" * 40)
    print("SMART ROAST")
    print("=" * 40)

    print("1. Registrar venta")
    print("2. Ver inventario")
    print("3. Ver historial")
    print("4. Ver facturación total")
    print("0. Salir")

def mostrar_productos(productos):

    print("\nCATÁLOGO")

    for codigo, producto in productos.items():

        print(
            f"{codigo}. {producto['nombre']} - ${producto['precio']}"
        )

def registrar_venta(
    inventario,
    historial,
    productos,
    opcion_producto,
    cantidad
):

    if opcion_producto not in productos:
        return False, 0

    try:

        cantidad_num = int(cantidad)

        if cantidad_num <= 0:
            return False, 0

    except ValueError:

        return False, 0

    cafe_necesario = (
        productos[opcion_producto]["cafe"]
        * cantidad_num
    )

    leche_necesaria = (
        productos[opcion_producto]["leche"]
        * cantidad_num
    )

    if (
        inventario["cafe"] < cafe_necesario
        or
        inventario["leche"] < leche_necesaria
    ):
        return False, 0

    inventario["cafe"] -= cafe_necesario
    inventario["leche"] -= leche_necesaria

    total = (
        productos[opcion_producto]["precio"]
        * cantidad_num
    )

    historial.append(
        {
            "producto": productos[opcion_producto]["nombre"],
            "cantidad": cantidad_num,
            "total": total
        }
    )

    return True, total

def calcular_cambio(
    total,
    dinero_recibido
):

    try:

        dinero = float(
            dinero_recibido
        )

        if dinero < total:
            return False, 0

        cambio = dinero - total

        return True, cambio

    except ValueError:

        return False, 0
    
def mostrar_inventario(
    inventario
):

    print("\nINVENTARIO")

    print(
        f"Café: {inventario['cafe']} gr"
    )

    print(
        f"Leche: {inventario['leche']} ml"
    )


def mostrar_historial(
    historial
):

    print("\nHISTORIAL DE VENTAS")

    if len(historial) == 0:

        print(
            "No existen ventas registradas."
        )

        return

    for venta in historial:

        print("-" * 30)

        print(
            f"Producto: {venta['producto']}"
        )

        print(
            f"Cantidad: {venta['cantidad']}"
        )

        print(
            f"Total: ${venta['total']}"
        )







def calcular_facturacion_total(
    historial
):

    acumulador = 0

    for venta in historial:

        acumulador += venta["total"]

    return acumulador



def alerta_stock(
    inventario
):

    if inventario["cafe"] <= 500:

        print(
            "\nALERTA: stock de cafe bajo."
        )


# =====================================
# PROGRAMA PRINCIPAL
# =====================================

def main():

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opcion: "
        )

        if opcion == "0":

            print(
                "\nGracias por utilizar Smart Roast."
            )

            break

        elif opcion == "1":

            mostrar_productos(
                productos
            )

            producto = input(
                "\nSeleccione producto: "
            )

            cantidad = input(
                "Cantidad: "
            )

            exito, total = registrar_venta(
                inventario,
                historial_ventas,
                productos,
                producto,
                cantidad
            )

            if exito:

                print(
                    f"\nTotal a cobrar: ${total}"
                )

                dinero = input(
                    "Dinero recibido: $"
                )

                venta_ok, cambio = calcular_cambio(
                    total,
                    dinero
                )

                if venta_ok:

                    print(
                        f"Cambio: ${cambio}"
                    )

                    alerta_stock(
                        inventario
                    )

                else:

                    print(
                        "Monto insuficiente."
                    )

            else:

                print(
                    "No fue posible registrar la venta."
                )

        elif opcion == "2":

            mostrar_inventario(
                inventario
            )

        elif opcion == "3":

            mostrar_historial(
                historial_ventas
            )
        
        elif opcion == "4":

            total = calcular_facturacion_total(
                historial_ventas
            )

            print(
                f"\nFacturación total: ${total}"
            )

        else:

            print(
                "Opción inválida."
            )



if __name__ == "__main__":
    main()