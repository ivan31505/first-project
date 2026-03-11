prompt = "\nнапиши мне что нибудь и я это повторю: "
prompt += "\nНабери слово 'выход'для завершения проги."
message = ""
активно = True # thats a flag
while активно:
    message = input(prompt)
    if message == 'выход':
        активно = False
    else:
        print(message)
