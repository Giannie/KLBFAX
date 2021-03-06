import os
import json
from re import sub
from page import Page
from colours import colour_print
from colours import Foreground
from printer import instance as printer
from time import strftime

def strip_tags(string):
    return sub(r'<[^>]*?>', '', string)

class BusPage(Page):
    def __init__(self, page_num, bus_num, station, code):
        super(BusPage, self).__init__(page_num)
        self.title = station+" ("+code+") Buses"
        self.tagline = "Live buses from "+station+" ("+code+"). Data from TfL."
        self.in_index = False
        self.station = station
        self.code = code
        self.bus_num = bus_num
        pages.append([page_num,station+" ("+code+")"])

    def generate_content(self):
        import urllib2
        content = colour_print(printer.text_to_ascii("BUSES",fill=False))+self.colours.Foreground.YELLOW+self.colours.Background.BLUE+" from "+self.station+" ("+self.code+")"+self.colours.Foreground.DEFAULT+self.colours.Background.DEFAULT

        content += self.colours.Foreground.GREEN+"\nTime   Num Destination"+self.colours.Foreground.DEFAULT
        response = urllib2.urlopen("http://countdown.tfl.gov.uk/stopBoard/"+self.bus_num)
        j = response.read()
        bus_times = json.loads(j)
        for bus in bus_times['arrivals']:
            content += "\n"
            wait = bus['estimatedWait']
            content += self.colours.Foreground.GREEN+wait+self.colours.Foreground.DEFAULT
            content += " "*(6-len(wait))
            content += " "+self.colours.Foreground.RED+bus['routeId']+self.colours.Foreground.DEFAULT
            content += " "*(4-len(bus['routeId']))
            content += bus['destination']
        self.content = content

pages=[]
bus01 = BusPage("801","57596","Gower Street / UCH","N")
bus02 = BusPage("802","50975","Euston Square Station","P")
bus03 = BusPage("803","51664","Euston Station","H")
bus04 = BusPage("804","75100","Euston Station","AZ")
bus05 = BusPage("805","73933","Euston Station","C")
bus06 = BusPage("806","53602","Euston Bus Station","AP")
bus07 = BusPage("807","56230",Foreground.GREEN+"Euston Station"+Foreground.DEFAULT,"D")
bus08 = BusPage("808","47118","Euston Bus Station","G")
bus09 = BusPage("809","58234","Euston Station","E")
bus10 = BusPage("810","51581","Upper Woburn Place / Euston Road","L")
bus11 = BusPage("811","72926","Upper Woburn Place","M")
bus12 = BusPage("812","72238","Jubilee Road","PD")
bus13 = BusPage("813","58812","Jubilee Road","J")
bus14 = BusPage("814","55027","Wembley Park Station","O")
bus15 = BusPage("815","59287",Foreground.GREEN+"Euston Square Station"+Foreground.DEFAULT,"Q")

tv_page = Page("800")
tv_page.content = colour_print(printer.text_to_ascii("Buses Index"))+"\n"
tv_page.title = "Buses Index"
i=0
for page in pages:
    tv_page.content+=tv_page.colours.Foreground.RED+page[0]+tv_page.colours.Foreground.DEFAULT+" "+page[1]
    if i==1:
        tv_page.content += "\n"
    else:
        tv_page.content += " "*(38-len(page[0]+page[1]))
    i = 1-i
