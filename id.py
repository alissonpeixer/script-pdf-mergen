import os
import re


# Fatura
# Dict
# excel
# PO


pdf_files = []

number_re = re.compile('\d{10}')

bd_re = re.compile('(\d{10}\_\d{10})')
ft_re = re.compile('(PO(\_|\-|\ )\d{10})')
po_re = re.compile('(\d{10}(\ |\-|\_)NI)')


def mergerPdf():

    for file in os.listdir():

        if not os.path.isfile(file):
            continue

        if file.endswith('.pdf'):

            pdf_files.append(file)

        elif file.endswith('.xlsx'):
            continue

    # genPdfFile
    from PyPDF2 import PdfMerger

    bd_po = []

    for file in pdf_files:

        file_name, disc = file.split('.')

        first_file_name = file_name.split(' ')[0]

        if len(file_name) == 10:
            bd_po.append(first_file_name)

        elif len(first_file_name) == 10:
            bd_po.append(first_file_name)

    pdfs = [
        pdf_files[2],  # Fatura

        pdf_files[3],  # Dict

        pdf_files[1],  # excel

        pdf_files[0]  # PO
    ]

    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf)

    os.mkdir('result')
    merger.write('result/result.pdf')
    merger.close()


mergerPdf()
