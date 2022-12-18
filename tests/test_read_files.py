import os
import zipfile
from zip_func import create_arch, delete_arch
import PyPDF2

path_files = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir, 'files')
path_resources = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir, 'resources')
zip_archive = os.path.join(path_resources, 'archive.zip')


def test_read_pdf():
    delete_arch(zip_archive)
    create_arch(path_files, zip_archive)
    with zipfile.ZipFile(zip_archive) as zp:
        pdf_file = zp.extract('rekomend.pdf')
        reader = PyPDF2.PdfReader(pdf_file)
        pages = reader.pages[0]
        text = pages.extract_text()
        assert 'Выдержка  из  " Методических  рекомендаций ..."' in text
    os.remove('rekomend.pdf')



