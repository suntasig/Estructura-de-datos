from fpdf import FPDF

# Crear clase para configurar el PDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", size=12)
        self.cell(0, 10, "Manejo de Productos personal", border=False, ln=1, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", size=8)
        self.cell(0, 10, f'Página {self.page_no()}', align="C")

# Crear documento PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_left_margin(15)
pdf.set_right_margin(15)

# Página 1: Carátula
pdf.add_page()
pdf.set_font("Arial", size=14, style="B")
pdf.ln(30)  # Más espacio en la parte superior
pdf.cell(0, 10, "Universidad Estatal Amazónica", ln=1, align="C")
pdf.ln(15)
pdf.set_font("Arial", size=12)
pdf.ln(25)
pdf.set_font("Arial", size=12)
pdf.cell(0, 8, "Estudiante: Luis Kleber Suntasig Ríos", ln=1, align="C")
pdf.cell(0, 8, "Carrera: Tecnología de la Información", ln=1, align="C")
pdf.cell(0, 8, "Nivel: Tercer Semestre", ln=1, align="C")
pdf.cell(0, 8, "Fecha: 20/12/2024", ln=1, align="C")

# Página 2: Introducción, Desarrollo, Conclusión y Bibliografía
pdf.add_page()
pdf.set_font("Arial", size=12, style="B")
pdf.cell(0, 8, "Introducción", ln=1)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 8, (
    "Este documento presenta una solución en Python para gestionar un sistema de registro de productos. "
    "Se implementan clases, arrays y matrices para representar los datos principales de los productos: ID, nombre, unidad y precios. "
    "Esta estructura es ideal para aplicaciones de inventarios y facturación."
))
pdf.ln(10)

pdf.set_font("Arial", size=12, style="B")
pdf.cell(0, 8, "Desarrollo", ln=1)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 8, (
    "El desarrollo del sistema incluye la definición de una clase `Producto` para estructurar la información, "
    "así como el uso de listas (arrays) para almacenar múltiples productos. A continuación, se muestra el código:"
))
pdf.ln(5)

# Código de ejemplo
pdf.set_font("Courier", size=10)
pdf.multi_cell(0, 7, """
class Producto:
    def __init__(self, id, nombre, unidad, precios):
        self.id = id
        self.nombre = nombre
        self.unidad = unidad 
        self.precios = precios
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Unidad: {self.unidad}, Precios: {self.precios}"

productos = []
productos.append(Producto(1, "Manzana", "Kg", [0.5, 0.6, 0.55]))
productos.append(Producto(2, "Leche", "Litro", [1.2, 1.3, 1.25]))
for producto in productos:
    print(producto)
""")
pdf.ln(10)

# Conclusión
pdf.set_font("Arial", size=12, style="B")
pdf.cell(0, 8, "Conclusión", ln=1)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 8, (
    "El uso de clases y estructuras como arrays y matrices en Python proporciona un manejo eficiente y organizado de datos. "
    "Esta solución permite gestionar productos y precios de manera flexible, siendo aplicable a sistemas de inventario o facturación más complejos. "
    "La implementación puede extenderse fácilmente para adaptarse a diferentes necesidades empresariales."
))
pdf.ln(10)

# Bibliografía
pdf.set_font("Arial", size=12, style="B")
pdf.cell(0, 8, "Bibliografía", ln=1)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 8, "- Documentación oficial")

# Guardar PDF
file_path = "Manejo_Productos_Personal_Caratula.pdf"
pdf.output(file_path)

print(f"El archivo PDF se ha guardado correctamente como '{file_path}'.")
