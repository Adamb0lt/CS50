def main():
    tweet = input("Text: ").strip()
    print(shorten(tweet))

def shorten(msg):
    vowels = ["a","e","i","o","u"]
    for i in msg:
        if i.lower() in vowels:
            msg = msg.replace(i,"")
    return msg

if __name__ == "__main__":
    main()

