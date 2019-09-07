import textwrap3


def wrap(string, max_width):
    wraper = textwrap3.TextWrapper(width=4)
    word_list = wraper.wrap(text=string)
    a =''
    for i in range(len(word_list)):
        a += word_list[i]
        a += '\n'
    return a

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)