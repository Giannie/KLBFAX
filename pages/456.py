import os
from page import Page
from random import choice
import colours
from colours import colour_print
from printer import instance as printer

page_number = os.path.splitext(os.path.basename(__file__))[0]
sub_page = Page(page_number)
sub_page.title = "Annawards"
sub_page.index_num = "456-457"
content = colour_print(
    printer.text_to_ascii("Annawards", padding={"left": 6}))

awards = [
          ["Boo Cow Annawards",{"Pietro Servini":1,"Stephen Muirhead":1,"Belgin Seymenoglu":2}],
            # Tea Wrecks was formerly known as Tea Breaker
          ["Tea Wrecks Annawards",{"Anna Lambert":1,"Rafael Prieto Curiel":1,"Belgin Seymenoglu":1}],
          ["Towel Flood Annawards",{"Jigsaw":1,"Belgin Seymenoglu":2}],
          ["Worst Sorting Hat",{"Anna Lambert":20}],
          ["Boo Key",{"Anna Lambert":1,"Sam Brown":1,"Rafael Prieto Curiel":1,"Mart Wright":1}],
          ["Stolen Pen",{"Anna Lambert":1}]
         ]
pages = ["457","457","458","458","458","458"]

content += "\nWho has the most Annawards?\n\n"

for i,award in enumerate(awards):
    content += "\n"+sub_page.colours.Foreground.GREEN+award[0]+sub_page.colours.Foreground.DEFAULT+" (see page "+pages[i]+")\n"
    max_ = 0
    max_p = None
    for person,number in award[1].items():
        if number>max_:
            max_p = person
            max_ = number
        elif number==max_:
            max_p = max_p+","+person
    if max_p is not None:
        content += "  " + max_p + "\n"
sub_page.content = content

def award_show(award):
    content = colours.Foreground.GREEN+award[0]+colours.Foreground.DEFAULT+"\n"
    max_len = 0
    for person in award[1]:
        max_len = max(max_len,len(person))
    for person,number in award[1].items():
        content += person + (" "*(max_len-len(person)))
        content += sub_page.colours.Foreground.RED+"|"+sub_page.colours.Foreground.DEFAULT
        for i in range(number):
            content += choice(sub_page.colours.Foreground.non_boring)
            content += u"o_O"+sub_page.colours.Foreground.DEFAULT
        content += "\n"
    return content

def title(text):
    return colour_print(printer.text_to_ascii(text))

tea_page = Page("457")
tea_page.content = title("Tea Annawards") + "\n\n" + award_show(awards[0]) + "\n" + award_show(awards[1])
tea_page.in_index = False

other_page = Page("458")
other_page.content = title("Other Annawards") + "\n\n" + award_show(awards[2]) + "\n" + award_show(awards[3]) + "\n" + award_show(awards[4]) + "\n" + award_show(awards[5])
other_page.in_index = False
