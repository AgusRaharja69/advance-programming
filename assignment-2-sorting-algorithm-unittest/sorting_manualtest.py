'''
I Kadek Agus Wahyu Raharja(23219019)
Sorting Random Interger Data with Bubble Sort Algorithm
and Selection Sort Algorithm

Deskripsi Program: program berisikan contens berupa 
input random data sebanyak 'n' 
(NB: bebas dalam memasukkan jumlah array)
output berupa hasil random data serta hasil sorting 
dengan algoritma yang dipilih
'''
import random
import pandas as pd
import csv
import time
import numpy as np
import array as arr

############ Unit test #########
def unit_test(data):
    for i in range(len(data)-1):
        if data[i] <= data[i+1] :
            Pass = True
            print('test data . . . OK')
        else :
            Pass = False
        assert Pass == True

def import_data(n):
    m = n
    # make array data
    row = arr.array('i',[])
    for i in range(n):
        row.append(i)
    # mix row data m times
    for i in range(m):
        x = random.randint(0,n-1)
        y = random.randint(0,n-1)
        # swap baris(x,y)
        xi = row[x]
        yi = row[y]
        row[y] = xi
        row[x] = yi

    # save in csv format
    f =open(f'{n}integer.csv', 'a', newline='')
    with f:
        writer = csv.writer(f)
        writer.writerows([row])
    
def get_data(n):
    filename = (f'{n}integer.csv')
    dataset = pd.read_csv(filename, header = None)
    dataset = dataset.values
    return dataset

def bubble_sort(data):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                # Swap the elements
                data[i], data[i + 1] = data[i + 1], data[i]
                # Set the flag to True so we'll loop again
                swapped = True

def selection_sort(data):
    # This value of i corresponds to how many values were sorted
    for i in range(len(data)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(data)):
            if data[j] < data[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        data[i], data[lowest_value_index] = data[lowest_value_index], data[i]


def main():    
    print("""Progams contents :\n
                1. Input Data\n
                2. View Data\n
                3. Sorting with Bubble Sort Algorithm \n
                4. Sorting with Selection Sort Algorithm \n""")
    
    mode = int(input('Input selection contents(1,2,3,4) :'))    

    if (mode==1):
        n = int(input('Input numbers of array (10, 100, 500, 1000, or 10000) : \n'))
        import_data(n)
        print('successfully imported data')
    elif (mode==2):
        n = int(input('Input numbers of array (10, 100, 500, 1000, or 10000) : \n'))
        data = get_data(n)
        print(data)

    elif (mode==3):
        print(""" Input type : \n
                1. csv file \n
                2. array data \n""")
        data_type = int(input('input data from (1 or 2):  '))

        if (data_type==1):
            n = int(input('Input numbers of array (10, 100, 500, 1000, or 10000) : \n'))
            start = time.time()
            data = get_data(n)
            print('data source :')
            print(data)
            #sorting data row to row
            row = len(data)
            row_sorting =[]
            for i in range(row):
                row_data = data[i][:]
                bubble_sort(row_data)
                #Start Unit Test
                unit_test(row_data)
                row_sorting.append(row_data)
            sorting = np.array(row_sorting)                
            print('Data with Bubble Sort Algorithm :')
            print(sorting)
        elif (data_type==2):
            data=[]
            n=int(input("Enter size of the list:\n"))
            
            for i in range(n):
                temp=int(input("Enter number to append:\n"))
                data.append(temp)
            start = time.time()
            print('data source :')
            print(data)
            bubble_sort(data)

            #Start Unit Test
            unit_test(data)
            print('Data with Bubble Sort Algorithm :')
            print(data)           
        
        #get time proccesing
        print("Execution time : {:2.4f} seconds".format(time.time() - start))
        

    elif (mode==4):
        print(""" Input type : \n
                1. csv file \n
                2. array data \n""")
        data_type = int(input('input data from (1 or 2):  '))

        if (data_type==1):
            n = int(input('Input numbers of array (10, 100, 500, 1000, or 10000) : \n'))
            start = time.time()
            data = get_data(n)
            print('data source :')
            print(data)

            #sorting data row to row
            row = len(data)
            print(row)
            row_sorting =[]
            for i in range(row):
                row_data = data[i][:]
                selection_sort(row_data)
                #Start Unit Test
                unit_test(row_data)
                row_sorting.append(row_data)
            sorting = np.array(row_sorting)
            print('Data with Selection Sort Algorithm :')
            print(sorting)
        elif (data_type==2):
            data=[]
            n=int(input("Enter size of the list:\n"))
            
            for i in range(n):
                temp=int(input("Enter number to append:\n"))
                data.append(temp)
            start = time.time()
            print('data source :')
            print(data)
            selection_sort(data)

            #Start Unit Test
            unit_test(data)
            print('Data with Selection Sort Algorithm :')
            print(data)         
             
        #get time proccesing
        print("Execution time : {:2.4f} seconds".format(time.time() - start))

    
while True:
    # main program
    Pass = True
    main()
    while True:
        print('')
        answer = str(input('Run program again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print ('Invalid input.')
    if answer == 'y':
        continue
    else:
        break      
