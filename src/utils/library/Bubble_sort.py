class Bubble_sort:
    def __init__(self, list_elements):
        self.list_elements = list_elements

    def Ascending_ordering(self):
        if not len(self.list_elements) == 0:
            count = 0
            swap_place = True
            while swap_place and count < len(self.list_elements) - 1:
                count += 1
                swap_place = False
                for index in range(0, len(self.list_elements) - count):
                    if self.list_elements[index] > self.list_elements[index + 1]:
                        self.list_elements[index], self.list_elements[index + 1] = (
                            self.list_elements[index + 1],
                            self.list_elements[index],
                        )
                        swap_place = True
            return self.list_elements

    # def descending ordering(self):
