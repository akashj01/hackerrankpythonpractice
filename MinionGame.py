def minion_game(string):


    kevin_score = 0
    stuart_score = 0
    sbtr = []
    for i in range(0,len(string)):
        if string[i] == 'A' or string[i] == 'E' or string[i] == 'I' or string[i] == 'O' or string[i] == 'U':

            for k in range(i,len(string)):
                sub_string = string[i:k+1]
                if sub_string not in sbtr:
                    sbtr.append(sub_string)
                    for j in range(i,len(string)):
                        if string.find(sub_string,j,j+len(sub_string)) != -1:
                            kevin_score += 1


        else:

            for k in range(i,len(string)):
                sub_string = string[i:k+1]
                if sub_string not in sbtr:
                    sbtr.append(sub_string)
                    for j in range(i,len(string)):
                        if string.find(sub_string,j,j+len(sub_string)) != -1:
                            stuart_score += 1
    print(stuart_score,kevin_score)
    if stuart_score > kevin_score:
        print('Stuart',stuart_score)
    elif kevin_score > stuart_score:
        print('Kevin',kevin_score)
    else:
        print('Draw')




    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)