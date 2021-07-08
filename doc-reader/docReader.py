import docx

if __name__ == '__main__':
    file = docx.Document('./b.docx')
    for f in file.paragraphs:
        if 'Heading' in f.style.name:
            i = int(f.style.name[-1:])-1
            print( i * '\t' + f.text)