import texttable as tt
import numpy as np

expert_1 = np.loadtxt("expert 1.txt", dtype=int)
expert_2 = np.loadtxt("expert 2.txt", dtype=int)
expert_3 = np.loadtxt("expert 3.txt", dtype=int)
expert_4 = np.loadtxt("expert 4.txt", dtype=int)
expert_5 = np.loadtxt("expert 5.txt", dtype=int)

importance = []
with open('importance.txt', 'r') as file:
    data_importance = file.read().split()
    for elem in data_importance:
        try:
            importance.append(float(elem))
        except ValueError:
            pass

cars = []
with open('Cars.txt', 'r') as file:
    for line in file:
        cars.append(line[:-1])
file.close()        

criterion = []
with open('Criterion.txt', 'r', encoding="utf-8") as file:
    for line in file:
        criterion.append(line[:-1])
file.close()        

price = []
engine = []
transmission = []
steering_wheel_suspension = []
total_weight = []
capacity = []
dimensions = []
for i in range(0, len(cars)):
    price.append(importance[0] * sum([expert_1[i][0],expert_2[i][0],expert_3[i][0],expert_4[i][0],expert_5[i][0]]))
    engine.append(importance[1] * sum([expert_1[i][1],expert_2[i][1],expert_3[i][1],expert_4[i][1],expert_5[i][1]]))
    transmission.append(importance[2] * sum([expert_1[i][2],expert_2[i][2],expert_3[i][2],expert_4[i][2],expert_5[i][2]]))
    steering_wheel_suspension.append(importance[3] * sum([expert_1[i][3],expert_2[i][3],expert_3[i][3],expert_4[i][3],expert_5[i][3]]))
    total_weight.append(importance[4] * sum([expert_1[i][4],expert_2[i][4],expert_3[i][4],expert_4[i][4],expert_5[i][4]]))
    capacity.append(importance[5] * sum([expert_1[i][5],expert_2[i][5],expert_3[i][5],expert_4[i][5],expert_5[i][5]]))
    dimensions.append(importance[6] * sum([expert_1[i][6],expert_2[i][6],expert_3[i][6],expert_4[i][6],expert_5[i][6]]))
  
price = [round(num, 2) for num in price]
engine = [round(num, 2) for num in engine]
transmission = [round(num, 2) for num in transmission]
steering_wheel_suspension = [round(num, 2) for num in steering_wheel_suspension]
total_weight = [round(num, 2) for num in total_weight]
capacity = [round(num, 2) for num in capacity]
dimensions = [round(num, 2) for num in dimensions]

All = [price, engine, transmission, steering_wheel_suspension, total_weight, capacity, dimensions]

Sum = [sum(x) for x in zip(*All)]

table = tt.Texttable()
data = [[]]
i = 0
for i in range(0, len(criterion)):
    data.append([i + 1, criterion[i], importance[i], All[i][0], All[i][1], All[i][2], All[i][3],
                 All[i][4], All[i][5], All[i][6], All[i][7], All[i][8]])
data.append([i + 2, 'Сума', sum(importance), Sum[0], Sum[1], Sum[2], Sum[3], Sum[4], Sum[5], Sum[6], Sum[7], Sum[8]])
table.add_rows(data)
table.set_cols_align(['c','c','c','c','c','c','c','c','c','c','c','c'])
table.set_cols_valign(["m", "m", "m", "m", "m", "m", "m", "m", "m", "m", "m", "m"])
table.set_cols_width((1, 11, 5, 7, 9, 8, 9, 7, 10, 9, 8, 10))
table.header(['№', 'Параметри', 'Вага', cars[0], cars[1], cars[2], cars[3], cars[4], cars[5], cars[6],
              cars[7], cars[8]])
print(table.draw())

