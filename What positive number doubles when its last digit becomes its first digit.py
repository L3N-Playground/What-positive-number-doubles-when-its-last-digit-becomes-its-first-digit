#What positive number doubles when its last digit becomes its first digit?
#What Positive Number Doubles When The Last Digit Moves To The First Digit?
#https://www.youtube.com/watch?v=1lHDCAIsyb8 [28.07.2021, 12:18]



import time
time_start = time.time()
#range of index
for index_start in range(0,10**20):
    index_doubles = index_start * 2
    #length of the number
    index_start_length = int(len(str(index_start)))
    #if the number have only one digit
    if index_start_length <= 1:
        index_moved_digit = index_start
    #the digit can only moved if the number have atleast 2 digits
    else:
        index_start_last_digit = str(index_start)[(index_start_length-1):]
        index_start_body_digits = str(index_start)[:(index_start_length-1)]
        index_moved_digit = index_start_last_digit + index_start_body_digits
        index_moved_digit = int(index_moved_digit)
    #compares the doubled number with the moved digit number
    if index_doubles == index_moved_digit:
        print(index_start,index_moved_digit)
#time for finishing the whole programm
print("time required: ", time.time() - time_start)



#results:
#105.263.157.894.736.842 -- 210.526.315.789.473.684


