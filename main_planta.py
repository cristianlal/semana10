from planta_clases import Automovil, BandaTransportadora, BrazoMecanico, Supervisor

banda_principal = BandaTransportadora()
brazo_robotico = BrazoMecanico("RX-100")

print("Digite el nombre o código del supervisor de planta: ")
encargado = str(input())
jefe_linea = Supervisor(encargado)

while True:
    print("\n==========================================")
    print("digite la letra 'A' para Cargar Automoviles a la banda")
    print("digite la letra 'B' para Activar el Brazo y poner vidrios")
    print("digite la letra 'C' para Consultar el reporte consolidado")
    print("digite la letra 'S' para salir del programa")
    
    letra = str(input())

    if letra == 'A' or letra == 'a':
        print("Digite la cantidad de automoviles que van a entrar: ")
        total_autos = int(input())
        for i in range(total_autos):
            auto_nuevo = Automovil(i + 1)
            banda_principal.registrar_auto(auto_nuevo)
            print(auto_nuevo.mostrar_datos())
            
    elif letra == 'B' or letra == 'b':
        if len(banda_principal.lista_autos) == 0:
            print("Aún no se han registrado automoviles en la banda.")
        else:
            for vehiculo in banda_principal.lista_autos:
                jefe_linea.ejecutar_montaje(banda_principal, brazo_robotico, vehiculo)
                
    elif letra == 'C' or letra == 'c':
        print("\n--- Estado de la Línea ---")
        print(jefe_linea.reporte_consolidado(banda_principal))
        
    elif letra == 'S' or letra == 's':
        print("finalizo con exito \n")
        break
        
    else:
        print("Sigue dentro del proceso del DO WHILE \n")

print("EL DO-WHILE a finalizado \n")