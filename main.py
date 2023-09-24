getal = 0
rij = 0
kol = 0

def on_button_pressed_a():
    basic.show_number(randint(1, 6))
    music.play(music.string_playable("C D E F G A B C5 ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.clear_screen()
    for index in range(25):
        Toongetal(index)
        basic.pause(100)
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
    basic.clear_screen()
    getal = 24
    Toongetal(getal)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    global getal
    while input.pin_is_pressed(TouchPin.P1):
        pass
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    getal += -1
    serial.write_number(getal)
    serial.write_line("")
    Toongetal(getal)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def Toongetal(num: number):
    global rij, kol
    rij = num / 5
    kol = num % 5
    index3 = 0
    while index3 <= rij:
        serial.write_value("x", index3)
        serial.write_string("")
        index22 = 0
        while index22 <= kol:
            serial.write_value("y", index22)
            led.plot(index22, index3)
            index22 += 1
        serial.write_line("")
        index3 += 1