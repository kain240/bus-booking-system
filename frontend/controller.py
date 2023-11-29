from frontend.page_2 import page2

def home_controller():
    while True:
        reopen_home = page2()
        if not reopen_home:
            break
