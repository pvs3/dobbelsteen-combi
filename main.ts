let getal = 0
let rij = 0
let kol = 0
function dump (num: number, num2: number) {
    serial.writeValue("x", num)
    serial.writeValue("y", num2)
    serial.writeLine("---------")
}
input.onButtonPressed(Button.A, function () {
    getal = 5
    for (let index = 0; index < 5; index++) {
        basic.showNumber(getal)
        getal += -1
        basic.pause(100)
    }
    basic.pause(100)
    getal = 19
    Toongetal(getal)
})
input.onPinPressed(TouchPin.P2, function () {
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.UntilDone)
    getal += -1
    Toongetal(getal)
    if (getal == 0) {
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        basic.showIcon(IconNames.No)
        while (true) {
        	
        }
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(20 - getal)
})
function Toongetal (num: number) {
    basic.clearScreen()
    rij = Math.floor(num / 5)
    kol = num % 5
    for (let index = 0; index <= 4; index++) {
        for (let index2 = 0; index2 <= rij - 1; index2++) {
            led.plot(index, 4 - index2)
        }
    }
    for (let index = 0; index <= kol; index++) {
        led.plot(index, 4 - rij)
    }
}
