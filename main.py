getal = 0
status = 0
pin = 0
pinA = 0
rij = 0
kol = 0
def dump(num: number, num2: number):
    serial.write_value("x", num)
    serial.write_value("y", num2)
    serial.write_line("---------")

def on_button_pressed_a():
    basic.show_number(randint(1, 6))
    music.play(music.string_playable("C D E F G A B C5 ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.clear_screen()
    for index in range(101):
        led.toggle(4, 0)
        basic.pause(100)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_pin_pressed_p2():
    global getal
    serial.write_number(0)
    serial.write_line("")
    music.play(music.tone_playable(262, music.beat(BeatFraction.SIXTEENTH)),
        music.PlaybackMode.UNTIL_DONE)
    getal += -1
    basic.clear_screen()
    Toongetal(getal)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

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
    global getal, status, pin, pinA
    getal = 5
    for index2 in range(5):
        basic.show_number(getal)
        getal += -1
        basic.pause(100)
    basic.pause(100)
    getal = 19
    Toongetal(getal)
    status = 0
    while getal >= 0:
        pin = pins.digital_read_pin(DigitalPin.P1)
        if pin == 1:
            if status == 1:
                getal += -1
                serial.write_number(pins.analog_read_pin(AnalogPin.P1))
                serial.write_line("")
                Toongetal(getal)
                music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
                    music.PlaybackMode.UNTIL_DONE)
                status = 0
                led.unplot(4, 0)
        else:
            status = 1
            led.plot(4, 0)
            pinA = pins.analog_read_pin(AnalogPin.P1)
            serial.write_number(pinA)
            serial.write_line("")
            if pinA < 3:
                basic.show_icon(IconNames.HAPPY)
                music.play(music.string_playable("C D E F G A B C5 ", 120),
                    music.PlaybackMode.UNTIL_DONE)
                pinA = 100
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.B, on_button_pressed_b)

def Toongetal(num3: number):
    global rij, kol
    basic.clear_screen()
    rij = Math.floor(num3 / 5)
    kol = num3 % 5
    for index3 in range(5):
        index22 = 0
        while index22 <= rij - 1:
            led.plot(index3, 4 - index22)
            index22 += 1
    index4 = 0
    while index4 <= kol:
        led.plot(index4, 4 - rij)
        index4 += 1