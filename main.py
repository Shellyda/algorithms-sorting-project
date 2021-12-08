import sort_algorithm
from generate_random_numbers import get_random_numbers
from time import sleep

# begin = timeit.default_timer()
# end = timeit.default_timer()
# print("Duration: %f" % (end - begin))


def show_five_first_numbers(list_numbers):
    for index in range(5):
        print(f">> {index+1}°) {list_numbers[index]}")


def main():
    case = 0
    while case != 5:
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
            print("A) The first five numbers of the set with not sorted elements:")
            show_five_first_numbers(get_random_numbers(100))
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
