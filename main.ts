let rij = 0
let kol = 0
let getal = 0
input.onButtonPressed(Button.A, function () {
    basic.showNumber(randint(1, 6))
    music.play(music.stringPlayable("C D E F G A B C5 ", 120), music.PlaybackMode.UntilDone)
})
input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
    for (let index = 0; index <= 0; index++) {
        basic.clearScreen()
        Toongetal(24 - index)
        serial.writeValue("getal", index)
        serial.writeString("")
        serial.writeValue("x", rij)
        serial.writeString("")
        serial.writeValue("y", kol)
        serial.writeLine("")
        basic.pause(500)
    }
    basic.clearScreen()
    for (let index2 = 0; index2 <= 4; index2++) {
        for (let index = 0; index <= 4; index++) {
            led.plot(index, 4 - index2)
            basic.pause(500)
        }
    }
})
input.onButtonPressed(Button.AB, function () {
    getal = randint(1, 3)
    if (getal == 1) {
        basic.showIcon(IconNames.Square)
    } else if (getal == 2) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    } else {
        basic.showLeds(`
            . . . # #
            # . # . .
            . # . . .
            # . # . .
            . . . # #
            `)
    }
})
input.onButtonPressed(Button.B, function () {
    getal = 5
    for (let index = 0; index < 5; index++) {
        basic.showNumber(getal)
        getal += -1
        basic.pause(100)
    }
    basic.pause(100)
    basic.clearScreen()
    getal = 24
    Toongetal(getal)
})
input.onPinPressed(TouchPin.P1, function () {
    while (input.pinIsPressed(TouchPin.P1)) {
    	
    }
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    getal += -1
    serial.writeNumber(getal)
    serial.writeLine("")
    basic.clearScreen()
    Toongetal(getal)
})
function Toongetal (num: number) {
    rij = Math.floor(num / 5)
    kol = num % 5
    for (let index = 0; index <= rij - 0; index++) {
        for (let index2 = 0; index2 <= kol; index2++) {
            led.plot(index, 4 - index2)
        }
    }
}
