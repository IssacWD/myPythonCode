from tkinter import *
root=Tk()
root.geometry('500x600+150+200')
root.title('TOEFL Vocabulary GUI')


    
def WordListToString(wordList):
    wordString=''
    if len(wordList)<=1:
        wordString=''.join(wordList)
    else:
        for i in range(len(wordList)-1):
            wordString=wordString+wordList[i]+'\n'
        wordString=wordString+wordList[len(wordList)-1]
    return wordString

        
def PressShowMeaning():
    #global vocabDatabase, wordEntry
    #global wordLabel1,meaningLabel1,sampleLabel1, synLabel1,antLabel1
    #The above global variables does not need to be declared, as they are not assigned, but only referenced in this function.
    
    meaning=wordEntry[1].lower()
    sample=wordEntry[2].lower()
    syns=wordEntry[3]
    ants=wordEntry[4]
    meaningLabel1.configure(text=meaning)
    sampleLabel1.configure(text=sample)
    synLabel1.configure(text=WordListToString(syns))
    antLabel1.configure(text=WordListToString(ants))

import pickle
file = open('vocabDatabaseFile.pkl', 'rb')
vocabDatabase= pickle.load(file)
file.close()

def PressNextWord():
    global wordIndex, wordEntry # These global variables are assigned in this function, and thus need to be declared.
    wordIndex+=1
    wordEntry=vocabDatabase[wordIndex]
    word=wordEntry[0].lower()
    meaning=''
    sample=''
    syns=''
    ants=''
    wordLabel1.configure(text=word)
    meaningLabel1.configure(text=meaning)
    sampleLabel1.configure(text=sample)
    synLabel1.configure(text=WordListToString(syns))
    antLabel1.configure(text=WordListToString(ants))
    
    




wordLabel0=Label(root,text='Word:', height=2)
wordLabel0.grid(row=0,column=0)
wordLabel1=Label(root,width=30,height=2)
wordLabel1.grid(row=0,column=1)

meaningLabel0=Label(root,text='Meaning:', height=3)
meaningLabel0.grid(row=1,column=0)
meaningLabel1=Label(root,height=3)
meaningLabel1.grid(row=1,column=1)

sampleLabel0=Label(root,text='Sample:', height=3)
sampleLabel0.grid(row=2,column=0)
sampleLabel1=Label(root, height=3)
sampleLabel1.grid(row=2,column=1)

synLabel0=Label(root,text='Synonyms:',  height=8)
synLabel0.grid(row=3,column=0)
synLabel1=Label(root, height=8 )
synLabel1.grid(row=3,column=1)

antLabel0=Label(root,text='Antonyms:', height=6)
antLabel0.grid(row=4,column=0)
antLabel1=Label(root, height=8)
antLabel1.grid(row=4,column=1)


showMeaningButton=Button(root, text="Show meaning...", command=PressShowMeaning)
showMeaningButton.grid(row=5,column=0)
nextWordButton=Button(root, text="Next word", command=PressNextWord)
nextWordButton.grid(row=5,column=1)

wordEntry=[] #Global variable
wordIndex=-1 #Global variable

root.mainloop()



