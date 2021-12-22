class Merge_sort:
    def Ascending_ordering(self, list_elements):
        if len(list_elements) > 1:
            middle = len(list_elements) // 2
            left_part = list_elements[:middle]
            right_part = list_elements[middle:]

            self.Ascending_ordering(left_part)
            self.Ascending_ordering(right_part)

            Iterator_main = i = j = 0

            while i < len(left_part) and j < len(right_part):
                if left_part[i] < right_part[j]:
                    list_elements[Iterator_main] = left_part[i]
                    i += 1
                else:
                    list_elements[Iterator_main] = right_part[j]
                    j += 1
                Iterator_main += 1

            while i < len(left_part):
                list_elements[Iterator_main] = left_part[i]
                i += 1
                Iterator_main += 1

            while j < len(right_part):
                list_elements[Iterator_main] = right_part[j]
                j += 1
                Iterator_main += 1
            return list_elements
