import random #导入random库

#硬编码字符列表
numbers = ['0','1','2','3','4','5','6','7','8','9']
lower_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special_symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','[',']','{','}','|',';',':','"',"'",'<','>',',','.','?','/']

#输出元素会先储存到这个列表
outputs = []

#输出程序标题及作者等信息
print("======Random_string_generater v2.0.1========")
print("by CH3Hg\nhttps://github.com/CH3Hg/Random_string_generater")

#获取生成长度函数，返回值length，类型为整型int
def get_length():

    while True:#死循环，在没有正确结束前不会跳出循环体

        try:#异常处理，检查是否能够正确把输入值转换为int类型，如果不能则代表输入了其他类型的数据

            length = int(input("请输入要生成的字符串长度(正整数):"))#获取长度变量length并转换为int类型，这一步报错会直接转到except

            if length <= 0:#比较length的大小，判定其是否为正数

                print("错误:输入的值必须为正整数(E02)")#输出报错信息

                continue#结束这次循环重新输入

            return length#所有步骤全部正确，返回length
        
        except ValueError:#数据转换类型出错

            print("错误:输入了不正确的数据类型(E01)")#输出报错信息

#生成一个随机字符函数，返回值为硬编码列表中的元素，类型为str
def generate_char():

    mode = random.randint(1, 4)#这里随机了一个1-4的整数代表模式，1代表生成数字，2代表生成小写字母...（后面同理）

    if mode == 1:

        return random.choice(numbers)#在列表中随机一个元素并返回
    
    elif mode == 2:

        return random.choice(lower_letters)
    
    elif mode == 3:

        return random.choice(upper_letters)
    
    else:

        return random.choice(special_symbols)

#主函数  
def main():

    for i in range(get_length()):#进行循环，次数为get_length()返回的值

        outputs.append(generate_char())#将随机生成的字符加入到outputs列表中

    output = "".join(outputs)#把outputs中的元素拼接为字符串并赋值给output

    print(output)#输出结果

#调用主函数
if __name__ == "__main__":

    main()
    
    input()#添加一个输入来避免窗口直接消失