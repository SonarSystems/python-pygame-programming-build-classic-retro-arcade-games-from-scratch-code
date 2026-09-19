import numpy
import pygame


def generate_tone(frequency, duration, sample_rate=44100, volume=0.3):
    """A simple sine-wave beep — the raw material for many arcade-style
    effects, with a linear fade-out to avoid an audible 'click' at the end."""
    num_samples = int(sample_rate * duration)
    t = numpy.linspace(0, duration, num_samples, False)
    wave = numpy.sin(frequency * t * 2 * numpy.pi)
    fade = numpy.linspace(1.0, 0.0, num_samples)
    wave = wave * fade * volume
    audio = numpy.int16(wave * 32767)
    stereo = numpy.column_stack([audio, audio])
    return pygame.sndarray.make_sound(stereo)


pickup_sound = generate_tone(880, 0.12)
laser_sound = generate_tone(220, 0.18)
