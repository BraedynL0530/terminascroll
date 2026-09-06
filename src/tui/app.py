from textual.app import App,ComposeResult
from textual.containers import HorizontalScroll,VerticalScroll # dunnow what to do yet

class Videos():
    pass #tbd

class TuiApp(App):
    BINDINGS = [("q", "quit", "Quit"),("d","cursor_right","->"),("a","cursor_left","<-"),
                ("j","cursor_down","Down"),("k","cursor_up","Up"),("i","toggle_input","Type Command"),]
    pass