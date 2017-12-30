
#Name: Murtaza Khambaty

#Used to generate a sequence of random numbers
import random
#Used for reading and writing to and from the file
import pickle
#Used to calculate the time taken by the algorithm
import time
#Used for plotting the graph
import matplotlib.pyplot as plt
import sys
import matplotlib.patches
sys.setrecursionlimit(10000) #Sets the recursion limit to 10,000

#Loaded a list 'ar' with 999,999 numbers(ranging from 1 to 10,00,000)
ar=random.sample(range(1,1000000),999999)
global time_list_merge_sort
time_list_merge_sort=[]
global time_list_insertion_sort    #Declared some variables globally
time_list_insertion_sort=[]
global avg_time_merge_sort
avg_time_merge_sort=0.0
global avg_time_insertion_sort
avg_time_insertion_sort=0.0
global time_list_quick_sort
time_list_quick_sort=[]
global avg_time_quick_sort
avg_time_quick_sort=0.0

def input(ar):      #A function caleled Input(), reads data from the file and calls the sorting functions
    avg_time_merge_sort=[]
    avg_time_insertion_sort=[]
    avg_time_quick_sort=[]
    input_list=[]


    ar=random.sample(range(1,300000),200000)       #Code to write 200,000 numbers into a list called ar. I wrote the data into the list just once.

    #Referred reading from file and writing to file from stackoverflow (https://stackoverflow.com/questions/35067957/how-to-read-pickle-file)
    with open("data.txt", 'wb') as fp:
        pickle.dump(ar,fp)

    with open("data.txt", 'rb') as fp:
        ar=pickle.load(fp)

    #ar3 = [9]*1000
    #ar1 = [8]*1000
    #ar2 = [7]*1000

    k=180     #A random variable 'k' helps us to read k numbers from the file into the list(k is incremented by 180 after every 10 iterations.
    for i in range (0,20):      #This iterates the loop 20 times. One time foreach dataset(180, 360,540 ..... 3600)

        time_list_merge_sort=[]
        time_list_insertion_sort=[]
        time_list_quick_sort=[]
        sum_time_merge_sort=0.0
        sum_time_insertion_sort=0.0
        sum_time_quick_sort=0.0

        for j in range(0,10):       #Iterates the loop 10 times for each dataset(180*10, 360*10 .... 3600*10)
            ar1=random.sample(ar,k)     #Loads a random sample of data into the list 'ar1' depending upon the value of k. Eg. if k=180, 180 elements will be loaded into ar1)
            ar2=random.sample(ar,k)     #Loads a random sample of data into the list 'ar2' depending upon the value of k. Eg. if k=180, 180 elements will be loaded into ar2)
            ar3=random.sample(ar,k)     #Loads a random sample of data into the list 'ar3' depending upon the value of k. Eg. if k=180, 180 elements will be loaded into ar3)

            #ar1=sorted(ar1,reverse=True)   #Used an inbuilt python function to sort the elements in descending order into ar1
            #ar2=sorted(ar2,reverse=True)   #Used an inbuilt python function to sort the elements in descending order into ar2
            #ar3=sorted(ar3,reverse=True)   #Used an inbuilt python function to sort the elements in descending order into ar3

            #ar1=sorted(ar1,reverse=False)  #Used an inbuilt python function to sort the elements in ascending order into ar1
            #ar2=sorted(ar2,reverse=False)  #Used an inbuilt python function to sort the elements in ascending order into ar2
            #ar3=sorted(ar3,reverse=False)   #Used an inbuilt python function to sort the elements in ascending order into ar3

            start_time_merge_sort=time.time()  #stores the current time into the variable.This is the start time of the algorithm
            merge_sort(ar1)    #Calls the function merge sort by passing ar1
            end_time_merge_sort=time.time()    #Stores the current time into the variable. This is the end time of the algorithm
            total_time_merge_sort=end_time_merge_sort-start_time_merge_sort  #Calculates the total time taken by merge sort to execute.
            time_list_merge_sort.append(total_time_merge_sort)                #Appends the total time into a list
            sum_time_merge_sort=sum_time_merge_sort+time_list_merge_sort[j]  #Calculates the sum of total time.


            start_time_quick_sort=time.time()  #stores the current time into the variable.This is the start time of the algorithm
            quick_sort(ar3,0,len(ar3)-1)    #Calls the function quick sort by passing ar3
            end_time_quick_sort=time.time()    #Stores the current time into the variable. This is the end time of the algorithm
            total_time_quick_sort=end_time_quick_sort-start_time_quick_sort  #Calculates the total time taken by quick sort to execute.
            time_list_quick_sort.append(total_time_quick_sort)                #Appends the total time into a list
            sum_time_quick_sort=sum_time_quick_sort+time_list_quick_sort[j]  #Calculates the sum of total time.




            start_time_insertion_sort=time.time()       #stores the current time into the variable.This is the start time of the algorithm
            insertion_sort(ar2)                         #Calls the function insertion sort by passing ar2
            end_time_insertion_sort=time.time()         #Stores the current time into the variable. This is the end time of the algorithm
            total_time_insertion_sort=end_time_insertion_sort-start_time_insertion_sort #Calculates the total time taken by insertion sort to execute.
            time_list_insertion_sort.append(total_time_insertion_sort)      #Appends the total time into a list
            sum_time_insertion_sort=sum_time_insertion_sort+time_list_insertion_sort[j]     #Calculates the sum of total time.




        avg_time_merge_sort.append(sum_time_merge_sort/10)        #Appends the avg time of 10 merge sorts into a list.
        avg_time_insertion_sort.append(sum_time_insertion_sort/10)  #Appends the avg time of 10 insertion sorts into a list.
        avg_time_quick_sort.append(sum_time_quick_sort/10)          #Appends the avg time of 10 quick sorts into a list.

        k=k+180      #Increments k by 180

    for i in range(1,21):       #Creates the list of the number of elemtents in one dataset. Used for plotting the graph
        input_list.append(180*i)


    plt.plot(input_list,avg_time_insertion_sort,'b--',input_list,avg_time_merge_sort,'r--',input_list,avg_time_quick_sort,'g--')    #Plots a graph of the time taken by the 3 sorting algorithms
    blue_line = matplotlib.patches.Patch(color='blue',label= 'Insertion sort')      #Creates a legend on the graph
    red_line = matplotlib.patches.Patch(color='red',label= 'Merge sort')
    green_line = matplotlib.patches.Patch(color='green', label= 'Quick sort')
    plt.legend(handles=[blue_line,red_line,green_line])
    plt.show()


def insertion_sort(ar):
    #Performs insertion sort
    n=len(ar)

    for j in range (1,n):
        key=ar[j]
        i=j-1
        while(i>=0 and ar[i]>key):
            ar[i+1]=ar[i]
            i=i-1

        ar[i+1] = key

def merge_sort(ar):     #Performs merge sort
    len_list=len(ar)
    left=[]
    right=[]
    if(len_list<=1):
        return
    else:
        mid = int(len_list/2)

        for i in range (0,mid):
            left.append(ar[i])

        for i in range(mid,len_list):
            right.append(ar[i])

        merge_sort(left)
        merge_sort(right)
        merge(ar,left,right)


def merge(ar,left,right):
    len_left=len(left)
    len_right=len(right)
    i=0
    j=0
    k=0

    while(i<len_left and j<len_right):
        if(left[i]>right[j]):
            ar[k]=right[j]
            j=j+1
            k=k+1
        else:
            ar[k]=left[i]
            i=i+1
            k=k+1

    while(i<len_left):
        ar[k]=left[i]
        i=i+1
        k=k+1

    while(j<len_right):
        ar[k]=right[j]
        j=j+1
        k=k+1

    return(ar)

def quick_sort(ar, start_index, end_index):     #Performs quick sort

    #print(ar)
    if(start_index>=end_index):
        return
    else:
        partition_index = partition(ar,start_index, end_index)
        quick_sort(ar,start_index,partition_index-1)
        #print("---------------")
        quick_sort(ar,partition_index+1,end_index)

def partition(ar,start_index, end_index):
    pivot = ar[end_index]
    x = start_index

    for i in range (start_index,end_index):
        if(ar[i]<=pivot):
            temp = ar[i]
            ar[i] = ar[x]
            ar[x] = temp
            x=x+1
    temp = ar[x]
    ar[x] = ar[end_index]
    ar[end_index] = temp
    return(x)



#Calls the method input(), which inturn calls merge, quick and insertion sort
input(ar)

