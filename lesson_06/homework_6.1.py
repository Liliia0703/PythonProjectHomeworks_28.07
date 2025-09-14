text = input("Hello, my friend! Write me a message: ")
all_chars = len(set(text))
if all_chars > 10:
    print(True)
else:
    print(False)
