#inserts spaces in between combined words with uppercase letters
#converts uppercase words to lowercase depending on placement within sentence
print("Word Separator")

usr_sent = input("Please enter the sentence you need to separate and this program will process it for you: ")

new_sent = "".join([" " + char if char.isupper() else char for char in usr_sent]).strip()

print(new_sent)
