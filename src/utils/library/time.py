import timeit
from src.utils.functions.generate_random_numbers import get_random_numbers


class List:
    def __init__(self):
        self.head = None

    def recem(random_list_elements):
        begin = timeit.default_timer()
        random_list_elements = get_random_numbers(random_list_elements)
        end = timeit.default_timer() - begin
        print("Tempo de execução recém criado: {} segundos".format(end))
        return random_list_elements

    def ordering_time(random_list_elements, algoritmo):
        begin = timeit.default_timer()
        algoritmo(random_list_elements)
        end = timeit.default_timer() - begin
        print("Tempo de execução ordenado do menor para o maior: {} segundos".format(end))

    def inverse_time(random_list_elements):
        begin = timeit.default_timer()
        #sorted_list_elements = SP.Insertion_sort(random_list_elements)
        end = timeit.default_timer() - begin
        print("Tempo de execução ordenado do maior para o menor Insertion Sort: {} segundos".format(end))
