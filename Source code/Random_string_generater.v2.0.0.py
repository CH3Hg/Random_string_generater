import random
import os

numbers = ['0','1','2','3','4','5','6','7','8','9']
lower_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special_symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','[',']','{','}','|',';',':','"',"'",'<','>',',','.','?','/']

outputs = []

print("======Random_string_generater v2.0.0========")
print("by CH3Hg\nhttps://github.com/CH3Hg/Random_string_generater")

def get_length():
    while True:
        try:
            length = int(input("请输入要生成的字符串长度(正整数):"))
            if length <= 0:
                print("错误:输入的值必须为正整数(E02)")
                continue
            return length
        except ValueError:
            print("错误:输入了不正确的数据类型(E01)")

def generate_char():
    mode = random.randint(1, 4)
    if mode == 1:
        return random.choice(numbers)
    elif mode == 2:
        return random.choice(lower_letters)
    elif mode == 3:
        return random.choice(upper_letters)
    else:
        return random.choice(special_symbols)
    
def main():
    for i in range(get_length()):
        outputs.append(generate_char())
    output = "".join(outputs)
    print(output)

if __name__ == "__main__":
    main()
    os.system("pause")