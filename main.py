
from database import inicializar_database
from interface import MainWindow


# Prepara o banco antes de abrir o sistema.
inicializar_database()

# Inicializa a interface gráfica.
app = MainWindow()
app.mainloop()
