from operator import index
import pandas as pd
from manualExport import manualexport

nameofCophieu = 'DVP'

rawdata = '''
Q1 2009	Q2 2009	Q3 2009	Q4 2009	Q1 2010
1. Tổng doanh thu hoạt động kinh doanh	
47,505	69,340	71,129	76,466	52,919
2. Các khoản giảm trừ doanh thu	
0	0	0	0	0
3. Doanh thu thuần (1)-(2)	
47,505	69,340	71,129	76,466	52,919
4. Giá vốn hàng bán	
32,341	42,304	40,241	49,165	34,102
5. Lợi nhuận gộp (3)-(4)	
15,164	27,036	30,888	27,301	18,817
6. Doanh thu hoạt động tài chính	
839	1,728	3,178	6,048	4,556

7. Chi phí tài chính	
1,455	1,135	1,666	4,274	2,319
-Trong đó: Chi phí lãi vay	
1,450	1,004	1,394	1,225	1,854
8. Phần lợi nhuận hoặc lỗ trong công ty liên kết liên doanh	
0	0	0	0	0
9. Chi phí bán hàng	
0	0	0	0	0
10. Chi phí quản lý doanh nghiệp	
2,144	2,192	2,420	5,338	2,292
11. Lợi nhuận thuần từ hoạt động kinh doanh (5)+(6)-(7)+(8)-(9)-(10)	
12,404	25,438	29,980	23,737	18,762
12. Thu nhập khác	
88	38	40	37	42
13. Chi phí khác	
0	0	0	0	0
14. Lợi nhuận khác (12)-(13)	
88	38	40	37	42
15. Tổng lợi nhuận kế toán trước thuế (11)+(14)	
12,492	25,476	30,020	23,774	18,803
16. Chi phí thuế TNDN hiện hành	
874	1,793	10,940	4,783	1,880
17. Chi phí thuế TNDN hoãn lại	
0	0	0	0	0
18. Chi phí thuế TNDN (16)+(17)	
874	1,793	10,940	4,783	1,880
19. Lợi nhuận sau thuế thu nhập doanh nghiệp (15)-(18)	
11,618	23,683	19,080	18,991	16,923
20. Lợi nhuận sau thuế của cổ đông không kiểm soát	
0	0	0	0	0
21. Lợi nhuận sau thuế của cổ đông của công ty mẹ (19)-(20)	
11,618	23,683	19,080	18,991	16,923
'''
old_dataframe = pd.read_csv('{name}.csv'.format(name=nameofCophieu))

new_dataframe = manualexport(rawdata)


print(old_dataframe['Index'].values)

print(new_dataframe['Index'].values)

print('1: ', pd.concat([old_dataframe, new_dataframe]).drop_duplicates().reset_index(drop=True)['Index'].values)

print('2: ', pd.concat([new_dataframe, old_dataframe]).drop_duplicates().reset_index(drop=True)['Index'].values)

UserChoice = input('Choose 1 or 2: ')

if(UserChoice == '1'):
    pd.concat([old_dataframe, new_dataframe]).drop_duplicates().reset_index(drop=True).to_csv('{name}.csv'.format(name=nameofCophieu), index=False)
else:
    pd.concat([new_dataframe, old_dataframe]).drop_duplicates().reset_index(drop=True).to_csv('{name}.csv'.format(name=nameofCophieu), index=False)