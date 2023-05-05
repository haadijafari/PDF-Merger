from PyPDF4 import PdfFileMerger
import os
import argparse


def merge_pdfs(input_files: list, page_range: tuple, output_file: str, bookmark: bool = True):
    # strict = False -> To ignore PdfReadError - Illegal Character error
    merger = PdfFileMerger(strict=False)
    for input_file in input_files:
        bookmark_name = os.path.splitext(os.path.basename(input_file))[
            0] if bookmark else None
        # pages To control which pages are appended from a particular file.
        merger.append(fileobj=open(input_file, 'rb'), pages=page_range,
                      import_bookmarks=False, bookmark=bookmark_name)
    # Insert the pdf at specific page
    merger.write(fileobj=open(output_file, 'wb'))
    merger.close()


merge_pdfs([f'pdf-files/{i}.pdf' for i in range(1, 11)],
           None, 'Merged.pdf', False)
