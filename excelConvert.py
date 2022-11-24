import os
from win32com import client


def excel_2_pdf(file_path):
    file_name, _ = os.path.splitext(file_path)

    xl = client.Dispatch("Excel.Application")
    xl.Visible = False
    xl.EnableEvents = False
    xl.DisplayAlerts = False

    wb = xl.Workbooks.Open(file_path)

    ws = wb.Worksheets("Hoja3")
    ws.PageSetup.Orientation = 2  # xlLandscape
    ws.PageSetup.Zoom = False
    ws.PageSetup.FitToPagesWide = 1
    ws.PageSetup.FitToPagesTall = 1

    # https://learn.microsoft.com/pt-br/office/vba/api/excel.worksheet.exportasfixedformat
    ws.ExportAsFixedFormat(
        0,  # Type:=xlTypePDF
        f"{file_name}.pdf",  # Filename
        0  # Quality:=xlQualityStandard
    )

    wb.Close(False)
