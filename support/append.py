fileName="./feedback.txt"

def append(text):
    try:
        with open(fileName, "a") as myfile:
            myfile.write(text)
    except Exception as e:
        pass