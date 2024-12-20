from fpdf import FPDF

# Crear el documento PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Título
pdf.set_font("Arial", style="B", size=16)
pdf.cell(200, 10, "Cálculo de Área y Perímetro de Figuras Geométricas en Python", ln=True, align="C")
pdf.ln(10)

# Introducción
pdf.set_font("Arial", style="B", size=14)
pdf.cell(0, 10, "Introducción", ln=True)
pdf.set_font("Arial", size=12)
intro = (
    "En este documento, se presentan dos clases en Python para trabajar con figuras geométricas. "
    "Cada clase encapsula datos relacionados con una figura específica (como círculos y rectángulos) "
    "y proporciona métodos para calcular su área y perímetro. "
    "Los comentarios explican detalladamente el propósito de cada método y su funcionamiento."
)
pdf.multi_cell(0, 10, intro)
pdf.ln(10)

# Código
pdf.set_font("Arial", style="B", size=14)
pdf.cell(0, 10, "Código", ln=True)
pdf.set_font("Courier", size=10)
codigo = (
    "# Clase para un circulo\n"
    "class Circulo:\n"
    "    def __init__(self, radio):\n"
    "        \"\"\"\n"
    "        Constructor para la clase Circulo.\n"
    "        :param radio: Radio del circulo (float).\n"
    "        \"\"\"\n"
    "        self.radio = radio\n\n"
    "    def calcular_area(self):\n"
    "        \"\"\"\n"
    "        Calcula el area del circulo.\n"
    "        Formula: pi * radio^2\n"
    "        :return: Area del circulo (float).\n"
    "        \"\"\"\n"
    "        import math\n"
    "        return math.pi * self.radio ** 2\n\n"
    "    def calcular_perimetro(self):\n"
    "        \"\"\"\n"
    "        Calcula el perimetro del circulo.\n"
    "        Formula: 2 * pi * radio\n"
    "        :return: Perimetro del circulo (float).\n"
    "        \"\"\"\n"
    "        import math\n"
    "        return 2 * math.pi * self.radio\n\n"
    "# Clase para un rectangulo\n"
    "class Rectangulo:\n"
    "    def __init__(self, largo, ancho):\n"
    "        \"\"\"\n"
    "        Constructor para la clase Rectangulo.\n"
    "        :param largo: Largo del rectangulo (float).\n"
    "        :param ancho: Ancho del rectangulo (float).\n"
    "        \"\"\"\n"
    "        self.largo = largo\n"
    "        self.ancho = ancho\n\n"
    "    def calcular_area(self):\n"
    "        \"\"\"\n"
    "        Calcula el area del rectangulo.\n"
    "        Formula: largo * ancho\n"
    "        :return: Area del rectangulo (float).\n"
    "        \"\"\"\n"
    "        return self.largo * self.ancho\n\n"
    "    def calcular_perimetro(self):\n"
    "        \"\"\"\n"
    "        Calcula el perimetro del rectangulo.\n"
    "        Formula: 2 * (largo + ancho)\n"
    "        :return: Perimetro del rectangulo (float).\n"
    "        \"\"\"\n"
    "        return 2 * (self.largo + self.ancho)\n\n"
    "# Ejemplo de uso\n"
    "if __name__ == \"__main__\":\n"
    "    # Crear un circulo con radio 5\n"
    "    circulo = Circulo(5)\n"
    "    print(f\"Area del circulo: {circulo.calcular_area():.2f}\")\n"
    "    print(f\"Perimetro del circulo: {circulo.calcular_perimetro():.2f}\")\n\n"
    "    # Crear un rectangulo con largo 10 y ancho 4\n"
    "    rectangulo = Rectangulo(10, 4)\n"
    "    print(f\"Area del rectangulo: {rectangulo.calcular_area():.2f}\")\n"
    "    print(f\"Perimetro del rectangulo: {rectangulo.calcular_perimetro():.2f}\")\n"
)
pdf.multi_cell(0, 5, codigo)
pdf.ln(10)

# Conclusión
pdf.set_font("Arial", style="B", size=14)
pdf.cell(0, 10, "Conclusión", ln=True)
pdf.set_font("Arial", size=12)
conclusion = (
    "Este codigo demuestra como utilizar la programacion orientada a objetos para modelar "
    "figuras geometricas y realizar calculos utiles como el area y el perimetro. "
    "Gracias a los metodos encapsulados, el codigo es claro, modular y facil de mantener."
)
pdf.multi_cell(0, 10, conclusion)

# Guardar el archivo
output_path = "Figuras_Geometricas_Python.pdf"
pdf.output(output_path)
