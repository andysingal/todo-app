contents = ["i love you","you are amazing","shanu love me "]
filenames = ["doc.txt","report.txt","presentation.txt"]

for content,filename in zip(contents,filenames):
    file = open(f"../file/{filename}",'w')
    file.write(content)
    file.close()