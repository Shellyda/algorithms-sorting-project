import timeit
from utils.functions.index import get_random_numbers


class Get_duration_execution_time:
    def __init__(self):
        self.head = None

    def creation_first_random_list(random_list):
        begin = timeit.default_timer()
        random_list = get_random_numbers(random_list)
        end = timeit.default_timer()
        print("Tempo de execução recém criado: {} segundos".format(end - begin))

    def ordering(algorithm):
        begin = timeit.default_timer()
        algorithm()
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
