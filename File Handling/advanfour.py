#4.Merge Multiple Files
#cobine the contents of chapter1.txt, chapter2.txt, and chapter3.txt into full_book.txt.
input_files = ['chapter1.txt', 'chapter2.txt', 'chapter3.txt']
output_file = 'full_book.txt'
with open(output_file, 'w', encoding='utf-8') as outfile:
    for file in input_files:
        with open(file, 'r', encoding='utf-8') as infile:
            content = infile.read()
            outfile.write(content + '\n') 