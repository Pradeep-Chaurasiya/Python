from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage

from io import StringIO
import os


# to extract text from pdf files
def get_pdf_file_content(path_to_pdf):
    resouce_manager = PDFResourceManager(caching=True)
    out_text = StringIO()
    laParams = LAParams()
    text_converter = TextConverter(resouce_manager,out_text,laparams=laParams)

    fp = open(path_to_pdf,'rb')
    interpreter = PDFPageInterpreter(resouce_manager, text_converter)

    for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0,password='',caching=True,check_extractable=True):
        interpreter.process_page(page)
    text = out_text.getvalue()
    # closing the objects
    fp.close()
    text_converter.close()
    out_text.close()

    return text

path = input("Enter your Source path : ")

for file in os.listdir(path):
    if file.endswith('.pdf'):
        print('pdf file name is : ' ,file)
        path_to_pdf = f'{path}/{file}'
        print(get_pdf_file_content(path_to_pdf))


# copy the file in text directory
def convert_To_Text(path, txtDir):
    # if path == "": path = os.getcwd() + "\\" #if no pdfDir passed in
    for pdf in os.listdir(path): #iterate through pdfs in pdf directory
        file_name_without_extension = pdf.split(".")[0]
        if pdf.endswith('.pdf'):
            print('pdf file name is : ', pdf)
            path_to_pdf = f'{path}/{pdf}'
            newtext = get_pdf_file_content(path_to_pdf) #get string of text content of pdf
            textFilename = txtDir+'/'+file_name_without_extension+".txt"
            textFile = open(textFilename, "w") #make text file
            textFile.write(newtext) #write text to text file
			#textFile.close

txtDir = input('Enter text Directory : ')
folder_exist = os.path.isdir(txtDir)
if folder_exist == True:
    print(txtDir,' : This destination path exist ')
else :
    print('This Path does not exist so Create txtDir ')
    os.mkdir(txtDir)
convert_To_Text(path,txtDir)