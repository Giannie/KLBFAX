import os
import screen
from page import Page

page_number = os.path.splitext(os.path.basename(__file__))[0]
test_page = Page(page_number)
test_page.title = "Test Page"
test_page.is_enabled = False

test_page.content="\nTEST PAGE\n"

j = 0
for i in range(1000,10000):
    test_page.content += str(i)+" "+unichr(i)
    j += 1
    if j % 9 != 0: test_page.content += "  "
    else: test_page.content += "\n"

printed=0
for i in range(0,len(test_page.colours.Foreground.list)):
    test_page.content+=test_page.colours.Foreground.list[i]+test_page.colours.Foreground.delist[i]+test_page.colours.Foreground.DEFAULT
    printed+=1
    if printed%3==0: test_page.content+="\n"
    else: test_page.content+=" "
for i in range(0,len(test_page.colours.Background.list)):
    test_page.content+=test_page.colours.Background.list[i]+test_page.colours.Background.delist[i]+test_page.colours.Background.DEFAULT
    printed+=1
    if printed%3==0: test_page.content+="\n"
    else: test_page.content+=" "
for i in range(0,len(test_page.colours.Style.list)):
    test_page.content+=test_page.colours.Style.list[i]+test_page.colours.Style.delist[i]+test_page.colours.Style.DEFAULT
    printed+=1
    if printed%3==0: test_page.content+="\n"
    else: test_page.content+=" "

