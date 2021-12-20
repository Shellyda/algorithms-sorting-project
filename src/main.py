from numpy import copy
from time import sleep
from utils.functions.index import get_random_numbers, show_five_first_numbers
from utils.libraries.index import (
    Bubble_sort,
    Merge_sort,
    Selection_sort,
    Insertion_sort,
    Get_duration_execution_time,
)

Bubble = Bubble_sort()
Merge = Merge_sort()
Selection = Selection_sort()
Insertion = Insertion_sort()

def Show_Each_Case_Execution_Time(aux_arr):
    print("  I) Elements NOT sorted execution time to sort from smallest to largest:")
    resut_I_Bubble = Get_duration_execution_time.Ordering("Bubble", Bubble.Ascending_ordering, aux_arr[0])
    resut_I_Merge = Get_duration_execution_time.Ordering("Merge", Merge.Ascending_ordering, aux_arr[1])
    resut_I_Selection = Get_duration_execution_time.Ordering("Selection", Selection.Ascending_ordering, aux_arr[2])
    resut_I_Insertion = Get_duration_execution_time.Ordering("Insertion", Insertion.Ascending_ordering, aux_arr[3])

    print("  II) Elements SORTED execution time to sort from smallest to largest:")
    resut_II_Bubble = Get_duration_execution_time.Ordering("Bubble", Bubble.Ascending_ordering, aux_arr[0])
    resut_II_Merge = Get_duration_execution_time.Ordering("Merge", Merge.Ascending_ordering, aux_arr[1])
    resut_II_Selection = Get_duration_execution_time.Ordering("Selection", Selection.Ascending_ordering, aux_arr[2])
    resut_II_Insertion = Get_duration_execution_time.Ordering("Insertion", Insertion.Ascending_ordering, aux_arr[3])

    print("\nE) Average of the runtimes in each scenario and algorithm:")
    print(" - Bubble: {}".format(resut_I_Bubble + resut_II_Bubble/2.0))
    print(" - Merge: {}".format(resut_I_Merge + resut_II_Merge/2.0))
    print(" - Selection: {}".format(resut_I_Selection + resut_II_Selection/2.0))
    print(" - Insertion: {}".format(resut_I_Insertion + resut_II_Insertion/2.0))

def Cases_format(case, len_list):
    aux_list = []
    print("You choosed case {} - equal a {} length list of elements! :)".format(case, len_list))
   
    print("\nC) The ordering time in 3 scenarios:")
    random_list = get_random_numbers(len_list)

    for x in range(4):
        aux_list.append(copy(random_list))
           
    Show_Each_Case_Execution_Time(aux_list)

def main():
    case = 0
    while case != 6:
        print(
            """Which size dataset do you want us to sort? Select one below :) 
[ 1 ] 100
[ 2 ] 1.000
[ 3 ] 10.000
[ 4 ] 100.000
[ 5 ] 1.000.000
[ 6 ] exit program
        """
        )
        case = int(input(">>>> What is your choice? "))
        if case == 1:
            len_list = 100
            aux_list = []
            print("\nYou choosed case {} - equal a {} length list of elements! :)".format(case, len_list))
            first_random_list = get_random_numbers(len_list)

            print("\nA) The first five numbers of the set with NOT sorted elements:")
            show_five_first_numbers(first_random_list)

            print("\n\nB) The first five numbers of sorted list:")
            sorted_list = Bubble.Ascending_ordering(first_random_list)
            show_five_first_numbers(sorted_list)
            
            print("\n\nC) The ordering time in 3 scenarios:")
            random_list = get_random_numbers(len_list)

            for x in range(4):
                aux_list.append(copy(random_list))
           
            Show_Each_Case_Execution_Time(aux_list)
        elif case == 2:
            Cases_format(case,1000)
        elif case == 3:
            Cases_format(case,10000)
        elif case == 4:
            Cases_format(case,100000)
        elif case == 5:
            Cases_format(case,1000000)      
        elif case == 6:
            print("exiting program...")
        else:
            print("not allowed option! :( Choose other...")
        sleep(1.5)
        print("=-=" * 22)

    print("End of program :) See you!")


main()
