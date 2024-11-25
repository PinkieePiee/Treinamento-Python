with open('conteudo/texto.txt', encoding='utf-8') as text:
    for linha in text:
        print(linha)


with open('conteudo/texto.txt', encoding='utf-8') as arquivo:
    texto = arquivo.read()

    palavras = texto.split()

    vogais = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'é', 'É', 'à')

    for palavra in palavras:
        if palavra.startswith(vogais):
            print(palavra)