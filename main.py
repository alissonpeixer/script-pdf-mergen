import os
import re
import asyncio


n_pdf_files = int(input("N file PDF: "))
print('----------------')
n_xls_files = int(input("N file XLSX: "))
print('----------------')

pdf_files, xlsx_files = [], []

bd_re = re.compile('(\d{10}\_\d{10})')
dict_re = re.compile('(PO(\_|\-|\ )\d{10})')  # DICT
po_re = re.compile('(\d{10}(\ |\-|\_)NI)')  # PO

WORKING_DIR = os.getcwd()

def mergerPdf():



    # filter files
    for file in os.listdir(WORKING_DIR):

        if not os.path.isfile(file):
            continue

        if file.lower().endswith('.pdf'):

            pdf_files.append(file)

        elif file.lower().endswith('.xlsx'):
            xlsx_files.append(file)

    if len(pdf_files) == n_pdf_files:
        if len(xlsx_files) == n_xls_files:

            invoices = {}
            bd_po = {}
            # analyze files
            for file in pdf_files:

                file_name, disc = file.split('.')

                first_file_name = file_name.split(' ')[0]

                if len(first_file_name) == 10:
                    invoices['BD'] = file
                    bd_po['bd_num'] = first_file_name
                if dict_re.findall(file):

                    invoices['DICT'] = file
                elif po_re.findall(file):

                    invoices['PO'] = file
                    bd_po['po_num'] = first_file_name

            if n_xls_files >= 1:
                # filter xlsx_files
                for xls in xlsx_files:
                    from excelConvert import excel_2_pdf
                    print('----------------')
                    print(f'Convert to Excel in Pdf')
                    print('----------------')
                    get_first_file_name = xls.split('.')
                    excel_2_pdf(os.path.join(WORKING_DIR, xls))

                    invoices['EXCEL'] = f'{get_first_file_name[0]}.pdf'

            # genPdfFile
            from PyPDF2 import PdfMerger

            print('----------------')
            print(f'Merger to files...')
            print('----------------')

            pdfs = [
                invoices['BD'],  # Fatura
                invoices['DICT'],  # Dict
                invoices['EXCEL'],
                invoices['PO']  # Po
            ]

            merger = PdfMerger()
            print('Done :D')
            for pdf in pdfs:
                merger.append(pdf)

            os.mkdir('result')
            merger.write(f'result/{bd_po["bd_num"]}_{bd_po["po_num"]}.pdf')
            merger.close()
        else:
            print(
                f'Error... XLSX files are required {n_pdf_files}! I just received {len(xlsx_files)}')
    else:
        print(
            f'Error... PDF are required {n_pdf_files}! I just received {len(pdf_files)}')


mergerPdf()
