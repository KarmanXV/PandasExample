import pandas as pd


def local(filename):
    data = pd.read_csv(filename, sep=';')
    # print(data)
    age = data.loc[2]['Age']
    grade = data.loc[2]['Grade']
    add = age + grade
    # print(sum)
    return add  # Should be 26


def web(filepath):
    data = pd.read_csv(filepath, sep='\s*,\s*', engine='python')
    # print(data)
    group = data.loc[0]['GroupCategoryID']
    # print(group)
    return group  # Should be 100


local("ExampleFile.csv")
web("http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportGroupsSample.csv")
