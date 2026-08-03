import tkinter as tk
from tkinter import ttk, messagebox
from controlador_serv import ControladorServicios
from datetime import datetime
from exceptions.costo_invalido import CostoInvalidoError
from exceptions.servicio_no_encontrado import ServicioNoEncontradoError

class TallerApp:

    def __init__(self):

        self.controlador = ControladorServicios()
        self.id_actual = None

        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Gestión de Servicios")

        ancho = self.ventana.winfo_screenwidth()
        alto = self.ventana.winfo_screenheight()

        self.ventana.geometry(f"{ancho}x{alto}")
        self.ventana.state("zoomed")
        self.ventana.configure(bg="#121826")

        self.COLOR_FONDO = "#121826"
        self.COLOR_PANEL = "#1D2433"
        self.COLOR_MORADO = "#7C3AED"
        self.COLOR_VERDE = "#10B981"
        self.COLOR_ROJO = "#EF4444"
        self.COLOR_AZUL = "#3B82F6"
        self.estilos()

        self.crear_header()

        self.crear_contenedor()

        self.crear_panel_superior()

        self.crear_panel_formulario()

        self.crear_panel_busqueda()

        self.crear_panel_botones()

        self.crear_panel_tabla()

        self.actualizar_hora()

        self.mostrar()

        self.ventana.mainloop()

    def estilos(self):

        estilo = ttk.Style()

        estilo.theme_use("clam")

    def crear_header(self):

        self.header = tk.Frame(
            self.ventana,
            bg="#0F172A",
            height=110
        )

        self.header.pack(fill="x")

        self.header.pack_propagate(False)

        self.lblTitulo = tk.Label(
            self.header,
            text="🚗 TALLER MECÁNICO",
            bg="#0F172A",
            fg="white",
            font=("Segoe UI", 28, "bold")
        )

        self.lblTitulo.place(x=30, y=20)

        self.lblSub = tk.Label(
            self.header,
            text="Sistema de Gestión de Servicios",
            bg="#0F172A",
            fg="#A78BFA",
            font=("Segoe UI", 14)
        )

        self.lblSub.place(x=35, y=65)

        self.lblFecha = tk.Label(
            self.header,
            bg="#0F172A",
            fg="white",
            font=("Segoe UI", 12)
        )

        self.lblFecha.place(relx=.98, y=25, anchor="ne")

        self.lblHora = tk.Label(
            self.header,
            bg="#0F172A",
            fg="#60A5FA",
            font=("Segoe UI", 18, "bold")
        )

        self.lblHora.place(relx=.98, y=55, anchor="ne")

    def actualizar_hora(self):

        ahora = datetime.now()

        self.lblHora.config(
            text=ahora.strftime("%H:%M:%S")
        )

        self.lblFecha.config(
            text=ahora.strftime("%d/%m/%Y")
        )

        self.ventana.after(
            1000,
            self.actualizar_hora
        )

    def crear_contenedor(self):

        self.contenedor = tk.Frame(
            self.ventana,
            bg=self.COLOR_FONDO
        )

        self.contenedor.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def crear_panel_superior(self):

        self.panelSuperior = tk.Frame(
        self.contenedor,
        bg=self.COLOR_FONDO
    )

        self.panelSuperior.pack(
        fill="x"
    )

    def crear_campo(self, texto, fila):

        lbl = tk.Label(
        self.panelFormulario,
        text=texto,
        bg=self.COLOR_PANEL,
        fg="white",
        font=("Segoe UI", 11)
    )

        lbl.place(
        x=40,
        y=fila
    )

        entry = tk.Entry(
        self.panelFormulario,
        font=("Segoe UI", 12),
        bd=0,
        relief="flat"
    )

        entry.place(
        x=40,
        y=fila + 28,
        width=620,
        height=35
    )

        return entry

    def crear_panel_formulario(self):

        self.panelFormulario = tk.Frame(
        self.panelSuperior,
        bg=self.COLOR_PANEL,
        width=720,
        height=330,
        highlightbackground="#374151",
        highlightthickness=1
    )

        self.panelFormulario.pack(
        side="left",
        padx=(0, 20)
    )

        self.panelFormulario.pack_propagate(False)

        titulo = tk.Label(
        self.panelFormulario,
        text="INFORMACIÓN DEL SERVICIO",
        bg=self.COLOR_PANEL,
        fg="white",
        font=("Segoe UI", 15, "bold")
    )

        titulo.pack(pady=15)

        self.txtCliente = self.crear_campo(
        "Cliente",
        60
    )

        self.txtVehiculo = self.crear_campo(
        "Vehículo",
        120
    )

        self.txtTipo = self.crear_campo(
        "Tipo de servicio",
        180
    )

        self.txtCosto = self.crear_campo(
        "Costo",
        240
    )

    def crear_panel_busqueda(self):

        self.panelBusqueda = tk.Frame(
        self.panelSuperior,
        bg=self.COLOR_PANEL,
        width=420,
        height=330,
        highlightbackground="#374151",
        highlightthickness=1
    )

        self.panelBusqueda.pack(
        side="left"
    )

        self.panelBusqueda.pack_propagate(False)

        titulo = tk.Label(
        self.panelBusqueda,
        text="BUSCAR SERVICIO",
        bg=self.COLOR_PANEL,
        fg="white",
        font=("Segoe UI",15,"bold")
    )

        titulo.pack(pady=15)

        lbl = tk.Label(
        self.panelBusqueda,
        text="Buscar cliente, vehículo o servicio",
        bg=self.COLOR_PANEL,
        fg="white",
        font=("Segoe UI",11)
    )

        lbl.pack(
        anchor="w",
        padx=30
    )

        self.txtBuscar = tk.Entry(
        self.panelBusqueda,
        font=("Segoe UI",12),
        bd=0,
        relief="flat"
    )

        self.txtBuscar.pack(
        fill="x",
        padx=30,
        pady=(8,20),
        ipady=8
    )
        self.txtBuscar.bind(
            "<KeyRelease>",
            self.buscar_dinamico
    )

        self.btnBuscar = tk.Button(
            self.panelBusqueda,
            text="Limpiar búsqueda",
            bg=self.COLOR_AZUL,
            fg="white",
            font=("Segoe UI",11,"bold"),
            relief="flat",
            cursor="hand2",
            command=self.limpiar_busqueda
        )

        self.btnBuscar.pack(
        fill="x",
        padx=30,
        ipady=8
    )

    def crear_panel_botones(self):

        self.panelBotones = tk.Frame(
            self.contenedor,
            bg=self.COLOR_FONDO
        )

        self.panelBotones.pack(
            pady=25
    )

        self.btnRegistrar = tk.Button(
            self.panelBotones,
            text="➕ Registrar",
            bg="#7C3AED",
            fg="white",
            font=("Segoe UI",11,"bold"),
            relief="flat",
            cursor="hand2",
            width=16,
            height=2,
            command=self.registrar
        )

        self.btnRegistrar.pack(
        side="left",
        padx=10
    )

        self.btnActualizar = tk.Button(
        self.panelBotones,
        text="✏️ Actualizar",
        bg="#10B981",
        fg="white",
        font=("Segoe UI",11,"bold"),
        relief="flat",
        cursor="hand2",
        width=16,
        height=2,
        command=self.actualizar
    )
        self.btnActualizar.pack(
        side="left",
        padx=10
    )

        self.btnEliminar = tk.Button(
        self.panelBotones,
        text="🗑️ Eliminar",
        bg="#EF4444",
        fg="white",
        font=("Segoe UI",11,"bold"),
        relief="flat",
        cursor="hand2",
        width=16,
        height=2,
        command=self.eliminar
    )

        self.btnEliminar.pack(
        side="left",
        padx=10
    )

    def crear_panel_tabla(self):

        self.panelTabla = tk.Frame(
            self.contenedor,
            bg=self.COLOR_FONDO
        )

        self.panelTabla.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "id",
            "cliente",
            "vehiculo",
            "tipo",
            "costo"
        )

        self.tabla = ttk.Treeview(
            self.panelTabla,
            columns=columnas,
            show="headings",
            height=12
        )

        self.tabla.heading("id", text="ID")
        self.tabla.heading("cliente", text="Cliente")
        self.tabla.heading("vehiculo", text="Vehículo")
        self.tabla.heading("tipo", text="Tipo de Servicio")
        self.tabla.heading("costo", text="Costo")

        self.tabla.column("id", width=70, anchor="center")
        self.tabla.column("cliente", width=220)
        self.tabla.column("vehiculo", width=220)
        self.tabla.column("tipo", width=220)
        self.tabla.column("costo", width=120, anchor="center")

        scrollbar = ttk.Scrollbar(
            self.panelTabla,
            orient="vertical",
            command=self.tabla.yview
        )

        self.tabla.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )
        self.tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar
        )

    def mostrar(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        registros = self.controlador.mostrar()

        for registro in registros:
            self.tabla.insert(
                "",
                tk.END,
                values=registro
            )

    def seleccionar(self, event):

        fila = self.tabla.focus()

        if fila == "":
            return

        datos = self.tabla.item(fila)

        valores = datos["values"]

        self.id_actual = valores[0]

        self.txtCliente.delete(0, tk.END)
        self.txtCliente.insert(0, valores[1])

        self.txtVehiculo.delete(0, tk.END)
        self.txtVehiculo.insert(0, valores[2])

        self.txtTipo.delete(0, tk.END)
        self.txtTipo.insert(0, valores[3])

        self.txtCosto.delete(0, tk.END)
        self.txtCosto.insert(0, valores[4])

    def registrar(self):

        cliente = self.txtCliente.get().strip()
        vehiculo = self.txtVehiculo.get().strip()
        tipo = self.txtTipo.get().strip()
        costo = self.txtCosto.get().strip()

        if cliente == "" or vehiculo == "" or tipo == "" or costo == "":
            messagebox.showwarning(
                "Campos vacíos",
                "Completa toda la información."
            )
            return

        try:
            costo = costo.replace(",", "")
            costo = float(costo)

            self.controlador.registrar(
                cliente,
                vehiculo,
                tipo,
                costo
            )

            self.mostrar()      # ← Cambia esta línea
            self.limpiar()

            messagebox.showinfo(
                "Correcto",
                "Servicio registrado correctamente."
            )

        except CostoInvalidoError as e:

            messagebox.showerror(
                "Costo inválido",
                str(e)
            )

        except ValueError as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

        # ==========================================
# ACTUALIZAR
# ==========================================

    def actualizar(self):

        if self.id_actual is None:
            messagebox.showwarning(
                "Aviso",
                "Seleccione un servicio de la tabla."
            )
            return

        cliente = self.txtCliente.get().strip()
        vehiculo = self.txtVehiculo.get().strip()
        tipo = self.txtTipo.get().strip()
        costo = self.txtCosto.get().strip()

        try:
            costo = costo.replace(",", "")
            costo = float(costo)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Costo inválido."
            )
            return

        self.controlador.actualizar(
            self.id_actual,
            cliente,
            vehiculo,
            tipo,
            costo
        )

        self.mostrar()

        self.limpiar()

        messagebox.showinfo(
            "Correcto",
            "Servicio actualizado."
        )

# ==========================================
# ELIMINAR
# ==========================================

    def eliminar(self):

        if self.id_actual is None:
            messagebox.showwarning(
                "Aviso",
                "Seleccione un servicio."
            )
            return

        respuesta = messagebox.askyesno(
            "Confirmar",
            "¿Desea eliminar este servicio?"
        )

        if not respuesta:
            return

        try:

            self.controlador.eliminar(
                self.id_actual
            )

            self.mostrar()

            self.limpiar()

            messagebox.showinfo(
                "Correcto",
                "Servicio eliminado."
            )

        except ServicioNoEncontradoError as e:

            messagebox.showerror(
                "Servicio no encontrado",
                str(e)
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

# ==========================================
# BUSCADOR DINÁMICO
# ==========================================

    def buscar_dinamico(self, event=None):

        texto = self.txtBuscar.get().strip().lower()

        # Limpiar la tabla
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        registros = self.controlador.mostrar()

        for registro in registros:

            cadena = " ".join(str(x).lower() for x in registro)

            if texto in cadena:
                self.tabla.insert(
                    "",
                    tk.END,
                    values=registro
                )

    def buscar_dinamico(self, event=None):

        texto = self.txtBuscar.get().strip().lower()

        # Limpiar tabla
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        registros = self.controlador.mostrar()

        # Si no escribió nada, mostrar todo
        if texto == "":
            for registro in registros:
                self.tabla.insert("", tk.END, values=registro)
            return

        for registro in registros:

            id_servicio = str(registro[0]).lower()
            cliente = str(registro[1]).lower()
            vehiculo = str(registro[2]).lower()
            servicio = str(registro[3]).lower()
            costo = str(registro[4]).lower()

            if (
                cliente.startswith(texto)
                or vehiculo.startswith(texto)
                or servicio.startswith(texto)
                or id_servicio == texto
                or costo.startswith(texto)
            ):

                self.tabla.insert(
                    "",
                    tk.END,
                    values=registro
                )

    # ==========================================
# LIMPIAR BÚSQUEDA
# ==========================================

    def limpiar_busqueda(self):

        self.txtBuscar.delete(0, tk.END)

        self.mostrar()


    def limpiar(self):

        self.txtCliente.delete(0, tk.END)
        self.txtVehiculo.delete(0, tk.END)
        self.txtTipo.delete(0, tk.END)
        self.txtCosto.delete(0, tk.END)

        if hasattr(self, "txtBuscar"):
            self.txtBuscar.delete(0, tk.END)

        self.id_actual = None

if __name__ == "__main__":
    TallerApp()