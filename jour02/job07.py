def lang(langage):
    if langage == "javascript":
        return "Tu es dev web"
    elif langage == "python":
        return "Tu es dev AI"
    elif langage == "java":
        return "Tu es dev logiciel"
    elif langage == "reactjs":
        return "Tu es dev mobile"
    else:
        return "Un jour je serais dev..."

print(lang("javascript"))
print(lang("python"))
print(lang("grub"))