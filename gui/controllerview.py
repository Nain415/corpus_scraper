from tkinter import *
import tkinter.messagebox
from main import scrapermodel

class redditButtons:

    def __init__(self, master=None, status=None):

        self.statusBar = status
        redditFrame = Frame(master)
        redditFrame.grid(row=0, columnspan=4)

        R1 = Button(redditFrame, text="UBC Subreddit", command=lambda: self.loadReddit("subreddit-UBC"))
        R2 = Button(redditFrame, text="Cornell Subreddit", command=lambda: self.loadReddit("subreddit-Cornell"))
        R3 = Button(redditFrame, text="SFU Subreddit", command=lambda: self.loadReddit("subreddit-simonfraser"))

        R1.grid(row=0,column=1)
        R2.grid(row=0,column=2)
        R3.grid(row=0,column=3)

    def loadReddit(self, name):
        if self.setWarning():
            self.statusBar.setStatus("Working...")
            Scraper.set_subreddit(name)
            self.statusBar.setReddit(name)
            self.statusBar.setStatus("OK")

    def setWarning(self):
        indexmsg = "Your index range is very large.  Loading the data set might crash your computer."
        normalmsg = "This is a computationally demanding procedure. Proceed?"

        if abs(Scraper.get_indices()[0] - Scraper.get_indices()[1]) > 5*10**5:
            return tkinter.messagebox.askyesnocancel(title="Proceed?", message=indexmsg)
        else:
            return tkinter.messagebox.askokcancel(title="Proceed?", message=normalmsg)

class indexEntries:

    def __init__(self, master=None):
        indexFrame = Frame(master)
        indexFrame.grid(row=1, columnspan=4)

        self.startVar = StringVar()
        self.startVar.set("0")
        self.startVar.trace_add("write", callback=self.callback)

        self.endVar = StringVar()
        self.endVar.set("250000")
        self.endVar.trace_add("write", callback=self.callback)

        startLabel = Label(indexFrame, text="Start Index: ")
        startIndex = Entry(indexFrame, textvariable=self.startVar)

        endLabel = Label(indexFrame, text="End Index: ")
        endIndex = Entry(indexFrame, textvariable=self.endVar)

        startLabel.grid(row=1, column=0)
        startIndex.grid(row=1, column=1)
        endLabel.grid(row=1, column=2)
        endIndex.grid(row=1, column=3)

    def getVars(self):
        return (self.startVar.get(), self.endVar.get())

    def callback(self, var, index, mode):
        Scraper.set_indices(self.getVars()[0], self.getVars()[1])


class dateEntries:

    def __init__(self, master=None):
        dates = list(range(2007, 2018 + 1))
        dateFrame = Frame(master)
        dateFrame.grid(row=2, columnspan=4)

        self.startVar = StringVar()
        self.startVar.set(dates[0])
        self.endVar = StringVar()
        self.endVar.set(dates[len(dates)-1])

        startLabel = Label(dateFrame, text="Start Date: ")
        startDate = OptionMenu(dateFrame, self.startVar, *dates, command=self.OptionMenu_SelectionEvent)
        startLabel.grid(row=2, column=0, sticky='W')
        startDate.grid(row=2, column=1)

        endLabel = Label(dateFrame, text="End Date: ")
        endDate = OptionMenu(dateFrame, self.endVar, *dates, command=self.OptionMenu_SelectionEvent)
        endLabel.grid(row=2,column=2)
        endDate.grid(row=2, column=3)

    def OptionMenu_SelectionEvent(self, event):
        Scraper.set_dates(self.getVars()[0], self.getVars()[1])

    def getVars(self):
        return (self.startVar.get(), self.endVar.get())

class searchArea:

    def __init__(self, master=None, dates=None, status=None):
        searchFrame = Frame(master)
        searchFrame.grid(row=3, columnspan=4)

        self.statusBar = status
        self.dates = dates
        self.searchVar = StringVar()

        searchLabel = Label(searchFrame, text="Regex String: ")
        searchEntry = Entry(searchFrame, textvariable=self.searchVar)

        searchLabel.grid(row=3, column=0)
        searchEntry.grid(row=3, column=1)

        searchButton = Button(searchFrame, text="Search", command=self.scrapeCorpus)
        searchButton.grid(row=3, column=2)

    def scrapeCorpus(self):
        self.setSearchVar(self.searchVar.get())
        startDate =  Scraper.get_dates()[0]
        endDate = Scraper.get_dates()[1]

        #error cases
        if startDate > endDate: tkinter.messagebox.showerror("Error", "Invalid Date Range")
        elif Scraper.get_subReddit() == "": tkinter.messagebox.showerror("Error", "No Subreddit Specified")
        else:
            self.statusBar.setStatus("Working...")
            Scraper.search_date(self.searchVar.get(), startDate, endDate)
            self.statusBar.setStatus("OK")


    def setSearchVar(self, str):
        r'{0}'.format(str) #set to raw string
        return self.searchVar.set(str)


class sampleArea:

    def __init__(self, master=None, search=None):
        self.search = search
        self.stringVarList = []
        for i in range(0,3):
            self.stringVarList.append(StringVar())
        self.stringVarList[0], self.stringVarList[1], self.stringVarList[2] = ":)", "Hello", "Jesus"
        self.sampleDict = {":)": r"\:\)", "Hello": r"(h|H)ello", "Jesus": r"(j|J)esus"}

        sampleFrame = Frame(master)
        sampleFrame.grid(row=4, columnspan=4)

        sampleLabel = Label(sampleFrame, text="Sample Expressions: ")
        sampleButton1 = Button(sampleFrame, text=self.stringVarList[0], command=lambda: self.changesearchVar(0))
        sampleButton2 = Button(sampleFrame, text=self.stringVarList[1], command=lambda: self.changesearchVar(1))
        sampleButton3 = Button(sampleFrame, text=self.stringVarList[2], command=lambda: self.changesearchVar(2))

        sampleLabel.grid(row=4,column=0, sticky=W)
        sampleButton1.grid(row=4,column=1)
        sampleButton2.grid(row=4, column=2)
        sampleButton3.grid(row=4, column=3)


    def changesearchVar(self, num):
        sampleDictKey = self.stringVarList[num]
        sampleDictVal = self.sampleDict[sampleDictKey]

        self.search.setSearchVar(sampleDictVal)




class StatusBar:

    def __init__(self, master=None):

        self.redditStr = StringVar()
        self.redditStr.set("Selected - ")

        self.statusStr = StringVar()
        self.statusStr.set("Status: OK")

        self.redditText = Label(master, textvariable=self.redditStr, relief=GROOVE)
        self.redditText.grid(row=6, column=0, sticky=SW)
        self.statusText = Label(master, textvariable=self.statusStr, relief=GROOVE)
        self.statusText.grid(row=5, column=0, sticky=SW)

        creditText1 = Label(master, text="Made by Nain415")
        creditText1.grid(row=5, column=3, sticky='SE')
        creditText2 = Label(master, text="UBC Vancouver 2021")
        creditText2.grid(row=6, column=3, sticky='SE')

    def setReddit(self, str):
        self.redditStr.set("Selected: " + str)
        self.redditText.update()

    def setStatus(self, str):
        self.statusStr.set("Status: " + str)
        self.statusText.update()


def main():
    root = Tk()
    root.resizable(False, False)
    root.geometry("500x200")

    root.title('Mini Reddit Corpus Scraper')
    root.rowconfigure(5, weight=1)  # sets row 5 to be the bottom right
    root.columnconfigure(3, weight=1)


    global Scraper
    Scraper = scrapermodel.Scraper()

    statusBar = StatusBar(root)
    selectionParams1 = indexEntries(root)
    selectionParams2 = dateEntries(root)
    searchBar = searchArea(root, dates=selectionParams1, status=statusBar)
    selectionBar = redditButtons(root, statusBar)
    searchBarDemo = sampleArea(root, searchBar)




    root.mainloop()

if __name__ == '__main__':
    main()
