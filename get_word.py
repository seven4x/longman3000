import PyPDF2


pdfFileObj = open('longman_3000_list.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

total_size = pdfReader.numPages

txt_file = open('words.txt', 'w')
dirty = ['S1', 'S2', 'S3', "W1", "W2", "W3",
         'S1,', 'S2,', 'S3,', "W1,", "W2,", "W3,",""]

for i in range(1, total_size):
    word_list = pdfReader.getPage(i).extractText()
    for word_line in word_list.split('\n'):
        word = word_line.split(' ')[0]
        if word in dirty:
            continue
        else:
            txt_file.write(word+"\n")
