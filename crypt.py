# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from numbers import Number

alphabet = []
altalphabet = []
letters = "A,B,C,Ć,Č,D,Đ,DŽ,E,F,G,H,I,J,K,L,LJ,M,N,NJ,O,P,R,S,Š,T,U,V,Z,Ž"
altletters = "A,B,C,Ć,Č,D,Đ,X,E,F,G,H,I,J,K,L,Y,M,N,W,O,P,R,S,Š,T,U,V,Z,Ž"
alphabet.extend(letters.split(","))
altalphabet.extend(altletters.split(","))

while True:
    string = raw_input("Unesite string za kriptiranje/dekriptiranje (q za izlazak): \n?> ").decode('utf-8').upper()
    if string == "q" or string == "Q":
        break
    method = raw_input("Kriptiranje/Dekriptiranje (k/d): \n?> ").decode('utf-8').upper()
    shift = int(raw_input("Unesite pomak: \n?> "))

    chiper = []

    string = string.replace("DŽ", "X")
    string = string.replace("LJ", "Y")
    string = string.replace("NJ", "W")
    for char in string:
        if char in altalphabet:
            if method == "k" or method == "K":
                chiper.append(alphabet[(altalphabet.index(char) + shift) % len(alphabet)])
            else:
                chiper.append(alphabet[(altalphabet.index(char) - shift) % len(alphabet)])
        else:
            chiper.append(char)

    print "Rezultat: \n"
    print "".join(chiper)