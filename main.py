getal = 0
rij = 0
kol = 0

def on_button_pressed_a():
    basic.show_number(randint(1, 6))
    music.play(music.string_playable("C D E F G A B C5 ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    for index in range(25):
        Toongetal(index)
        basic.pause(100)
        basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global getal
    getal = randint(1, 3)
    if getal == 1:
        basic.show_icon(IconNames.SQUARE)
    elif getal == 2:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
    else:
        basic.show_leds("""
            . . . # #
            # . # . .
            . # . . .
            # . # . .
            . . . # #
            """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global getal
    getal = 5
    for index2 in range(5):
        basic.show_number(getal)
        getal += -1
        basic.pause(100)
    basic.pause(100)
    getal = 0
    basic.show_number(getal)
    basic.clear_screen()
    while input.pin_is_pressed(TouchPin.P1):
        getal += 1
        Toongetal(getal)
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_number(getal)
input.on_button_pressed(Button.B, on_button_pressed_b)

def Toongetal(num: number):
    global rij, kol
    rij = Math.constrain(num, 0, 4)
    kol = num % 5
    index3 = 0
    while index3 <= rij:
        serial.write_number(index3)
        index4 = 0
        while index4 <= kol:
            serial.write_number(index4)
            led.plot(index4, index4)
            index4 += 1
        index3 += 1