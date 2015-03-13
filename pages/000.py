import os
from page import Page

page_number = os.path.splitext(os.path.basename(__file__))[0]
test_page = Page(page_number)
test_page.title = "Test Page"
test_page.is_enabled = False

test_page.content="""
TEST PAGE
"""
for i in range(0,len(test_page.colours.Foreground.list)):
    test_page.content+=test_page.colours.Foreground.list[i]+test_page.colours.Foreground.delist[i]+test_page.colours.Foreground.DEFAULT+"""
"""
for i in range(0,len(test_page.colours.Background.list)):
    test_page.content+=test_page.colours.Background.list[i]+test_page.colours.Background.delist[i]+test_page.colours.Background.DEFAULT+"""
"""
for i in range(0,len(test_page.colours.Style.list)):
    test_page.content+=test_page.colours.Style.list[i]+test_page.colours.Style.delist[i]+test_page.colours.Style.DEFAULT+"""
"""
