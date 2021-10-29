import numpy as np
import texttable as tt

def Walds_criterion(mat):
    min_in_row = mat.min(axis=1)
    return min_in_row

def Maximum_criterion(mat):
    max_in_row = mat.max(axis=1)
    return max_in_row
    
def Laplace_criterion(mat):
    K_opt = np.around(np.sum(mat, axis=1) / len(mat[0]), 2)
    return K_opt

def Hurwitz_criterion(mat):
    Alfa = 0.5
    min_in_row = mat.min(axis=1)
    max_in_row = mat.max(axis=1)
    s = []
    for i in range(0, len(min_in_row)):
        s.append(Alfa * min_in_row[i] + (1 - Alfa) * max_in_row[i])
    return np.array(s)

def Bayes_Laplace_criterion(mat):
    p = np.array([0.5, 0.35, 0.15])
    res = mat.dot(p)
    return res

matrix = np.loadtxt("lab 1.txt", dtype=int)

Walds_value = Walds_criterion(matrix)
Walds_value = Walds_value.tolist()
Maximim_value = Maximum_criterion(matrix)
Maximim_value = Maximim_value.tolist()
Laplace_value = Laplace_criterion(matrix)
Laplace_value = Laplace_value.tolist()
Hurwitz_value = Hurwitz_criterion(matrix)
Hurwitz_value = Hurwitz_value.tolist()
Bayes_Laplace_value = Bayes_Laplace_criterion(matrix)
Bayes_Laplace_value = Bayes_Laplace_value.tolist()

table = tt.Texttable()
x = [[]]
for i in range(0, len(Walds_value)):
    x.append([matrix[i], Walds_value[i], Maximim_value[i], Laplace_value[i], 
              Hurwitz_value[i], Bayes_Laplace_value[i]])

x.append(['Максимальні значення', max(Walds_value), max(Maximim_value), max(Laplace_value),
          max(Hurwitz_value), max(Bayes_Laplace_value)])

x.append(['Вибрані оптимальні стратегії', Walds_value.index(max(Walds_value))+1, 
          Maximim_value.index(max(Maximim_value))+1, Laplace_value.index(max(Laplace_value))+1,
          Hurwitz_value.index(max(Hurwitz_value))+1, Bayes_Laplace_value.index(max(Bayes_Laplace_value))+1])

table.add_rows(x)
table.set_cols_align(['c','c','c','c','c','c'])
table.set_cols_valign(["m", "m", "m", "m", "m", "m"])
table.header(['Зчитана матриця', 'Критерій Вальда', 'Максимальний Критерій', 'Критерій Лапласа',
            'Критерій Гурвіца', 'Критерій Байеса-Лапласа'])
print(table.draw())