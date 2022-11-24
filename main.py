import os
import re

# Fatura
# Dict
# excel
# PO

pdf_files, xlsx_files = [], []

bd_re = re.compile('(\d{10}\_\d{10})')
dict_re = re.compile('(PO(\_|\-|\ )\d{10})')  # DICT
po_re = re.compile('(\d{10}(\ |\-|\_)NI)')  # PO


def mergerPdf():

    invoices = {}

    # filter files
    for file in os.listdir():

        if not os.path.isfile(file):
            continue

        if file.endswith('.pdf'):

            pdf_files.append(file)

        elif file.endswith('.xlsx'):
            xlsx_files.append(file)
    # analyze files
    for file in pdf_files:

        file_name, disc = file.split('.')

        first_file_name = file_name.split(' ')[0]

        if len(first_file_name) == 10:
            invoices['BD'] = file

        if dict_re.findall(file):
            invoices['DICT'] = file
        elif po_re.findall(file):
            invoices['PO'] = file
    # filter xlsx_files
    for xls in xlsx_files:

        from excelConvert import excel_2_pdf

        get_first_file_name = xls.split('.')
        excel_2_pdf(xls)

        invoices['EXCEL'] = f'{get_first_file_name[0]}.pdf'
    # genPdfFile
    from PyPDF2 import PdfMerger

    pdfs = [
        invoices['BD'],  # Fatura
        invoices['DICT'],  # Dict
        invoices['EXCEL'],
        invoices['PO']  # Po
    ]

    merger = PdfMerger()

    print(f'Merger to files...')
    for pdf in pdfs:
        merger.append(pdf)

    os.mkdir('result')
    merger.write('result/result.pdf')
    merger.close()


mergerPdf()
