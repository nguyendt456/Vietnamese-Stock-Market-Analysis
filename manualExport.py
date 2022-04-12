from tempfile import TemporaryDirectory
import numpy as np
import pandas as pd


def manualexport(rawData):
    lines = rawData.split('\n')

    print("#######Columns Content########")
    DataFrameColumns = []
    statisticsData = []
    DataFrameColumns.append("Index")
    for columns in lines:    
        theIndex = columns[0:3].find('.')
        if theIndex != -1:
            print(columns[theIndex + 2 : ])
            DataFrameColumns.append(columns[theIndex + 2 : ].rstrip())
            continue
        if columns[0:3].find('-T') != -1:
            print(columns[theIndex + 12 : ])
            DataFrameColumns.append(columns[theIndex + 12 : ].rstrip())
            continue
        if columns == '':
            continue
        statisticsData.append(columns.rstrip())
    statisticsData = statisticsData[1 : ]
    print("##################################################\n")

    data = pd.DataFrame(data=[], columns=DataFrameColumns)

    indexRows = []
    i = 0
    while i < len(lines[1]):
        indexRows.append(lines[1][i : i + 8].rstrip())
        i = i + 8
    data['Index'] = indexRows

    a = 0
    for columnsElement in statisticsData:
        columnsElement = columnsElement.split('\t')
        TemporaryData = []
        for i in columnsElement:
            TemporaryData.append(int(i.replace(',', '')))
        a += 1
        data.iloc[:, a] = TemporaryData
    return data
