options: List[str] = []

def on_forever():
    global options
    options = ["clean", "homework", "game", "eat", "sleep", "work", "drive"]
    if input.is_gesture(Gesture.SHAKE):
        basic.show_string("" + (options[randint(0, 5)]))
        basic.clear_screen()
basic.forever(on_forever)
