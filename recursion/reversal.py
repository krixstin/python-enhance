def string_reversal(input):
    print(input)
    if input == "":
        return ""
    # print(string_reversal(input[1:])+ input[0])
    return string_reversal(input[1:])+ input[0]

print(string_reversal("string"))