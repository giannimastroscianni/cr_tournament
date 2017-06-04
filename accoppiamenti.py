import random

# this dictionary maps the player to his own position at the end of the season
dic = {1: "JaK", 2: "Archer", 3: "federico", 4: "minu", 5: "nanorosa", 6: "Serj", 7: "CapitanComodino",
       8: "Orange Rubis", 9: "fax", 10: "Alex Metagame",
       11: "giannisoad", 12: "L'Oste", 13: "kikoraspa", 14: "kiaruch", 15: "NOFE90B", 16: "Jusdeby"}

# it prints the list of players
print "Lista dei partecipanti in ordine di arrivo nella stagione:"
for el in dic:
    print el, ":", dic[el]

# a little bit of suspance...
go = raw_input("Premere invio per continuare...")

# it creates matchings. it deletes iteratively the entry from the dictionary, than returns every couple
i = 1
count = 1
while i < len(dic):
    print "Accoppiamento " + str(count)
    first = random.choice(dic.keys())
    home = dic[first]
    del dic[first]
    second = random.choice(dic.keys())
    away = dic[second]
    del dic[second]
    count += 1
    print (home, away)
