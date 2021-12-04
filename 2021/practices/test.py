numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)




   while col in range(len(boards[b][0])) and coltest == False:
        coltest = len(set(ele[col] for ele in boards[b])) == 1
        col+=1
