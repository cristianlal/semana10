class Automovil:
    def __init__(self, codigo_auto):
        self.codigo_auto = codigo_auto
        self.panoramico_puesto = "No"
        self.fase = "pendiente"

    def get_panoramico(self):
        return self.panoramico_puesto

    def set_panoramico(self, valor):
        self.panoramico_puesto = valor

    def mostrar_datos(self):
        return f"Automóvil #{self.codigo_auto} -> Panorámico: {self.panoramico_puesto} | Fase: {self.fase}"


class BandaTransportadora:
    def __init__(self):
        self.lista_autos = []
        self.estado_banda = "quieta"

    def registrar_auto(self, auto):
        self.lista_autos.append(auto)

    def avanzar_banda(self, auto):
        self.estado_banda = "rodando"
        auto.fase = "en zona de robot"
        return f"[Banda {self.estado_banda}] Moviendo el Automóvil #{auto.codigo_auto}..."

    def frenar_banda(self):
        self.estado_banda = "frenada"
        return f"[Banda {self.estado_banda}] Vehículo asegurado para el montaje."


class BrazoMecanico:
    def __init__(self, referencia):
        self.referencia = referencia
        self.tarea_actual = "en reposo"

    def colocar_panoramico(self, auto):
        if auto.get_panoramico() == "No":
            self.tarea_actual = "fijando vidrio con ventosas"
            auto.set_panoramico("Sí")
            auto.fase = "terminado"
        else:
            self.tarea_actual = "esperando (el auto ya tenía vidrio)"

    def mostrar_datos(self):
        return f"[Brazo {self.referencia}] Acción: {self.tarea_actual}"


class Supervisor:
    def __init__(self, identificacion):
        self.identificacion = identificacion

    def ejecutar_montaje(self, banda, brazo, auto):
        print(f"\n>>> Supervisor {self.identificacion} enviando orden desde la tablet <<<")
        print(banda.avanzar_banda(auto))
        print(banda.frenar_banda())
        brazo.colocar_panoramico(auto)
        print(brazo.mostrar_datos())
        print(auto.mostrar_datos())

    def reporte_consolidado(self, banda):
        terminados = sum(1 for a in banda.lista_autos if a.fase == "terminado")
        faltantes = sum(1 for a in banda.lista_autos if a.fase == "pendiente")
        return f"Reporte Consolidado:\n- Autos terminados: {terminados}\n- Autos faltantes: {faltantes}"