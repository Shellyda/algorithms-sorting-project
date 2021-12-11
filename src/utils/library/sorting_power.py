class Sorting_power:
    def __init__(self):
        self.head = None

    def Bubble_sort(list_elements):
        if not len(list_elements) == 0:
            count = 0
            swap_place = True
            while swap_place and count < len(list_elements) - 1:
                count += 1
                swap_place = False
                for index in range(0, len(list_elements) - count):
                    if list_elements[index] > list_elements[index + 1]:
                        list_elements[index], list_elements[index + 1] = (
                            list_elements[index + 1],
                            list_elements[index],
                        )
                        swap_place = True
            return list_elements

    def Insertion_sort(list_elements):
        if not len(list_elements) == 0:
            for i in range(1, len(list_elements)):
                aux = list_elements[i]
                j = i - 1
                while aux < list_elements[j] and j >= 0:
                    list_elements[j + 1] = list_elements[j]
                    j -= 1
                list_elements[j + 1] = aux
            return list_elements

    def Merge_sort(list_elements):
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
