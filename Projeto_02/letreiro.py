import pyfiglet

def banner_pagga(texto):
    letra = pyfiglet.figlet_format(texto, font="pagga")
    return letra

def banner_future(texto):
    letra = pyfiglet.figlet_format(texto, font="future")
    return letra