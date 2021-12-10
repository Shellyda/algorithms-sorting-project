import timeit

from utils.library.sorting_power import Sorting_power as SP
from utils.functions.generate_random_numbers import get_random_numbers
from utils.functions.show_numbers import show_five_first_numbers
from time import sleep

# begin = timeit.default_timer()
# end = timeit.default_timer()
# print("Duration: %f" % (end - begin))


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
            random_list_elements = get_random_numbers(100)
            show_five_first_numbers(random_list_elements)
            print("\nB) The first five numbers of sorted list:")

            #Ordenacao e time: bubble sort
            begin = timeit.default_timer()
            sorted_list_elements = SP.Bubble_sort(random_list_elements)
            end = timeit.default_timer() - begin
            show_five_first_numbers(sorted_list_elements)

            print("\nC) Runtime:")
            print("Tempo de execução Bubble Sort: {} segundos".format(end))

        elif case == 2:
            random_list_elements2 = get_random_numbers(1000)
            #Ordenacao e time: bubble sort
            begin = timeit.default_timer()
            sorted_list_elements2 = SP.Bubble_sort(random_list_elements2)
            end = timeit.default_timer() - begin
            print("Tempo de execução Bubble Sort: {} segundos".format(end))

        elif case == 3:
            random_list_elements3 = get_random_numbers(10000)
            #Ordenacao e time: bubble sort
            begin = timeit.default_timer()
            sorted_list_elements3 = SP.Bubble_sort(random_list_elements3)
            end = timeit.default_timer() - begin
            print("Tempo de execução Bubble Sort: {} segundos".format(end))

        elif case == 4:
            random_list_elements4 = get_random_numbers(100000)
            # Ordenacao e time: bubble sort
            begin = timeit.default_timer()
            sorted_list_elements4 = SP.Bubble_sort(random_list_elements4)
            end = timeit.default_timer() - begin
            print("Tempo de execução Bubble Sort: {} segundos".format(end))

        elif case == 5:
            random_list_elements5 = get_random_numbers(1000000)
            # Ordenacao e time: bubble sort
            begin = timeit.default_timer()
            sorted_list_elements5 = SP.Bubble_sort(random_list_elements5)
            end = timeit.default_timer() - begin
            print("Tempo de execução Bubble Sort: {} segundos".format(end))

        else:
            print("not allowed option! :( Choose other...")
        sleep(1.5)
        print("=-=" * 22)

    print("End of program :) See you!")


main()
