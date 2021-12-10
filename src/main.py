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
            random_list = get_random_numbers(100)
            five_first = random_list[0:5]
            show_five_first_numbers(five_first)

            print("\nB) The first five numbers of sorted list:")
            sorted_list_elements = SP.Bubble_sort(five_first)
            show_five_first_numbers(sorted_list_elements)
        elif case == 2:
            print("teste")
        elif case == 6:
            print("exiting program...")
        else:
            print("not allowed option! :( Choose other...")
        sleep(1.5)
        print("=-=" * 22)

    print("End of program :) See you!")


main()
