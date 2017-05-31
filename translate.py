# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
# That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun")
# should return the string "tothohisos isos fofunon".


def translate(text):
    new_text = []
    for word in text:
        if word in ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "z"):
            new_text.append(word + "o" + word)
        else:
            new_text.append(word)
    print("".join(new_text))
    return new_text
