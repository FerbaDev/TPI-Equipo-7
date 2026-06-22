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

def mostrar_menu():

    print("\n" + "=" * 40)
    print("SMART ROAST")
    print("=" * 40)

    print("1. Espresso")
    print("2. Cafe con leche")
    print("3. Filtrado V60")
    print("4. Bolsa de granos 250g")
    print("5. Ver inventario")
    print("6. Ver historial")
    print("0. Salir")

def verificar_stock(
    inventario,
    productos,
    opcion,
    cantidad
):

    cafe_necesario = (
        productos[opcion]["cafe"]
        * cantidad
    )

    leche_necesaria = (
        productos[opcion]["leche"]
        * cantidad
    )

    if (
        inventario["cafe"] >= cafe_necesario
        and
        inventario["leche"] >= leche_necesaria
    ):
        return True

    return False

def main():

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opcion: "
        )

        if opcion == "0":
            break

        elif opcion == "5":

            print("\nINVENTARIO")

            print(
                "Cafe:",
                inventario["cafe"],
                "gr"
            )

            print(
                "Leche:",
                inventario["leche"],
                "ml"
            )


if __name__ == "__main__":
    main()