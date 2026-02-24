import wave

def gerar_som(lista_frequencias, duracao, volume, arquivo):
    import math
    import struct

    taxa_amostragem = 44100
    total_amostragem = int(taxa_amostragem * duracao)


    for i in range(total_amostragem):
         soma = 0
         for frequencia_atual in lista_frequencias:
             valor = math.sin(2 * math.pi * frequencia_atual * i / taxa_amostragem)
             soma += valor

         valor_final = soma / len(lista_frequencias) 

         amplitude_final = int(valor_final * 32767 * volume)
         dados = struct.pack("<h", amplitude_final)
         arquivo.writeframes(dados)


arquivo = wave.open("som.wav", "w")

arquivo.setparams((1, 2, 44100, 0, "NONE", "not compressed"))

gerar_som([440, 660, 880], 2, 0.5, arquivo)

arquivo.close() 


