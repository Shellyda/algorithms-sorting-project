class Selection_sort:
    def __init__(self, list_elements):
        self.list_elements = list_elements

    def Ascending_ordering(self):
        for index in range(0, len(self.list_elements)):
            min_index = index

            for right in range(index + 1, len(self.list_elements)):
                if self.list_elements[right] < self.list_elements[min_index]:
                    min_index = right

            self.list_elements[index], self.list_elements[min_index] = (
                self.list_elements[min_index],
                self.list_elements[index],
            )
        return self.list_elements
