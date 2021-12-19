class Merge_sort:
    def __init__(self, list_elements):
        self.list_elements = list_elements

    def Ascending_ordering(self):
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
