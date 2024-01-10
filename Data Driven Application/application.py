from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import json
root = Tk()
root.title("Tree of Words")
root.geometry("350x190")
style = ttk.Style()
style.theme_use('default')
style.configure('lefttab.TNotebook', tabposition='wn')
style.configure('TNotebook.Tab', background="lightblue", width=10)
style.map("TNotebook.Tab", background= [("selected", "white")])

def dictionary():
    #Change width of window
    root.state('zoomed')
    #Show The Main Frame
    output.pack(fill=BOTH, padx=150, pady=(30,40))

    #Input the word into the titles in the main frames
    word = SearchedWord.get().title()
    definitionWord["text"] = word
    antonymWord["text"] = word
    synonymWord["text"] = word
    rhymeWord["text"] = word
    examplesWord["text"] = word

    #PRONUNCIATION
    pronunciationUrl = "https://wordsapiv1.p.rapidapi.com/words/" + word +"/pronunciation"
    pronunciationheaders = {
        "X-RapidAPI-Key": "76e3ad0f56msh28639798b27e362p1da4e9jsn98406c16dddb",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }
    api_pronunciation = requests.get(pronunciationUrl, headers=pronunciationheaders)
    pronounce = json.loads(api_pronunciation.text)
    pronunciation["text"] = f"[ {pronounce['pronunciation']['all']} ]"

    #DEFINITION
    defineURL = "https://wordsapiv1.p.rapidapi.com/words/" + word + "/definitions"
    defineheaders = {
        "X-RapidAPI-Key": "76e3ad0f56msh28639798b27e362p1da4e9jsn98406c16dddb",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }
    api_definition = requests.request("GET", defineURL, headers=defineheaders)
    meaning = json.loads(api_definition.text)
    definelist=[]
    string = ""
    i=1
    for x in meaning["definitions"]:
        definitionMeaning = f"{i} {x['definition']}\n"
        definelist.append(definitionMeaning)
        i = i+1
    for x in definelist[0:10]:
        string = f"{string} {x}"
    meaningLabel["text"] = string

    #ANTONYMS
    antonymUrl = "https://wordsapiv1.p.rapidapi.com/words/" + word + "/antonyms"
    antonymheaders = {
        "X-RapidAPI-Key": "76e3ad0f56msh28639798b27e362p1da4e9jsn98406c16dddb",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }
    api_antonyms = requests.get(antonymUrl, headers=antonymheaders)
    opposite = json.loads(api_antonyms.text)
    oppositeList = []
    ostring = ""
    for x in opposite["antonyms"]:
        antonyms = f"• {x}\n"
        oppositeList.append(antonyms)
    if len(oppositeList) == 0:
        ostring = "No Input"
    else:
        for x in oppositeList[0:10]:
            ostring = f"{ostring} {x}"
    antonymLabel["text"] = ostring

    #SYNONYMS
    synonymsUrl = "https://wordsapiv1.p.rapidapi.com/words/" + word + "/synonyms"
    synonymheaders = {
        "X-RapidAPI-Key": "76e3ad0f56msh28639798b27e362p1da4e9jsn98406c16dddb",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }
    api_synonyms = requests.get(synonymsUrl, headers=synonymheaders)
    similar = json.loads(api_synonyms.text)
    similarList = []
    sstring = ""
    for x in similar["synonyms"]:
        synonyms = f"• {x}\n"
        similarList.append(synonyms)
    if len(similarList) == 0:
        sstring = "No Input"
    else:
        for x in similarList[0:10]:
            sstring = f"{sstring} {x}"
    synonymLabel["text"] = sstring
    
    #RHYMES
    rhymeUrl = "https://wordsapiv1.p.rapidapi.com/words/" + word + "/rhymes"
    rhymeheaders = {
        "X-RapidAPI-Key": "76e3ad0f56msh28639798b27e362p1da4e9jsn98406c16dddb",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }
    api_rhyme = requests.get(rhymeUrl, headers=rhymeheaders)
    rhyme = json.loads(api_rhyme.text)
    rhymelist=[]
    rstring1 = ""
    rstring2 = ""
    for x in rhyme["rhymes"]["all"]:
        rhymes = f"• {x}\n"
        rhymelist.append(rhymes)
    if len(rhymelist) == 0:
        rstring1 = "No Input"
    elif len(rhymelist) < 11:
        rhymeLabel1["width"] = 120
        rhymeLabel1.grid(row=1, column=1)
        for x in rhymelist[0:9]:
            rstring1 = f"\n{rstring1} {x}"
    else:
        rhymeLabel1.grid(row=1, column=1, padx=5)
        rhymeLabel2.grid(row=1, column=2)
        for x in rhymelist[0:9]:
            rstring1 = f"\n{rstring1} {x}"
        for x in rhymelist[10:19]:
            rstring2 = f"\n{rstring2} {x}"
    rhymeLabel1["text"] = rstring1
    rhymeLabel2["text"] = rstring2

    #EXAMPLES
    exampleurl = "https://wordsapiv1.p.rapidapi.com/words/" + word + "/examples"
    exampleheaders = {
        "X-RapidAPI-Key": "76e3ad0f56msh28639798b27e362p1da4e9jsn98406c16dddb",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }
    api_example = requests.get(exampleurl, headers=exampleheaders)
    examples = json.loads(api_example.text)
    examplelist=[]
    estring = ""
    i=1
    for x in examples["examples"]:
        example = f"{i} {x}\n"
        examplelist.append(example)
        i = i+1
    for x in examplelist[0:10]:
        estring = f"{estring} {x}"
    exampleLabel["text"] = estring

#HEADER
bg = Frame(root, bg="lightblue")
bg.pack(fill=X)
heading = Frame(bg, bg="lightblue")
heading.pack(side=TOP)
photo = Image.open("logo.png")
img = ImageTk.PhotoImage(photo.resize((60,40)))
logo = Label(heading, image=img, bg="lightblue")
logo.grid(row=1, column=1, pady=10, padx=5)
title = Label(heading, text="TREE OF WORDS", bg="lightblue", font=("PMingLiU-ExtB", 20, "bold"))
title.grid(row=1, column=2)

#SEARCH
searchLabel = Label(root, text="Enter the Word to Search", font=("Times New Roman CE", 11))
searchLabel.pack(pady=(20,0))
search = Frame(root)
search.pack()
SearchedWord = StringVar()
WordEntry = Entry(search, width=20, textvariable = SearchedWord, relief=SOLID, font=("Times New Roman", 14))
WordEntry.grid(row=1, column=1)
button = Button(search, width=10, relief=SOLID, bd=1, text="SEARCH", bg="lightblue", fg="white", font=("Times New Roman CE", 10), command=dictionary)
button.grid(row=1, column=2, pady=5, padx=1)


#MAIN FRAME 
output = Frame(root, bd=0, highlightthickness=5, highlightcolor="#c1cbda", highlightbackground="#c1cbda")
notebook = ttk.Notebook(output, style='lefttab.TNotebook')
notebook.pack(expand=TRUE, fill=BOTH)
#Definition
definition = Frame(notebook)
definition.pack()
definitionSubtitle = Label(definition, text="DEFINITION", font=("Kozuka Gothic Pr6N R", 10, "bold"))
definitionSubtitle.pack(side=TOP, anchor=W, padx=15, pady=(10,6))
definitionWord = Label(definition, text="WORD", font=("Times New Roman", 35))
definitionWord.pack(side=TOP, anchor=W, padx=20)
pronunciation = Label(definition, width=22, text="[ pro - nun - cia - tion ]", font=("Times New Roman", 13))
pronunciation.pack(anchor=W, padx=6)
line = Canvas(definition, width=960, height=6)
line.pack(side=TOP, padx=16, pady=(5,10))
line.create_line(0,6,1000,6, fill="lightblue", width=3)
meaningLabel = Label(definition, relief=GROOVE, bd=3, text="name\ntype\nfriends", width=140, height=18, font=("Times New Roman", 13), anchor=NW, justify=LEFT)
meaningLabel.pack(padx=18, pady=(10,40))
notebook.add(definition, text="Definition")
#Antonyms
antonyms = Frame(notebook)
antonyms.pack()
antonymsSubtitle = Label(antonyms, text="ANTONYMS OF", font=("Kozuka Gothic Pr6N R", 12, "bold"))
antonymsSubtitle.pack(side=TOP, padx=15, pady=(15,6))
antonymWord = Label(antonyms, text="", font=("Times New Roman", 30), width=10, height=1, relief=SOLID, bg="lightblue")
antonymWord.pack(side=TOP)
line2 = Canvas(antonyms, width=960, height=6)
line2.pack(side=TOP, padx=16, pady=(15,10))
line2.create_line(0,6,1000,6, fill="lightblue", width=3)
antonymLabel = Label(antonyms, relief=GROOVE, bd=3, text="", width=140, height=18, font=("Times New Roman", 13), anchor=NW, justify=LEFT)
antonymLabel.pack(padx=18, pady=(10,40))
notebook.add(antonyms, text="Antonyms")
#Synonyms
synonyms = Frame(notebook)
synonyms.pack()
synonymsSubtitle = Label(synonyms, text="SYNONYMS OF", font=("Kozuka Gothic Pr6N R", 12, "bold"))
synonymsSubtitle.pack(side=TOP, padx=15, pady=(15,6))
synonymWord = Label(synonyms, text="", font=("Times New Roman", 30), width=10, height=1, relief=SOLID, bg="lightblue")
synonymWord.pack(side=TOP)
line3 = Canvas(synonyms, width=960, height=6)
line3.pack(side=TOP, padx=16, pady=(15,10))
line3.create_line(0,6,1000,6, fill="lightblue", width=3)
synonymLabel = Label(synonyms, relief=GROOVE, bd=3, text="", width=140, height=18, font=("Times New Roman", 13), anchor=NW, justify=LEFT)
synonymLabel.pack(padx=18, pady=(10,40))
notebook.add(synonyms, text="Synonyms")
#Rhymes
rhymes = Frame(notebook)
rhymes.pack()
rhymeSubtitle = Label(rhymes, text="RHYMES OF", font=("Kozuka Gothic Pr6N R", 12, "bold"))
rhymeSubtitle.pack(side=TOP, padx=15, pady=(15,6))
rhymeWord = Label(rhymes, text="", font=("Times New Roman", 30), width=10, height=1, relief=SOLID, bg="lightblue")
rhymeWord.pack(side=TOP)
line4 = Canvas(rhymes, width=960, height=6)
line4.pack(side=TOP, padx=16, pady=(15,10))
line4.create_line(0,6,1000,6, fill="lightblue", width=3)
rhymeFrame = Frame(rhymes)
rhymeFrame.pack(pady=(10,40))
rhymeLabel1 = Label(rhymeFrame, relief=GROOVE, bd=3, text="", width=60, height=18, font=("Times New Roman", 13), anchor=NW, justify=LEFT)
rhymeLabel2 = Label(rhymeFrame, relief=GROOVE, bd=3, text="", width=60, height=18, font=("Times New Roman", 13), anchor=NW, justify=LEFT)
notebook.add(rhymes, text="Rhymes")
#Examples
examples = Frame(notebook)
examples.pack()
examplesSubtitle = Label(examples, text="EXAMPLES OF", font=("Kozuka Gothic Pr6N R", 10, "bold"))
examplesSubtitle.pack(side=TOP, anchor=W, padx=15, pady=(10,6))
examplesWord = Label(examples, text="", font=("Times New Roman", 35), relief=SOLID, bg="lightblue", width=10)
examplesWord.pack(side=TOP, anchor=W, padx=20)
line5 = Canvas(examples, width=960, height=6)
line5.pack(side=TOP, padx=16, pady=(15,10))
line5.create_line(0,6,1000,6, fill="lightblue", width=3)
exampleLabel = Label(examples, relief=GROOVE, bd=3, text="", width=140, height=18, font=("Times New Roman", 13), anchor=NW, justify=LEFT)
exampleLabel.pack(padx=18, pady=(10,40))
notebook.add(examples, text="Examples")

root.mainloop()
