import wave

arquivo = wave.open("som.wav", "w")
arquivo.close()

arquivo.setparams()
parametros = (1, 2, 44100, 0, "NONE", "not compressed")