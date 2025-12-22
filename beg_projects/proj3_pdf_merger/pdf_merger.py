from pypdf import PdfWriter

merger = PdfWriter()

pdfs=[]
n = int(input("Enter the number of pdfs to merge: "))
for i in range(0,n):
    name=input(f"Enter {i+1} pdf name: ")
    pdfs.append(name)
    

for pdf in pdfs:
    merger.append(pdf)

merger.write("final_merged.pdf")