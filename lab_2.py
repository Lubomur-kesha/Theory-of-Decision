import texttable as tt

with open('lab 2.txt') as fd:
    for n, line in enumerate(fd):
        if n == 0:
            A = line.strip()
        elif n == 1:
            B = line.strip()
        elif n == 2:
            C = line.strip()
fd.close()

A = A.split(' ')
B = B.split(' ')
C = C.split(' ')

A = [float(i) for i in A]
B = [float(i) for i in B]
C = [float(i) for i in C]

incomeA = 5 * A[1]
wasteA = 5 * A[3]
average_expected_win_A_for_5_years = incomeA * A[2] + wasteA * A[4] - A[0]

incomeB = 5 * B[1]
wasteB = 5 * B[3]
average_expected_win_B_for_5_years = 5 * B[1] * B[2] + 5 * B[3] * B[4] - B[0]

incomeA1 = 4 * A[1]
wasteA1 = 4 * A[3]
average_expected_win_A_for_4_years = incomeA1 * C[2] + wasteA1 * C[3] - A[0]

incomeB1 = 4 * B[1]
wasteB1 = 4 * B[3]
average_expected_win_B_for_4_years = incomeB1 * C[2] + wasteB1 * C[3] - B[0]

if average_expected_win_A_for_4_years > average_expected_win_B_for_4_years:
    average_expected_win_for_4_years = average_expected_win_A_for_4_years
else:
    average_expected_win_for_4_years = average_expected_win_B_for_4_years
    
average_expected_win_C1_for_4_years = C[0] * average_expected_win_for_4_years
average_expected_win_C2_for_4_years = C[1] * 0

if average_expected_win_C1_for_4_years > average_expected_win_C2_for_4_years:
    average_expected_win_C_for_5_years = average_expected_win_C1_for_4_years
else:
    average_expected_win_C_for_5_years = average_expected_win_C2_for_4_years

print('A strategy:')
tableA = tt.Texttable()
dataA = [[]]
dataA.append([A[0], A[1], A[2], A[3], A[4], incomeA, wasteA, average_expected_win_A_for_5_years,
              ])
tableA.add_rows(dataA)
tableA.set_cols_align(['c','c','c','c','c','c','c','c'])
tableA.header(['M1', 'D1', 'P1', 'D2', 'P2', 'income for 5 years', 'waste for 5 years', 
               'expected avarage win A'])
print(tableA.draw())

print('B strategy:')
tableB = tt.Texttable()
dataB = [[]]
dataB.append([B[0], B[1], B[2], B[3], B[4], incomeB, wasteB, average_expected_win_B_for_5_years])
tableB.add_rows(dataB)
tableB.set_cols_align(['c','c','c','c','c','c','c','c'])
tableB.header(['M2', 'D1', 'P1', 'D2', 'P2', 'income for 5 years', 'waste for 5 years', 
               'expected avarage win B'])
print(tableB.draw())

print('C strategy:')
tableA1 = tt.Texttable()
dataA1 = [[]]
dataA1.append([A[0], A[1], C[2], A[3], C[3], incomeA1, wasteA1, average_expected_win_A_for_4_years])
tableA1.add_rows(dataA1)
tableA1.set_cols_align(['c','c','c','c','c','c','c','c'])
tableA1.header(['M1', 'D1', 'P1', 'D2', 'P2', 'income for 4 years', 'waste for 4 years', 
               'expected avarage win A1'])
print(tableA1.draw())

tableB1 = tt.Texttable()
dataB1 = [[]]
dataB1.append([B[0], B[1], C[2], B[3], C[3], incomeB1, wasteB1, average_expected_win_B_for_4_years])
tableB1.add_rows(dataB1)
tableB1.set_cols_align(['c','c','c','c','c','c','c','c'])
tableB1.header(['M2', 'D1', 'P1', 'D2', 'P2', 'income for 4 years', 'waste for 4 years', 
               'expected avarage win A2'])
print(tableB1.draw())

tableC = tt.Texttable()
dataC = [[]]
dataC.append([C[0], C[1], average_expected_win_A_for_4_years, average_expected_win_B_for_4_years,
              average_expected_win_C1_for_4_years, average_expected_win_C2_for_4_years,
              average_expected_win_C_for_5_years])
tableC.add_rows(dataC)
tableC.set_cols_align(['c','c','c','c','c','c','c'])
tableC.header(['P3', 'P4', 'expected avarage win for 4 years for A', 'expected avarage win for 4 years for B',
               'expected avarage win for 5 years for C1', 'expected avarage win for 5 years for C2',
               'expected avarage win C'])
print(tableC.draw())

win_strategy = max(average_expected_win_A_for_5_years, average_expected_win_B_for_5_years,
                   average_expected_win_C_for_5_years)

if win_strategy == average_expected_win_A_for_5_years:
    print('Win strategy is A, because of average expected win is ', win_strategy)
    print('It is better to build a large plant')
elif win_strategy == average_expected_win_B_for_5_years:
    print('Win strategy is B, because of average expected win is ', win_strategy)
    print('It is better to build a mini plant')
elif win_strategy == average_expected_win_C_for_5_years:
    print('Win strategy is C, because of average expected win is ', win_strategy)
    print('It is better to postpone construction')