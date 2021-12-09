class Sorting_power:
    def Bubble_sort(list_elements):
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
