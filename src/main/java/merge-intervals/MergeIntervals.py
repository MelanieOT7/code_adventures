def merge_intervals(interval):
    new_list = []
    initial = 0
    for i in interval:
        if i[0] > initial:
            _lst = []
            initial = i[1]
            _lst = i
            new_list.append(_lst)
            continue
        else:
            list = []
            list.append(_lst[0])
            list.append(i[1])
            new_list.pop()
            new_list.append(list)
           
            
        
        
    return new_list

# print(merge_intervals( [[1,4],[4,5]]))