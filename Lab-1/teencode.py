teendict = {
    'any' : 'Anh người yêu',
    'ns' : 'Nói - Hành động giao tiếp của con người',
    'xm' : 'Xem - Hoạt động nhìn ngắm của con người',
    'hk' : 'Không - Sự từ chối, lời từ chối',
    'ngta': 'Người ta - Ý nói người khác không liên quan tới mình',
    'cng': 'Con người',
    'gato' : 'gen ăn tức ở - Sự ganh tỵ, khó chịu với người khác'
}

while True:
    for key in teendict:
        print(key, end=' ')
    print()

    code = input("Enter your code: ").lower()

    if code in teendict:
        print("*" * 40)
        print("Code:", key)
        print("Translation:", teendict[key])
        print("*" * 40)
    else:
        contr = input("Not found in dict! Do you want to contribute new code? (Y/N)").lower()
        if contr == "y":
            trans = input("Enter its translation: ")
            teendict[code] = trans
        elif contr == "n":
            print("Okay Bye1")
            break
