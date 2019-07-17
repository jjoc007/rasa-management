

def save_file(path, text):
    text_file = open(path, "w")
    text_file.write(text)
    text_file.close()
