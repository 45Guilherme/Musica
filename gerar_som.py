import wave

def gerar_som(frequencia, duracao, volume, arquivo):
    import math
    import struct

    taxa_amostragem = 44100
    total_amostragem = int(taxa_amostragem * duracao)


    for i in range(total_amostragem):
      valor = math.sin(2 * math.pi * frequencia * (i / taxa_amostragem))
      amplitude = int(valor * 32767 * volume)
      dados = struct.pack("<h", amplitude)
      arquivo.writeframes(dados)


arquivo = wave.open("som.wav", "w")

arquivo.setparams((1, 2, 44100, 0, "NONE", "not compressed"))

gerar_som(440, 2, 0.5, arquivo)
gerar_som(880, 2, 0.5, arquivo)
gerar_som(660, 2, 0.5, arquivo)

arquivo.close() 


