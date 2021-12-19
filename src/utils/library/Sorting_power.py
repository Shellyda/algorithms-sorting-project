class Sorting_power:
    def __init__(self, list_elements):
        self.list_elements = list_elements

    def Bubble_sort(self):
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

    def Insertion_sort(self):
        if not len(self.list_elements) == 0:
            for i in range(1, len(self.list_elements)):
                aux = self.list_elements[i]
                j = i - 1
                while aux < self.list_elements[j] and j >= 0:
                    self.list_elements[j + 1] = self.list_elements[j]
                    j -= 1
                self.list_elements[j + 1] = aux
            return self.list_elements

    def Merge_sort(self):
        if not len(self.list_elements) == 0:
            middle = len(self.list_elements) // 2
            left_part = self.list_elements[:middle]
            right_part = self.list_elements[middle:]

            left_part.sort()
            right_part.sort()

            Iterator_main = i = j = 0

            while i < len(left_part) and j < len(right_part):
                if left_part[i] < right_part[j]:
                    self.list_elements[Iterator_main] = left_part[i]
                    i += 1
                else:
                    self.list_elements[Iterator_main] = right_part[j]
                    j += 1
                Iterator_main += 1

            while i < len(left_part):
                self.list_elements[Iterator_main] = left_part[i]
                i += 1
                Iterator_main += 1

            while j < len(right_part):
                self.list_elements[Iterator_main] = right_part[j]
                j += 1
                Iterator_main += 1
            return self.list_elements

    def selection_sort(self):
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
