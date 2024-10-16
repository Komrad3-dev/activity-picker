let options : string[] = []
basic.forever(function on_forever() {
    
    options = ["clean", "homework", "game", "eat", "sleep", "work", "drive"]
    if (input.isGesture(Gesture.Shake)) {
        basic.showString("" + options[randint(0, 5)])
        basic.clearScreen()
    }
    
})
