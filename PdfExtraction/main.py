import PyPDF2

a = PyPDF2.PdfFileReader('android_tutorial.pdf')

# print(a.documentInfo)  # print document information
# print(a.getNumPages())  # print the number of pages in the pdf
# print(a.getPage(2).extractText())  # extract the text of page 2

# now i want to read the pdf file from page number 1 to page 10 and writing its content in a txt file

content = ''
for i in range(1, 11):
    content += a.getPage(i).extractText()

with open('text.txt', 'w', encoding='utf-8') as f:
    f.write(content)



