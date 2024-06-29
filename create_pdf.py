from fpdf import FPDF
from PIL import Image

# Determine as dimensões originais da imagem
image_path = 'logo.png'
image = Image.open(image_path)
image_width, image_height = image.size

# Converta as dimensões para milímetros (1 inch = 25.4 mm)
mm_per_inch = 25.4
image_width_mm = image_width * mm_per_inch / image.info['dpi'][0]
image_height_mm = image_height * mm_per_inch / image.info['dpi'][1]

# Crie uma classe PDF
class PDF(FPDF):
    def header(self):
        # Adiciona a imagem logo.png centralizada
        page_width = self.w
        x_position = (page_width - image_width_mm) / 2
        self.image(image_path, x = x_position, y = 10, w = image_width_mm, h = image_height_mm)
        self.set_y(10 + image_height_mm + 10)  # Ajusta a posição do título após a imagem
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Suas respostas ao recrutamento Fury', 0, 1, 'C')
        self.ln(10)  # Adiciona um espaço após o título

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

def instance_pdf(data, nickname):
    # Inicialize o PDF
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font('Arial', '', 12)

    # Adicione os dados do dicionário ao PDF
    for key, value in data.items():
        pdf.set_font('Arial', 'B', 12)  # Fonte em negrito para as chaves
        pdf.cell(50, 10, f'{key}:', 0, 0)
        pdf.set_font('Arial', '', 12)  # Fonte normal para os valores
        pdf.cell(0, 10, f'{value}', 0, 1)

    # Salve o PDF
    pdf_output_path = f'pdf/respostas_form_{nickname}.pdf'
    pdf.output(pdf_output_path)
