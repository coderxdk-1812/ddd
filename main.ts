pins.digitalWritePin(DigitalPin.P1, 0)
control.waitMicros(2)
pins.digitalWritePin(DigitalPin.P1, 1)
control.waitMicros(5)
pins.digitalWritePin(DigitalPin.P1, 0)
control.waitMicros(2)
let distance = pins.pulseIn(DigitalPin.P1, PulseValue.High) / 58
basic.forever(function on_forever() {
    
    distance = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.Centimeters)
    if (distance > 100) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 5000, 1, 239, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
    } else if (distance > 50) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 838, 1, 239, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
    } else if (distance > 30) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 838, 1, 239, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
    } else if (distance > 10) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 838, 1, 239, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
    } else {
        pins.digitalWritePin(DigitalPin.P0, 1)
    }
    
})
