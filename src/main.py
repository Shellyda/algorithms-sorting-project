import numpy as np
from time import sleep
from utils.functions.index import get_random_numbers, show_five_first_numbers
from utils.libraries.index import (
    Bubble_sort,
    Merge_sort,
    Selection_sort,
    Insertion_sort,
    Get_duration_execution_time,
)

BS = Bubble_sort()

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
            print("\nYou choosed case 1 - equal a 100 length list of elements!\n")
            first_random_list = Get_duration_execution_time.creation_first_random_list(100)
            print("\nA) The first five numbers of the set with NOT sorted elements:")
            show_five_first_numbers(first_random_list)

            print("\nB) The first five numbers of sorted list:")
            sorted_list = BS.Ascending_ordering(first_random_list)
            show_five_first_numbers(sorted_list)

            print("\nRuntime:")
            print("\nBubble Sort:")
            Get_duration_execution_time.ordering(BS.Ascending_ordering, get_random_numbers(100))

            # print("\nInsertion Sort:")
            # Get_duration_execution_time.ordering_time(random_list, SP.Insertion_sort)

            # print("\nMerge Sort:")
            # Get_duration_execution_time.ordering_time(random_list, SP.Merge_sort)

            # print("\nSelection Sort:")
            # Get_duration_execution_time.ordering_time(random_list, SP.selection_sort)

        elif case == 2:
            print("\nRuntime:")
            array = Get_duration_execution_time.creation_first_random_list(1000)
            np.save("algoritmo2.npy", array)  # save

            arrayBubble = np.load("algoritmo2.npy")  # load
            arrayInsertion = np.load("algoritmo2.npy")
            arrayMerge = np.load("algoritmo2.npy")
            arraySelection = np.load("algoritmo2.npy")

            print("\nBuble Sort:")
            Get_duration_execution_time.ordering_time(arrayBubble, SP.Bubble_sort)

            print("\nInsertion Sort:")
            Get_duration_execution_time.ordering_time(arrayInsertion, SP.Insertion_sort)

            print("\nMerge Sort:")
            Get_duration_execution_time.ordering_time(arrayMerge, SP.Merge_sort)

            print("\nSelection Sort:")
            Get_duration_execution_time.ordering_time(arraySelection, SP.selection_sort)

        elif case == 3:
            print("\nRuntime:")
            array = Get_duration_execution_time.creation_first_random_list(10000)

            print("\nBuble Sort:")
            Get_duration_execution_time.ordering_time(array, SP.Bubble_sort)

            print("\nInsertion Sort:")
            Get_duration_execution_time.ordering_time(array, SP.Insertion_sort)

            print("\nMerge Sort:")
            Get_duration_execution_time.ordering_time(array, SP.Merge_sort)

            print("\nSelection Sort:")
            Get_duration_execution_time.ordering_time(array, SP.selection_sort)

        elif case == 4:
            print("\nRuntime:")
            array = Get_duration_execution_time.creation_first_random_list(100000)

            print("\nBuble Sort:")
            Get_duration_execution_time.ordering_time(array, SP.Bubble_sort)

            print("\nInsertion Sort:")
            Get_duration_execution_time.ordering_time(array, SP.Insertion_sort)

            print("\nMerge Sort:")
            Get_duration_execution_time.ordering_time(array, SP.Merge_sort)

            print("\nSelection Sort:")
            Get_duration_execution_time.ordering_time(array, SP.selection_sort)

        elif case == 5:
            print("\nRuntime:")
            array = Get_duration_execution_time.creation_first_random_list(1000000)

            print("\nBuble Sort:")
            Get_duration_execution_time.ordering_time(array, SP.Bubble_sort)

            print("\nInsertion Sort:")
            Get_duration_execution_time.ordering_time(array, SP.Insertion_sort)

            print("\nMerge Sort:")
            Get_duration_execution_time.ordering_time(array, SP.Merge_sort)

            print("\nSelection Sort:")
            Get_duration_execution_time.ordering_time(array, SP.selection_sort)
        elif case == 6:
            print("exiting program...")
        else:
            print("not allowed option! :( Choose other...")
        sleep(1.5)
        print("=-=" * 22)

    print("End of program :) See you!")


main()
