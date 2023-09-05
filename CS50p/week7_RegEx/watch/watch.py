import re
import sys

#calls HTML iframe and also prints the simplified youtube link
def main():
    print(parse(input("HTML: ")))


def parse(s):

    #seaches for youtube link in iframe
    if match := re.search(r'src="https?://(www\.)?youtube\.com/embed/(\w{11})"', s, re.IGNORECASE):

        #returns the group of the end to be included in f string
        return f"https://youtu.be/{match.group(2)}"
    else:
        return None







if __name__ == "__main__":
    main()