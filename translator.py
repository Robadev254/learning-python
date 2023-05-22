def translate (phrase):
    trnslation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            trnslation = translate +"g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase :")))
