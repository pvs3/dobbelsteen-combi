let getal = 0
let rij = 0
let kol = 0
input.onButtonPressed(Button.A, function () {
    basic.showNumber(randint(1, 6))
    music.play(music.stringPlayable("C D E F G A B C5 ", 120), music.PlaybackMode.UntilDone)
})
input.onGesture(Gesture.Shake, function () {
    for (let index = 0; index <= 24; index++) {
        Toongetal(index)
        basic.pause(100)
        basic.clearScreen()
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
    getal = 0
    basic.showNumber(getal)
    basic.clearScreen()
    while (input.pinIsPressed(TouchPin.P1)) {
        getal += 1
        Toongetal(getal)
        basic.pause(1000)
    }
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    basic.showNumber(getal)
})
function Toongetal (num: number) {
    rij = num / 5
    kol = num % 5
    for (let index = 0; index <= rij; index++) {
        serial.writeNumber(index)
        for (let index2 = 0; index2 <= kol; index2++) {
            serial.writeNumber(index2)
            led.plot(index, index2)
        }
        serial.writeLine("")
    }
}
