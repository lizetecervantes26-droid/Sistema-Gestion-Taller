from interfaz_v2 import TallerApp
import tkinter as tk


def main():
    ventana = tk.Tk()
    app = TallerApp(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()