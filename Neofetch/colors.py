"""
Bright Black: \u001b[30;1m
Bright Red: \u001b[31;1m
Bright Green: \u001b[32;1m
Bright Yellow: \u001b[33;1m
Bright Blue: \u001b[34;1m
Bright Magenta: \u001b[35;1m
Bright Cyan: \u001b[36;1m
Bright White: \u001b[37;1m
Reset: \u001b[0m
"""
def reset():
    print(u"\u001b[0m")
def red(txt):
    print(u"\u001b[31;1m"+txt)
def green(txt):
    print(u"\u001b[32;1m"+txt)
def yellow(txt):
    print(u"\u001b[33;1m"+txt)
def blue(txt):
    print(u"\u001b[34;1m"+txt)
def cyan(txt):
    print(u"\u001b[35;1m"+txt)
def magenta(txt):
    print( u"\u001b[36;1m"+txt)
def white(txt):
    print(u"\u001b[37;1m"+txt)