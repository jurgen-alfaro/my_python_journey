
text = "Heeeeey\nThis is some text\nHave a good one!\n"
append_text = "Have a good day"

with open("test_write.txt", 'w') as file: # This writes and overwrittes
    file.write(text)
    
with open("test_write.txt", 'a') as file: # This appends
    file.write(append_text)