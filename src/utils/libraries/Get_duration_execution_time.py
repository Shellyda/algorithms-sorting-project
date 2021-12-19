import timeit
from utils.functions.index import get_random_numbers


class Get_duration_execution_time:
    def __init__(self):
        self.head = None

    def creation_first_random_list(length):
        begin = timeit.default_timer()
        first_random_list = get_random_numbers(length)
        end = timeit.default_timer()
        print("Time of executin newly created random list of numbers with {} length: {} seconds".format(length,end - begin))
        return first_random_list

    def ordering(algorithm, random_list):
        begin = timeit.default_timer()
        algorithm(random_list)
        end = timeit.default_timer()
        print(
            "Tempo de execução ordenado do menor para o maior: {} segundos".format(
                end - begin
            )
        )

    def inverse_ordering(random_list):
        begin = timeit.default_timer()
        # sorted_list_elements = SP.Insertion_sort(random_list)
        end = timeit.default_timer()
        print(
            "Tempo de execução ordenado do maior para o menor Insertion Sort: {} segundos".format(
                end - begin
            )
        )
