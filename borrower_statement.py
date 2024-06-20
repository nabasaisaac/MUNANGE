from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from io import BytesIO
import os
import sys
import tempfile
from datetime import date, datetime


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class BorrowerStatement:
    def __init__(self, directory, borrower_photo, borrowers_data, loan_date, payments_info, missed_days,
                 remaining_days):
        # Generate PDF in memory
        if directory:
            c = canvas.Canvas(f'{directory}/{borrowers_data[1]}.pdf', pagesize=letter)
        else:
            pdf_buffer_memory = BytesIO()
            c = canvas.Canvas(pdf_buffer_memory, pagesize=letter)
            c.setTitle(f'{borrowers_data[1]}')
        # Example content, customize as needed
        c.drawImage(resource_path('images/munange_pdf_logo.png'), 30, 700, width=70, height=70)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(120, 755, "MUNANGE FINANCIAL SERVICES LTD")
        c.drawString(120, 740, "P.0 BOX 268, Masaka, Uganda")
        c.drawString(120, 725, "Tel: 0701677728/0755299598")
        c.setFont("Helvetica", 12)
        c.drawString(120, 710, "Email: kapalagajameshillary@gmail.com")

        c.setFont("Helvetica-Bold", 12)
        hex_color1 = HexColor('#344767')
        hex_color2 = HexColor('#7b809a')
        c.setFillColor(hex_color1)

        time_method = datetime(date.today().year, date.today().month, date.today().day)
        day = time_method.strftime("%d")
        month = time_method.strftime("%b")
        year = time_method.strftime("%Y")
        global current_date2
        current_date2 = f'{day}-{month}-{year}'

        c.drawString(160, 670, f"BORROWER PAYMENTS INFO AS OF, {current_date2.upper()}.")

        passport = ImageReader(borrower_photo)
        c.drawImage(passport, 30, 520, width=110, height=120)
        c.setFont("Helvetica", 11)
        c.setFillColor(hex_color2)
        c.drawString(170, 640, "FULL NAME")
        c.setFillColor(hex_color1)
        c.drawString(170, 620, borrowers_data[1].upper())

        c.setFillColor(hex_color2)
        c.drawString(170, 600, "ACCESS NUMBER")
        c.setFillColor(hex_color1)
        c.drawString(170, 580, f'{borrowers_data[0]}')

        c.setFillColor(hex_color2)
        c.drawString(170, 560, "GENDER")
        c.setFillColor(hex_color1)
        c.drawString(170, 540, f'{borrowers_data[2].upper()}')

        c.setFillColor(hex_color2)
        c.drawString(170, 520, "LOAN DATE")
        c.setFillColor(hex_color1)
        c.drawString(170, 500, f'{loan_date}')

        c.setFillColor(hex_color2)
        c.drawString(400, 640, "MISSED DAYS")
        c.setFillColor(hex_color1)
        c.drawString(400, 620, f'{missed_days}')

        c.setFillColor(hex_color2)
        c.drawString(400, 600, "DAYS TO DEADLINE")
        c.setFillColor(hex_color1)
        c.drawString(400, 580, f'{remaining_days}')

        c.setFillColor(hex_color2)
        c.drawString(400, 560, "AMOUNT BORROWED")
        c.setFillColor(hex_color1)
        c.drawString(400, 540, f'{borrowers_data[4]} + INTEREST ({int(borrowers_data[4])*0.2})')

        c.setFillColor(hex_color2)
        c.drawString(400, 520, "BALANCE")
        c.setFillColor(hex_color1)
        c.drawString(400, 500, f'{borrowers_data[5]}')

        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(hex_color1)
        c.drawString(240, 480, "LOAN PAYMENTS HISTORY")

        c.setFont("Helvetica", 11)

        c.setFillColor('#44aaee')
        c.roundRect(30, 447, 550, 25, radius=0, fill=1, stroke=0)
        c.setFillColor('#ffffff')
        c.drawString(50, 455, "S/No")
        c.drawString(220, 455, "DATE")
        c.drawString(400, 455, "AMOUNT PAID (UGX)")
        c.setFillColor('#333333')

        frame_y = 420
        text_y = 430
        count = 0
        # payments_info.reverse()
        for payment in payments_info:
            bg_color = '#F7F7F7' if count % 2 == 0 else '#FFFFFF'
            c.setFillColor(bg_color)
            c.roundRect(30, frame_y, 550, 25, radius=0, fill=1, stroke=0)
            c.setFillColor('#666666')
            c.drawString(55, text_y, f'{count+1}')
            c.drawString(220, text_y, f'{payment[0]}')
            c.drawString(420, text_y, f'{payment[1]}')
            # c.drawString(250, text_y, f'{payment[3]}')
            # c.drawString(370, text_y, f'{payment[4]}')
            # c.drawString(450, text_y, f'{payment[5]}')
            # c.drawString(535, text_y, f'{payment[6]}')
            if count + 1 > 15:
                frame_y = 755
                text_y = 765
                count = 16
                c.showPage()
                for payment in payments_info[16:]:
                    bg_color = '#F7F7F7' if count % 2 == 0 else '#FFFFFF'
                    c.setFillColor(bg_color)
                    c.roundRect(30, frame_y, 550, 25, radius=0, fill=1, stroke=0)
                    c.setFillColor('#666666')
                    c.drawString(55, text_y, f'{count + 1}')
                    c.drawString(220, text_y, f'{payment[0]}')
                    c.drawString(420, text_y, f'{payment[1]}')

                    frame_y -= 25
                    text_y -= 25
                    count += 1
                break
            count += 1
            frame_y -= 25
            text_y -= 25

        c.save()

        if not directory:
            pdf_buffer_memory.seek(0)
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
                temp_pdf.write(pdf_buffer_memory.getvalue())
                temp_pdf_path = temp_pdf.name

            # Open the PDF in the default viewer
            if os.name == 'posix':
                os.system(f'xdg-open "{temp_pdf_path}"')
            elif os.name == 'nt':
                os.startfile(temp_pdf_path)
            elif os.name == 'mac':
                os.system(f'open "{temp_pdf_path}"')



