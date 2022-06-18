# Mini Reddit Corpus Scraper
<p align="center">
<img src=https://user-images.githubusercontent.com/78244259/174459056-5669b65e-40b9-44c5-b6bb-227a41590342.png>

</p>

## Sample Output (search for the string "handsome" in R/UBC from 2007-2018)
<p align="left">
<img src=https://user-images.githubusercontent.com/78244259/116946614-73bae280-ac2f-11eb-9e45-c23ce137094b.png>
</p>

There don't seem to be too many handsome people at UBC :(

##### Function
Produces an excel spreadsheet with results from Pushshift.io's collection of Reddit corpuses, given a regular expression pattern and subreddit name.  I've limited this program to R/UBC, R/Cornell and R/Simonfraser.  Utterances are loaded in segments defined by the user because of computational resource limitations (the 650,000 and 1,000,000 in the image).

##### Purpose
I created this for a group project in an English Grammar course at UBC (ENGL 321, taught by Dr. Elise Stickles), where we were investigating modern usages of some English expressions.   A gui was necessary for it to be user-friendly.  The corpuses provided to the class weren't up to date with the latest modern expressions: particularly, my group had selected to investigate the usage of emoji expressions in English utterances, so a very modern corpus was necessary.  The group desired Excel spreadsheet outputs because of the various data-analysis functions that Excel supports.

##### Usage Note 
Any index shifts will require loading a new corpus instance.  Therefore, if I had loaded utterances 0 through 100,000, then to load the next 500,000 utterances of the corpus, I would have to change Start Index to 100,001 and End Index to 600,001, and then select the corpus on the top bar.

Python's Regex Syntax: https://docs.python.org/3/library/re.html

##### Requirements
(1) A python interpreter installed.
(2) A modern computer to load in reasonably-sized datasets.

##### Construction Remarks
For this project, I spent some time learning Python's built-in Tkinter gui-building library.  The rest was the application of previously learned knowledge (aside from importing and using the excel-constructing and corpus-scraping libraries).  I also found it valuable to have a proper IDE for Python because of the suggestions one provides for different function/method calls; I needed this because of the new libraries I was working with.  Therefore, I installed and began using VSC.  VSC's built-in Git support also turned out to be very handy, and reduced the time I spent at the command line.

I hadn't delved much into object-oriented programming in Python before this project.  Prior to this, I'd only dealt with classes in the context of Java and C++ during the UBC courses CPSC 210 (Software Construction) and CPSC 221 (Basic Algorithms and Data Structures) respectively.  Additionally, because the program was built out of an immediate need, the code might not be the prettiest, but I've endeavoured to make it somewhat maintainable.
