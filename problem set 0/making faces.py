def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    userInput = input("Enter some text with emoticons: ")
    convertedText = convert(userInput)
    print("Converted text: ", convertedText)

main()
