import wave
import math
import struct

arquivo = wave.open("som.wav", "w")
arquivo.setparams((1, 2, 44100, 0, "NONE", "not compressed"))
frequencia = 440
duracao = 2
taxa_amostragem = 44100
total_amostragem = int(taxa_amostragem * duracao)

for i in range(total_amostragem):
    valor = math.sin(2 * math.pi * frequencia * (i / taxa_amostragem))
    amplitude = int(valor * 32767)
    dados = struct.pack("<h", amplitude)
    arquivo.writeframes(dados)

arquivo.close()

