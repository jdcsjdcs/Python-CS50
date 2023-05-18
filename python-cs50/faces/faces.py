def main():
    txt = input()
    conv_message = convert(txt)
    print(conv_message)

def convert(txt):
    txt1 = txt.replace(':)', '🙂')
    txt2 = txt1.replace(':(', '🙁')
    return txt2

main()