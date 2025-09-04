while True:
    word = input("Enter a word that contains the letter 'h': ")
    if "h" in word.lower():
        print("Word is correct:", word)
        break
    else:
        print("Word is wrong")