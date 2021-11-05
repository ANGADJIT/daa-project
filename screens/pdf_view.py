import tkinter as tk
from tkPDFViewer import tkPDFViewer as pdf


class PdfView:

    # * file path
    path = ''

    # * object of pdf
    pdfObj = pdf.ShowPdf()

    def __init__(self, path: str):
        self.path = path

        self.root = tk.Tk()

        # * set dimentions of window
        self.root.geometry('600x900')

        # * add location of pdf
        self.pdfWidget = self.pdfObj.pdf_view(
            self.root, width=100, height=100, pdf_location=self.path)

        self.pdfWidget.pack()

        self.root.mainloop()  # * event loop
