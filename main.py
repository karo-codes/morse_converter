# A text-based Python program to convert Strings into Morse Code.

morse_code = {
        "A": "•-",
        "B": "-•••",
        "C": "-•-•",
        "D": "-••",
        "E": "•",
        "F": "••-•",
        "G": "--•",
        "H": "••••",
        "I": "••",
        "J": "•---",
        "K": "-•-",
        "L": "•-••",
        "M": "--",
        "N": "-•",
        "O": "---",
        "P": "•--•",
        "Q": "--•-",
        "R": "•-•",
        "S": "•••",
        "T": "-",
        "U": "••-",
        "V": "•••-",
        "W": "•--",
        "X": "-••-",
        "Y": "-•--",
        "Z": "--••",
        "0": "-----",
        "1": "•----",
        "2": "••---",
        "3": "•••--",
        "4": "••••-",
        "5": "•••••",
        "6": "-••••",
        "7": "--•••",
        "8": "---••",
        "9": "----•",
        "&": "•-•••",
        "'": "•----•",
        "@": "•--•-•",
        ")": "-•--•-",
        "(": "-•--•",
        ":": "---•••",
        ",": "--••--",
        "=": "-•••-",
        "!": "-•-•--",
        ".": "•-•-•-",
        "-": "-••••-",
        "+": "•-•-•",
        "?": "••--••",
        "/": "-••-•",
        }

on = True
while on:
    text = str(input('What string should we convert to Morse Code? (type stop to end) ').upper())

    if '"' in text or "%" in text:
        print('Sorry, try again without including " or % characters')
    elif text == "STOP":
        on = False

    else:
        wordlist = text.split(' ')

        #print(wordlist)

        for word in wordlist:
            for ch in word:
                # match the character inputted to a morse_character, then return the morse_code w/ the same index and add
                # a letter space
                print(f"{morse_code[ch]}...", end="")
            # then print ....... to indicate space b/w word
            print(".......", end="")
        # add plus sign as it's also the End of message sign
        print(morse_code["+"])
