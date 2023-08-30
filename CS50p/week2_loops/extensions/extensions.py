def main():
    #input on file type from user
    form = input("Name of file: ").lower().strip()

    #if the input doesnt have a dot, this places in a dot
    if "." not in form:
        form += "."

    #splits input and places into list(["name", "file type"])
    pp = form.split(".")

    #function that  spits out media type of the file
    print(output(pp))

#defining output function
def output(p):

    #using case and match to create file's media type
    #can be more simple by doing case by each ending and also printing out output instead of returning
    #this is inefficient and was ignorant. Only wanted to see if something extra could work
    match str(p[len(p)-1]):
        case "gif" | "jpeg" | "png":
            c = "image/" + str(p[len(p)-1])
            return c
        case "jpg":
            c = "image/jpeg"
            return c
        case "pdf" | "zip":
            c = "application/" + str(p[len(p)-1])
            return c
        case "txt":
            c = "text/plain"
            return c
        case _:
          return "application/octet-stream"





main()
