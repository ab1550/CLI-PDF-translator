from googletrans import Translator
import PyPDF2
import googletrans
import click

@click.command()
@click.option('--filename', prompt='source file', help='give name of non encrypted pdf file')

def doTranslate(filename):
    translator = Translator()

    pdf_file = PyPDF2.PdfReader(filename)
    text_file = open(file="output.txt", mode="w+", newline="\n")

    for page in pdf_file.pages:
        text_file.write(translator.translate(page.extract_text(), dest='gu', src='en').text)

    text_file.close()

if __name__ == '__main__':
    doTranslate()