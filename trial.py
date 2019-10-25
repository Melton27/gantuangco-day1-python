content = {"aa": 12, "bb": 21}

with open("sample.txt", "w+") as file:
    file.write(str(content))

with open("sample.txt","r+") as file:
    contents = file.read()

def main():
    
        print(content)
main()