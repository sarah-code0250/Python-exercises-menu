    while True:

    print("MENU DE EJERCICIOS")
    print("1. Ejercicio 1: Parqueadero")
    print("2. Ejercicio 2: Descuentos")
    print("3. Ejercicio 3: Venta de perros")
    print("4. Salir")

    opcion = input("Elige el ejercicio que quieras: ")

    if opcion == "1":
        print("Playa de estacionamiento")

        horas = int(input("Ingrese las horas que se estaciono: "))

        if horas == 1:
            pago = 1500
            print(f"Debe pagar: ${pago:,.0f}")

        elif horas > 1:
            pago = 1500 + (horas - 1) * 1000
            print(f"Debe pagar: ${pago:,.0f}")

        else:
            print("No debe pagar")


    elif opcion == "2":
        print("Descuento de producto")

        precio = float(input("Ingrese el precio del producto: "))
        docenas = int(input("Ingrese la cantidad de docenas: "))

        costo_total = precio * docenas

        if docenas > 3:
            descuento = costo_total * 0.15
        else:
            descuento = costo_total * 0.10

        costo_con_descuento = costo_total - descuento

        print(f"Costo de la compra: ${costo_total:,.0f}")
        print(f"El descuento es: ${descuento:,.0f}")
        print(f"El producto con descuento vale: ${costo_con_descuento:,.0f}")


    elif opcion == "3":
        print("Venta de perros")

        print("1. Perro negro - $100,000")
        print("2. Perro blanco - $30,000")
        print("3. Perro moreno - $60,000")

        perro = input("Elija el perro que quiere comprar: ")
        cantidad = int(input("Ingrese la cantidad de perros: "))

        if perro == "1":
            precio = 100000

        elif perro == "2":
            precio = 30000

        elif perro == "3":
            precio = 60000

        else:
            print("Opcion no valida")
            precio = 0

        total = precio * cantidad

        if precio > 0:
            print(f"El precio del perro es: ${precio:,.0f}")
            print(f"La cantidad de perros es: {cantidad}")
            print(f"El costo total de la compra es: ${total:,.0f}")
            print("Disfruta tu mascota")


    elif opcion == "4":
        print("Salir del programa")
        break

    else:
        print("Opcion no valida")
