class Search:
    POSITION = 0

    # linear search with algorithm O(n)
    def linear(self, list, number):
        for i in range(len(list)):
            if list[i] == number:
                self.POSITION = i
                return True

        return False

    # linear search with algorithm O(n)
    def binary(self, list, number):
        lowest = 0
        upper = len(list) - 1

        while lowest <= upper:
            mid = (lowest + upper) // 2  # find mid

            if list[mid] == number:  # check if mid is equal number
                self.POSITION = mid
                return True
            else:
                if list[mid] < number:
                    lowest = mid + 1
                else:
                    upper = mid - 1

        return False


list = [1, 2, 3, 4, 5, 8, 10, 12, 13, 17, 19, 23, 25, 26, 28, 30]

print(list)
number = int(input('Enter number:'))

object = Search()

if object.linear(list, number):
    print('Found on', object.POSITION)
else:
    print('Not found!')

if object.binary(list, number):
    print('Found on', object.POSITION)
else:
    print('Not found!')
