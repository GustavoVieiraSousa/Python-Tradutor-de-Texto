from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source= "pt", target= "en")

texto = "Teste de tradução rapida utilizando Python"

traducao = tradutor.translate(texto)


print(traducao)