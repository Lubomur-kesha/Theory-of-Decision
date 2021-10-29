import numpy as np
import texttable as tt
from pulp import *

def delete_dominant_row_and_col(mat):
    row1 = []
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            if all(np.less_equal(mat[j], mat[i])) == True and i != j and i < j:
                row1.append(j)
    row1 = list(dict.fromkeys(row1))
    mat = np.delete(mat, row1, 0)
    
    col1 = []
    mat = np.transpose(mat)
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            if all(np.greater_equal(mat[j], mat[i])) == True and i != j and i < j:
                col1.append(j)
    col1 = list(dict.fromkeys(col1))
    mat = np.transpose(mat)
    mat = np.delete(mat, col1, 1)
    
    row2 = []
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            if all(np.less_equal(mat[j], mat[i])) == True and i != j and i < j:
                row2.append(j)
    row2 = list(dict.fromkeys(row2))
    mat = np.delete(mat, row2, 0)
    
    col2 = []
    mat = np.transpose(mat)
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            if all(np.greater_equal(mat[i], mat[j])) == True and i != j and i < j:
                col2.append(i)
    col2 = list(dict.fromkeys(col2))
    mat = np.transpose(mat)
    mat = np.delete(mat, col2, 1)
    
    cols = sorted(col1 + col2)
    rows = sorted(row1 + row2)
    
    return mat, cols, rows
    
def print_all_payment_table(mat, not_use_col, not_use_row):
    input_matrix_tolist = mat.tolist()

    all_payment_matrix_table = tt.Texttable()
    all_payment_data = [[]]
    all_payment_header = ["Гравці"]
    last_payment_row = ["b = max(Bi)"]
    cols_align = ([])
    
    for i in range(0, len(input_matrix_tolist[0])):
        if i not in not_use_col:
            all_payment_header.append("B" + str(i+1))
    all_payment_header.append("a = min(Ai)")
    
    for i in range(0, len(all_payment_header)):
        cols_align.append('c')

    minus = 0
    for j in range(0, len(not_use_col)):
        for i in range(0, len(input_matrix_tolist)):
            del input_matrix_tolist[i][not_use_col[j]-minus]
        minus +=1 
    
    delete__matrix = input_matrix_tolist
    minus = 0
    for i in range(0, len(not_use_row)):
        del delete__matrix[not_use_row[i] - minus]
        minus +=1

    delete__matrix = np.array(delete__matrix)
    delete__matrix = np.transpose(delete__matrix)
    maximum = delete__matrix.max(axis=1)
    delete__matrix = np.transpose(delete__matrix)
    delete__matrix = delete__matrix.tolist()
    
    for i in range(0, len(maximum)):
        last_payment_row.append(maximum[i])
    last_payment_row.append(" ")

    minimum = [min(r) for r in delete__matrix]
    A = []
    for i in range(0, len(mat)):
        if i not in not_use_row:
            A.append("A" + str(i+1))
    
    for i in range(0, len(delete__matrix)):
        delete__matrix[i].insert(0, A[i])
        delete__matrix[i].append(minimum[i])
        all_payment_data.append(delete__matrix[i])
    
    all_payment_matrix_table.add_rows(all_payment_data)
    all_payment_matrix_table.add_row(last_payment_row)
    all_payment_matrix_table.set_cols_align(cols_align)
    all_payment_matrix_table.header(all_payment_header)
    
    print(all_payment_matrix_table.draw())
    print()

def print_unknown(mat, sign, unknown, function, known):
    print("Система рівнянь:")
    for i in range(0, len(mat)):
        print(str(sum(mat[i] * unknown)) + " " + sign + " 1")
        
    table_unknown = tt.Texttable()
    cols_align = []
    cols_width = []
    cols_dtype = []
    cols_header = []
    
    print("Функція:")
    if sign == ">=":
        print("F(x) = " + str(sum(unknown)) + " -> Min")
        cols_header = unknown+["F(x)"]
    elif sign == "<=":
        print("F(y) = " + str(sum(unknown)) + " -> Max")
        cols_header = unknown+["F(y)"]
    table_unknown.header(cols_header)
    
    print("Розв'язок:")
    for i in range(0, len(cols_header)):
        cols_align.append('c')
        cols_width.append(11)
        cols_dtype.append('t')
    table_unknown.set_cols_dtype(cols_dtype)
    table_unknown.add_row(known+[function])
    table_unknown.set_cols_align(cols_align)
    table_unknown.set_cols_width(cols_width)
    print(table_unknown.draw())

def print_pesults(cost, probability, p_or_q):
    table_unknown = tt.Texttable()
    cols_align = []
    cols_width = []
    cols_dtype = []
    cols_header = []
    
    probability = [round(num, 8) for num in probability]
    cost = round(cost, 8)
    
    if p_or_q == "p":
        for i in range(0, len(probability)):
            cols_header.append(p_or_q + str(i+1))
    elif p_or_q == "q":
        for i in range(0, len(probability)):
            cols_header.append(p_or_q + str(i+1))    
    cols_header.append("Ціна гри:")
    table_unknown.header(cols_header)
    
    for i in range(0, len(cols_header)):
        cols_align.append('c')
        cols_width.append(11)
        cols_dtype.append('t')
    table_unknown.set_cols_dtype(cols_dtype)
    table_unknown.add_row(probability+[cost])
    table_unknown.set_cols_align(cols_align)
    table_unknown.set_cols_width(cols_width)
    print(table_unknown.draw())
        
input_matrix = np.loadtxt("lab 5.txt", dtype=int)

min_in_row = input_matrix.min(axis=1)
max_in_col = input_matrix.max(axis=0)

deleted_cols = []
deleted_rows = []

print("Платіжна матриця:")
print_all_payment_table(input_matrix, deleted_cols, deleted_rows)

max_min_in_row = max(min_in_row)
min_max_in_col = min(max_in_col)

if max_min_in_row == min_max_in_col:
    min_in_row = min_in_row.tolist() 
    max_in_col = max_in_col.tolist()
    
    index_A = min_in_row.index(max_min_in_row) + 1
    index_B = max_in_col.index(min_max_in_col) + 1

    print("Вітаю, ти щасливчик. У вас верхня і нижня ціни гри співпадають.")
    print("Досягається це на одній і тій же парі стратегій:")
    print("(A" + str(index_A) + ",B" + str(index_B) + ") = " + str(max_min_in_row))
    print("Значить гра має сідлову точку (A" + str(index_A) + ",B" + str(index_B) + ")" +
      "і ціна гри дорівнює v = " + str(max_min_in_row))
elif max_min_in_row != min_max_in_col:
    print("Знаходимо гарантований виграш, який визначається нижньою ціною гри a = max(ai) = " + str(max_min_in_row) +
          ", яка вказує на максимальну чисту стратегію A2. Верхня ціна гри b = min(bj) = " + str(min_max_in_col) + 
          " Що свідчить про відсутність сідлової точки, оскільки a ≠ b, тоді ціна гри знаходиться в межах " + 
          str(max_min_in_row) + " <= y" + " <= " + str(min_max_in_col) + 
          ". Знаходимо рішення гри у змішаних стратегіях.")
    print()
    
    new_matrix, deleted_cols, deleted_rows = delete_dominant_row_and_col(input_matrix)
    
    print("Платіжна матриця після видалення домінуючих рядків та стовпчиків:")
    print_all_payment_table(input_matrix, deleted_cols, deleted_rows)
    
    transpose_new_matrix = np.transpose(new_matrix)
    
    x = []
    for i in range(0, len(transpose_new_matrix[0])):
        x.append(LpVariable("x" + str(i + 1), lowBound=0))
    problem_x = LpProblem("Simple Problem", LpMinimize)     
        
    problem_x += sum(x)
    
    for i in range(0, len(transpose_new_matrix)):
        problem_x += sum(transpose_new_matrix[i] * x) >= 1
        
    problem_x.solve()
    X = []
    for variable in problem_x.variables():
        X.append(variable.varValue)
    F_x = value(problem_x.objective)
    
    print("Стратегія для А:")
    print_unknown(transpose_new_matrix, ">=", x, F_x, X)
    print()
      
    V_x = 1 / sum(X)
    p = []
    for element in X:
        p.append(element * V_x)
    
    print("Ціна гри і ймовірності застосування стратегій гравця А:")
    print_pesults(V_x, p, "p")
    print()
    
    
    y = []
    for i in range(0, len(new_matrix[0])):
        y.append(LpVariable("y" + str(i + 1), lowBound=0))
    problem_y = LpProblem("Simple Problem", LpMaximize)        
        
    problem_y += sum(y)
    
    for i in range(0, len(new_matrix)):
        problem_y += sum(new_matrix[i] * y) <= 1
    
    problem_y.solve()
    Y = []
    for variable in problem_y.variables():
        Y.append(variable.varValue)
    F_y = value(problem_y.objective)
    
    print("Стратегія для B:")
    print_unknown(new_matrix, "<=", y, F_y, Y)
    print()
    
    V_y = 1 / sum(Y)
    q = []
    for element in Y:
        q.append(element * V_y)
        
    print("Ціна гри і ймовірності застосування стратегій гравця B:")
    print_pesults(V_y, q, "q")
    print()