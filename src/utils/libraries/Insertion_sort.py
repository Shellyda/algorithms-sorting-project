class Insertion_sort:
    def Ascending_ordering(self, list_elements):
        if not len(list_elements) == 0:
            for i in range(1, len(list_elements)):
                aux = list_elements[i]
                j = i - 1
                while aux < list_elements[j] and j >= 0:
                    list_elements[j + 1] = list_elements[j]
                    j -= 1
                list_elements[j + 1] = aux
            return list_elements
