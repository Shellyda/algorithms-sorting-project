import numpy as np
from src.utils.library.sorting_power import Sorting_power as SP
from src.utils.functions.show_numbers import show_five_first_numbers
from src.utils.library.time import List
from time import sleep


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
            print(
                """You choosed case 1 - equal a 100 length list of elements!
A) The first five numbers of the set with NOT sorted elements:"""
            )
            random_list = List.recem(100)
            show_five_first_numbers(random_list)

            np.save('algoritmo100.npy', random_list)  #save
            arrayBubble = np.load('algoritmo100.npy')  # load
            arrayInsertion = np.load('algoritmo100.npy')
            arrayMerge = np.load('algoritmo100.npy')
            arraySelection = np.load('algoritmo100.npy')

            array5 = random_list[0:5]
            #np.save('algoritmo5.npy', array5)  #save five
            #arrayFive = np.load('algoritmo5.npy')
            #print(arrayFive)
            print("\nB) The first five numbers of sorted list:")
            sorted_list = SP.Bubble_sort(array5)
            show_five_first_numbers(sorted_list)

            print("\nRuntime:")
            print("\nBuble Sort:")
            List.ordering_time(arrayBubble, SP.Bubble_sort)

            print("\nInsertion Sort:")
            List.ordering_time(arrayInsertion, SP.Insertion_sort)

            print("\nMerge Sort:")
            List.ordering_time(arrayMerge, SP.Merge_sort)

            print("\nSelection Sort:")
            List.ordering_time(arraySelection, SP.selection_sort)


        elif case == 2:
            print("\nRuntime:")
            array = List.recem(1000)
            np.save('algoritmo2.npy', array)  #save

            arrayBubble = np.load('algoritmo2.npy') #load
            arrayInsertion = np.load('algoritmo2.npy')
            arrayMerge = np.load('algoritmo2.npy')
            arraySelection = np.load('algoritmo2.npy')

            print("\nBuble Sort:")
            List.ordering_time(arrayBubble, SP.Bubble_sort)

            print("\nInsertion Sort:")
            List.ordering_time(arrayInsertion, SP.Insertion_sort)

            print("\nMerge Sort:")
            List.ordering_time(arrayMerge, SP.Merge_sort)

            print("\nSelection Sort:")
            List.ordering_time(arraySelection, SP.selection_sort)


        elif case == 3:
            print("\nRuntime:")
            array = List.recem(10000)
            np.save('algoritmo3.npy', array)  # save

            arrayBubble = np.load('algoritmo3.npy')  # load
            arrayInsertion = np.load('algoritmo3.npy')
            arrayMerge = np.load('algoritmo3.npy')
            arraySelection = np.load('algoritmo3.npy')

            print("\nBuble Sort:")
            List.ordering_time(arrayBubble, SP.Bubble_sort)

            print("\nInsertion Sort:")
            List.ordering_time(arrayInsertion, SP.Insertion_sort)

            print("\nMerge Sort:")
            List.ordering_time(arrayMerge, SP.Merge_sort)

            print("\nSelection Sort:")
            List.ordering_time(arraySelection, SP.selection_sort)

        elif case == 4:
            print("\nRuntime:")
            array = List.recem(100000)
            np.save('algoritmo4.npy', array)  # save

            arrayBubble = np.load('algoritmo4.npy')  # load
            arrayInsertion = np.load('algoritmo4.npy')
            arrayMerge = np.load('algoritmo4.npy')
            arraySelection = np.load('algoritmo4.npy')

            print("\nBuble Sort:")
            List.ordering_time(arrayBubble, SP.Bubble_sort)

            print("\nInsertion Sort:")
            List.ordering_time(arrayInsertion, SP.Insertion_sort)

            print("\nMerge Sort:")
            List.ordering_time(arrayMerge, SP.Merge_sort)

            print("\nSelection Sort:")
            List.ordering_time(arraySelection, SP.selection_sort)

        elif case == 5:
            print("\nRuntime:")
            array = List.recem(1000000)
            np.save('algoritmo5.npy', array)  # save

            arrayBubble = np.load('algoritmo5.npy')  # load
            arrayInsertion = np.load('algoritmo5.npy')
            arrayMerge = np.load('algoritmo5.npy')
            arraySelection = np.load('algoritmo5.npy')

            print("\nBuble Sort:")
            List.ordering_time(arrayBubble, SP.Bubble_sort)

            print("\nInsertion Sort:")
            List.ordering_time(arrayInsertion, SP.Insertion_sort)

            print("\nMerge Sort:")
            List.ordering_time(arrayMerge, SP.Merge_sort)

            print("\nSelection Sort:")
            List.ordering_time(arraySelection, SP.selection_sort)
        elif case == 6:
            print("exiting program...")
        else:
            print("not allowed option! :( Choose other...")
        sleep(1.5)
        print("=-=" * 22)


    print("End of program :) See you!")


main()

