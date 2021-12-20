class Merge_sort:
    def Ascending_ordering(self, list_elements):
        if not len(list_elements) == 0:
            middle = len(list_elements) // 2
            left_part = list_elements[:middle]
            right_part = list_elements[middle:]

            left_part.sort()
            right_part.sort()

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
