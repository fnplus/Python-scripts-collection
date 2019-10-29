#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import sys
 
def contador(link, palavra):
    print("Bem vindo ao contador de palavra")
    print()
    link = sys.argv[1]
    palavra = sys.argv[2]
    while True:
        try:
            r = requests.get(link)
            texto = r.text.lower()
            contador = texto.count(palavra.lower())
            print()
            print('{} aparece {} vezes em {}'.format(palavra, contador, link))
            break
        except (requests.exceptions.ConnectionError, IndexError):
            print('O link informado é inválido, verifique-o e tente novamente.')
            break
        except requests.exceptions.MissingSchema:
            print('Por favor insira http(s) antes do seu link.')
            break
contador(sys.argv[1], sys.argv[2])
