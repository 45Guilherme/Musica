import wave
import math

arquivo = wave.open("som.wav", "w")
arquivo.setparams((1, 2, 44100, 0, "NONE", "not compressed"))
frequencia = 440
duracao = 2
taxa_amostragem = 44100
total_amostragem = int(taxa_amostragem * duracao)
arquivo.close()

