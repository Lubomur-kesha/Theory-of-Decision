import texttable as tt

def sum_of_votes(mat, lines, cand):
    Sum = 0
    for i in range(0, lines):    
        for j in range(0, len(mat[0])):
            if values[i][j] == cand:
                if values[i].index(cand) == 1:
                    Sum += values[i][0] * 2
                elif values[i].index(cand) == 2:
                    Sum += values[i][0] * 1
                elif values[i].index(cand) == 3:
                    Sum += values[i][0] * 0
    return Sum

def method_Condorce(mat, lines, left, right):
    res = list()
    res1 = 0
    res2 = 0
    for i in range(0, lines):
        if mat[i].index(left) < mat[i].index(right):
            res1 += mat[i][0]
        else:
            res2 += mat[i][0]
    res.append(res1)
    res.append(res2)
    return res

input_data = open("lab 3.txt", "r")

values = []
amount_of_line = 0
for aline in input_data:
    values.append(aline.split())
    amount_of_line +=1
input_data.close()

for i in range(0, amount_of_line):    
    if values[i][0].isdigit() == True:
        values[i][0] = int(values[i][0])

A = sum_of_votes(values, amount_of_line, 'A')
B = sum_of_votes(values, amount_of_line, 'B')
C = sum_of_votes(values, amount_of_line, 'C')

table = tt.Texttable()
data = [[]]
S = 0
for i in range(0, amount_of_line):
    data.append([values[i][0], values[i][1], values[i][2], values[i][3]])
    S += values[i][0]
data.append(['Сума', 'Бали кандидата 1', 'Бали кандидата 2', 'Бали кандидата 3'])
data.append([S, 2, 1, 0])
table.add_rows(data)
table.set_cols_align(['c','c','c','c'])
table.header(['', 1, 2, 3])
print('Дані для визначення переможця:')
print(table.draw())

table_Borda = tt.Texttable()
data_Borda = [[]]
data_Borda.append([A, B, C])
table_Borda.add_rows(data_Borda)
table_Borda.header(['A', 'B', 'C'])
print('Результати для методу Борда:')
print(table_Borda.draw())

res_Borda = max(A, B, C)

if res_Borda == A:
    print('Переможцем за методом Борда є кандидат А з рахунком ', res_Borda)
elif res_Borda == B:
    print('Переможцем за методом Борда є кандидат B з рахунком ', res_Borda)
elif res_Borda == C:
    print('Переможцем за методом Борда є кандидат C з рахунком ', res_Borda)    

first = method_Condorce(values, amount_of_line, 'A', 'B')
first_max = max(first)
if first.index(first_max) == 0:
    str1 = 'A > B'
else:
    str1 = 'B > A'

second = method_Condorce(values, amount_of_line, 'B', 'C')
second_max = max(second)
if second.index(second_max) == 0:
    str2 = 'B > C'
else:
    str2 = 'C > B'

third = method_Condorce(values, amount_of_line, 'A', 'C')
third_max = max(third)
if third.index(third_max) == 0:
    str3 = 'A > C'
else:
    str3 = 'C > A'

table_Condorce = tt.Texttable()
table_Condorce.add_rows([["Порівняння", "Значення", "Переможне порівняння"],
                        ["A > B\nB > A", str(first[0]) + "\n" + str(first[1]), str1],
                        ["B > C\nC > B", str(second[0]) + "\n" + str(second[1]), str2],
                        ["A > C\nC > A", str(third[0]) + "\n" + str(third[1]), str3]])
table_Condorce.set_cols_align(['c','c','c'])
table_Condorce.set_cols_valign(["m", "m", "m"])
print('Результати для методу Кондорсе:')
print(table_Condorce.draw())

if str1[len(str1) - 1] == str2[0]:
    str1_str2 = str1 + ' > ' + str2[len(str2) - 1]
    if str1_str2[0] == str3[0] and str1_str2[len(str1_str2) - 1] == str3[len(str3) - 1]:
        print(str1_str2)
        print('Переможцем за методом Кондорсе є кандидат ', str1_str2[0])
    else:
        print('Разом ці твердження суперечливі. Неможливо прийняти якесь узгоджене рішення')
elif str1[len(str1) - 1] == str3[0]:
    str1_str3 = str1 + ' > ' + str3[len(str3) - 1]
    if str1_str3[0] == str2[0] and str1_str3[len(str1_str3) - 1] == str2[len(str2) - 1]:
        print(str1_str3)
        print('Переможцем за методом Кондорсе є кандидат ', str1_str3[0])
    else:
        print('Разом ці твердження суперечливі. Неможливо прийняти якесь узгоджене рішення')
elif str2[len(str1) - 1] == str3[0]:
    str2_str3 = str2 + ' > ' + str3[len(str3) - 1]
    if str2_str3[0] == str1[0] and str2_str3[len(str2_str3) - 1] == str1[len(str1) - 1]:
        print(str2_str3)
        print('Переможцем за методом Кондорсе є кандидат ', str2_str3[0])
    else:
        print('Разом ці твердження суперечливі. Неможливо прийняти якесь узгоджене рішення')
        