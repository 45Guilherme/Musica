import wave
import math

arquivo = wave.open("som.wav", "w")
arquivo.setparams((1, 2, 44100, 0, "NONE", "not compressed"))
arquivo.close()

