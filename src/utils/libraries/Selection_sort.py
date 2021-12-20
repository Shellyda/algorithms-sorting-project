class Selection_sort:
    def Ascending_ordering(self, list_elements):
        for index in range(0, len(list_elements)):
            min_index = index

            for right in range(index + 1, len(list_elements)):
                if list_elements[right] < list_elements[min_index]:
                    min_index = right

            list_elements[index], list_elements[min_index] = (
                list_elements[min_index],
                list_elements[index],
            )
        return list_elements
