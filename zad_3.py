import pandas as pd
import csv



with open ("zadanie_4_triangle_big.txt", "rt") as file:
    reader = csv.reader(file, delimiter=' ', skipinitialspace=True)
    data = list()
    for line in reader:
        line = filter(None,line)
        line = list(map(int, line))
        line.extend([0] * (999 - len(line)))
        data.append(line)


data = pd.DataFrame(data)


def Add_V(df, x, z):
    for row in range(x - 1, -1, -1):
        for col in range(row + 1):


            if (df.iloc[row + 1,col] > df.iloc[row + 1,col + 1]):
                df.iloc[row,col] += df.iloc[row + 1,col]
            else:
                df.iloc[row,col] += df.iloc[row + 1,col + 1]

    return df.iloc[0,0]

print(Add_V(data,999,999))



# rozmiar maciezy data to (999,2998)

print(data.iloc[1,1])
print(data.shape)
