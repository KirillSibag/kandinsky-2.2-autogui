import random as r

f = open("prompt.txt","w+")


##   15,  5,  3,   2, 1
##a = ["", "длинные", "короткие", "", "лысый"] # длина волос
##b = ["", "светлые", "тёмные", "fair", "зелёно-синие"] # цвет волос
##c = ["", "", "", "тёмной", ""] # цвет кожи
##d = ["", "", "карие", "чёрные", "голубые"] # цвет глаз
##i = ["", "", "стеснительная", "глупая", "умная"]
##e = ["девушка", "мальчик", "старик", "старуха", "кот"] # объект
##f = ["", "смеётся", "улыбается", "плачет", "спит"] # действие
##g = ["", "", "в классе", "в парке", "на скамейке"] # место
##h = ["", "", "детализация", "лайнарт", "минимализм"] # стиль
##m = ["", "", "", "", ""] # 
##n = ["", "", "", "", ""] # 
##o = ["", "", "", "", ""] # 
##p = ["", "", "", "", ""] # 
##q = ["", "", "", "", ""] # 
##r = ["", "", "", "", ""] # 
##s = ["", "", "", "", ""] # 
##t = ["", "", "", "", ""] # 
##u = ["", "", "", "", ""] # 

##a = ["", "long", "short", "", "bald"]                           # hair length
##b = ["", "light", "dark", "fair", "green-blue"]                 # hair color
##c = ["", "", "", "dark", ""]                                    # skin color
##d = ["", "", "brown", "black", "blue"]                          # eye color
##i = ["", "", "shy", "stupid", "smart"]                          # 
##e = ["girl", "boy", "old man", "old woman", "cat"]              # object
##f = ["", "laughing", "smiling", "crying", "sleeping"]           # action
##g = ["", "", "in the classroom", "in the park", "on the bench"] # seat
##h = ["", "", "detail", "lineart", "minimalism"]                 # style


count = 0
while count < 64000000:
    stri = ""

    character = r.choices(["", "cute", "shy", "stupid", "smart"] ,              weights=[15, 5, 3, 2, 1], k = 1)[0]
    who =       r.choices(["girl", "boy", "old man", "old woman", "cat"] ,              weights=[15, 5, 3, 2, 1], k = 1)[0]
    action =    r.choices(["", "laughing", "smiling", "crying", "sleeping"] ,           weights=[15, 5, 3, 2, 1], k = 1)[0]
    place =     r.choices(["", "", "in the classroom", "in the park", "on the bench"] , weights=[15, 5, 3, 2, 1], k = 1)[0]
    hairlen =   r.choices(["", "long", "short", "", "bald"] ,                           weights=[15, 5, 3, 2, 1], k = 1)[0]
    haircol =   r.choices(["", "light", "dark", "fair", "green-blue"] ,                 weights=[15, 5, 3, 2, 1], k = 1)[0]
    skin =      r.choices(["", "", "", "dark", ""] ,                                    weights=[15, 5, 3, 2, 1], k = 1)[0]
    eye =       r.choices(["", "", "brown", "black", "blue"] ,                          weights=[15, 5, 3, 2, 1], k = 1)[0]
    style =     r.choices(["", "", "detail", "lineart", "minimalism"] ,                 weights=[15, 5, 3, 2, 1], k = 1)[0]

    if character != "":
        stri += character + " "

    
    stri += who + " "

    if action != "":
        stri += action + " "
        
    if place != "":
        stri += place + ", "
    else:
        stri += ", "

    if hairlen != "":
        stri += haircol + " "
        stri += hairlen + " hair, "

    if skin != "":
        stri += skin + " skin, "

    if eye != "":
        stri += eye + " eyes, "

    if style != "":
        stri += style


    if len(stri) > 20:
        if stri[len(stri)-2] == ",":
##            print(stri)
            stri = stri[0:len(stri)-2]

        f.write(stri + "\n")
        count += 1

f.write("0")
f.close()
