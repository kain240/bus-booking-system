from page_2 import Page2
from page_3 import Page3

def page2_loop(next):
    if next == 'page2':
        d1 = Page2()
        d1.page2()
    else:
        d1 = Page3()
        d1.page3()

