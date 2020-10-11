import operator

def BMM(dic, context):
    ans = []
    end = len(context)
    max_word = max(len(i) for i in dic)
    while end > 0:
        for i in range(max(end - max_word,0), end):
            if context[i:end] in dic or end - i == 1:
                ans.append(context[i:end])
                break
        end = i
    return ' '.join(ans[::-1])

def FMM(dic,context):
    ans = []
    end = len(context)+1
    top = 0
    max_word = max(len(i) for i in dic)
    while end > top+1:
        for i in range(min(top + max_word,end),top,-1):
            if context[top:i] in dic or i - top == 1:
                ans.append(context[top:i])
                top = i
                break
    return ' '.join(ans[::])

def cut_word(dic,context):
    ans_1 = BMM(dic,context)
    ans_2 = FMM(dic,context)
    if len(ans_1) < len(ans_2):
        return ans_1
    if len(ans_1) > len(ans_2):
        return ans_2
    if len(ans_1) == len(ans_2):
        count_1 = count_2 = 0
        for i in ans_1:
            if len(i) == 1:
                count_1 = count_1 + 1
        for j in ans_2:
            if len(j) == 1:
                count_2 = count_2 + 1
        if(count_1 > count_2):
            return ans_2
        return ans_1

def cal_correctness(file_name_1,file_name_2):
    correct_num = total_num = 0
    f_1 = open(file_name_1,"r",encoding="UTF-8")
    f_2 = open(file_name_2,"r",encoding="UTF-8")
    res = f_1.readlines()
    ans = f_2.readlines()
    if len(res) != len(ans):
        print("Error")
    total_num = len(res)
    for i in range(0,total_num):
        ls_1 = res[i].split()
        ls_2 = ans[i].split()
        if operator.eq(ls_1,ls_2):
            correct_num = correct_num + 1
    f_1.close()
    f_2.close()
    return correct_num

#print(cal_correctness("BMM_output.txt","FMM_output.txt"))

if __name__ == '__main__':
    dic_file = open("dic.txt","r",encoding="UTF-8")
    dic_1 = dic_file.readlines()
    dic = []
    for i in dic_1:
        dic.append(i[:len(i)-1])
    input_file = open("input.txt","r",encoding="UTF-8")
    input = input_file.readlines()
    output_file = open("output.txt","w")
    BMM_output_file = open("BMM_output.txt","w")
    FMM_output_file = open("FMM_output.txt","w")
    for i in input:
        output_file.write(cut_word(dic,i))
        BMM_output_file.write(BMM(dic,i))
        FMM_output_file.write(FMM(dic,i))
    output_file.close()
    BMM_output_file.close()
    FMM_output_file.close()
    dic_file.close()
    input_file.close()
