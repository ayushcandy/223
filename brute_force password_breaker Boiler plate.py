import PyPDF2 as pd
filename = input('Path to the file: ')
filename = filename.strip()
file = open(filename,'rb')
pdfReader = pd.PdfFileReader(file)

tried = 0

if not pdfReader.isEncrypted:
    print('The file is not password protected! You can successfully open it!')

else :
    wordListFile=open("WordListTxt","r",errors="ignore")
    body=wordListFile.read().lower()
    words= body.split("/n")

    for i in range(len(words)):
        word=words[i]
        print("Tryind to Decode Password".format(word))
        result=pdfReader.decrypt(word)

        if result==1:
            print("Success the password is "+word)
            break

        elif result==0:
            tried+=1
            print("Password tried "+str(tried))
            
            
            Continue
                        


