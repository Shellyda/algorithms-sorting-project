class Insertion_sort:
    def __init__(self, list_elements):
        self.list_elements = list_elements

    def Ascending_ordering(self):
        if not len(self.list_elements) == 0:
            for i in range(1, len(self.list_elements)):
                aux = self.list_elements[i]
                j = i - 1
                while aux < self.list_elements[j] and j >= 0:
                    self.list_elements[j + 1] = self.list_elements[j]
                    j -= 1
                self.list_elements[j + 1] = aux
            return self.list_elements
