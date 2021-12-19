from timeit import default_timer

class Get_duration_execution_time:
    def Ordering(name_of_algorithm, function, random_list):
        begin = default_timer()
        function(random_list)
        end = default_timer()

        result = end - begin
        print(
            "   - {} runtime: {} seconds".format(
                name_of_algorithm, result
            )
        )
        return result