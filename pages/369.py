from page import Page
from printer import instance as printer
import datetime

class OllyPage(Page):
    def __init__(self, page_num,who,when,numb=False):
        super(OllyPage, self).__init__(page_num)
        self.title = "Countdowns"
        self.who = who
        self.when = when
        if numb==False:
            self.in_index = False
        else:
            self.in_index = True
            self.index_num = numb
            

    def generate_content(self):
        delta = self.when - datetime.datetime.now()
        hs = delta.seconds/3600
        ds = delta.days
        if ds > 0:
    
            left = str(ds) + " day"
            left2 = str(hs) + " hour"
            if ds!=1: left += "s"
            if hs!=1: left2 += "s"
            content = self.colours.colour_print(printer.text_to_ascii(self.who+" Leaves In"),foreground=self.colours.Foreground.GREEN+self.colours.Style.BOLD,background=self.colours.Background.BLACK)
            content += "\n\n"
            content += self.colours.colour_print(printer.text_to_ascii(left),foreground=self.colours.Foreground.MAGENTA+self.colours.Style.BOLD,background=self.colours.Background.BLACK)
            content += "\n\n"
            content += self.colours.colour_print(printer.text_to_ascii(left2),foreground=self.colours.Foreground.WHITE+self.colours.Style.BOLD,background=self.colours.Background.BLUE)
            self.content = content
        else:
            delta = datetime.datetime.now() - self.when
            hs = delta.seconds/3600
            ds = delta.days

            left = str(ds) + " day"
            left2 = str(hs) + " hour"
            if ds!=1: left += "s"
            if hs!=1: left2 += "s"
            content = self.colours.colour_print(printer.text_to_ascii(self.who+" Left"),foreground=self.colours.Foreground.GREEN+self.colours.Style.BOLD,background=self.colours.Background.BLACK)
            content += "\n"
            content += self.colours.colour_print(printer.text_to_ascii(left),foreground=self.colours.Foreground.MAGENTA+self.colours.Style.BOLD,background=self.colours.Background.BLACK)
            content += "\n"
            content += self.colours.colour_print(printer.text_to_ascii(left2),foreground=self.colours.Foreground.WHITE+self.colours.Style.BOLD,background=self.colours.Background.BLUE)
            content += "\n"
            content += self.colours.colour_print(printer.text_to_ascii("Ago"),foreground=self.colours.Foreground.GREEN+self.colours.Style.BOLD,background=self.colours.Background.BLACK)
            self.content = content

j_page = OllyPage("368","Jigsaw",datetime.datetime(2016, 3, 24, 17, 0),"368-370")
o_page = OllyPage("369","Olly",datetime.datetime(2016, 3, 24, 17, 0))
b_page = OllyPage("370","Belgin",datetime.datetime(2018, 8, 31, 16, 0))

