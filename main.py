pins.digital_write_pin(DigitalPin.P1, 0)
control.wait_micros(2)
pins.digital_write_pin(DigitalPin.P1, 1)
control.wait_micros(5)
pins.digital_write_pin(DigitalPin.P1, 0)
control.wait_micros(2)
distance = pins.pulse_in(DigitalPin.P1, PulseValue.HIGH) / 58

def on_forever():
    global distance
    distance = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.CENTIMETERS)
    if distance > 100:
        music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
                5000,
                1,
                239,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            SoundExpressionPlayMode.UNTIL_DONE)
    elif distance > 50:
        music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
                838,
                1,
                239,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            SoundExpressionPlayMode.UNTIL_DONE)
    elif distance > 30:
        music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
                838,
                1,
                239,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            SoundExpressionPlayMode.UNTIL_DONE)
    elif distance > 10:
        music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                838,
                1,
                239,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            SoundExpressionPlayMode.UNTIL_DONE)
    else:
        pins.digital_write_pin(DigitalPin.P0, 1)
basic.forever(on_forever)
