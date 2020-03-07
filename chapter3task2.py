def textFunc():
    text = input("text: ").split(" ")
    text.sort(key=len)
    text = ' '.join(text)
    print(text)
textFunc()
