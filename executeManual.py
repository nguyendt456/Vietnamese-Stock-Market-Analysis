from manualExport import manualexport

nameofCophieu = 'DVP'

rawData = '''
Q4 2020	Q1 2021	Q2 2021	Q3 2021	Q4 2021
1. Tổng doanh thu hoạt động kinh doanh	
139,441	132,246	166,337	156,636	153,358
2. Các khoản giảm trừ doanh thu	
0	0	0	0	0
3. Doanh thu thuần (1)-(2)	
139,441	132,246	166,337	156,636	153,358
4. Giá vốn hàng bán	
97,794	59,016	61,245	80,067	88,879
5. Lợi nhuận gộp (3)-(4)	
41,648	73,230	105,091	76,569	64,479
6. Doanh thu hoạt động tài chính	
29,854	4,184	11,383	38,229	28,618

7. Chi phí tài chính	
168	0	74	70	111
-Trong đó: Chi phí lãi vay	
0\t0\t0\t0\t0
8. Phần lợi nhuận hoặc lỗ trong công ty liên kết liên doanh	
0	0	0	0	0
9. Chi phí bán hàng	
0	0	0	0	0
10. Chi phí quản lý doanh nghiệp	
13,539	12,789	14,740	15,711	17,414
11. Lợi nhuận thuần từ hoạt động kinh doanh (5)+(6)-(7)+(8)-(9)-(10)	
57,794	64,625	101,661	99,018	75,572
12. Thu nhập khác	
8	452	11	309	14
13. Chi phí khác	
0	263	0	0	2,100
14. Lợi nhuận khác (12)-(13)	
8	189	11	309	-2,086
15. Tổng lợi nhuận kế toán trước thuế (11)+(14)	
57,802	64,815	101,672	99,327	73,486
16. Chi phí thuế TNDN hiện hành	
11,458	13,119	20,395	13,795	14,864
17. Chi phí thuế TNDN hoãn lại	
0	0	0	0	0
18. Chi phí thuế TNDN (16)+(17)	
11,458	13,119	20,395	13,795	14,864
19. Lợi nhuận sau thuế thu nhập doanh nghiệp (15)-(18)	
46,344	51,696	81,277	85,532	58,622
20. Lợi nhuận sau thuế của cổ đông không kiểm soát	
0	0	0	0	0
21. Lợi nhuận sau thuế của cổ đông của công ty mẹ (19)-(20)	
46,344	51,696	81,277	85,532	58,622
'''



data = manualexport(rawData)
data.to_csv('{name}.csv'.format(name = nameofCophieu), index=False)