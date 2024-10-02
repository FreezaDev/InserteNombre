memes = {"CRINGE": "algo excepcionalmente raro",
         "LOL": "respuesta comun a algo gracioso",
         "GG": "good game (bien jugado)",
         "EZ": "easy (facil)",
         "BRO": "brother/hermano (para referirse a alguien)",
         "BTW": "by the way (por cierto)",
         "TBH": "to be honest (para ser honesto)",
         "IMO": "in my opinion (en mi opinion)",
         "ASAP": "as soon as possible (tan pronto posible)"
        }

word = input("Escribe una palabra que no sepas en mayusculas\n(por favor escribe cringe o lol te lo ruego)")

if word in memes.keys():
    print("GRAX!!!!!!!!!!! AHORA PUUEDO MANTENER A MI FAMILIA\n", memes[word])
else:
    print("TE VOY A ENCONTRAR RAHHHHH")
