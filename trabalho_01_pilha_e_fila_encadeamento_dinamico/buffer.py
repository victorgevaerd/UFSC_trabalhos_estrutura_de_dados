from buffer_element import BufferElement


class Buffer:

    """This class represents a buffer structure.
    """

    def __init__(self, max_size: int=100):
        self.__first_element = None
        self.__last_element = None
        if not isinstance(max_size, int) or max_size <= 0:
            print('Setting the maximum size of the buffer to default value because "{}" is not valid.'.format(max_size))
            max_size = 100
        print('Buffer maximum size was set to {}'.format(max_size))
        self.__max_size = max_size
        self.__num_elements = 0

    def enqueue(self, element):
        """This method will enqueue the element to the tail of the
        buffer if it is not full.
        """
        if self.__is_empty():
            temp = BufferElement(element)
            self.__first_element = temp
            self.__last_element = temp
            self.__num_elements += 1
        elif not self.__is_full():
            temp = BufferElement(element)
            self.__last_element.next_element = temp
            self.__last_element = temp
            self.__num_elements += 1
        else:
            raise Exception('The buffer is full')

    def dequeue(self):
        """This method will dequeue the element from the head of the
        buffer if it is not empty.
        """
        if self.__is_empty():
            raise Exception('The buffer is empty')
        elif self.__num_elements == 1:
            self.__first_element = None
            self.__last_element = None
            self.__num_elements -= 1
        else:
            self.__first_element = self.__first_element.next_element
            self.__num_elements -= 1

    def head(self):
        """Returns the first element of the buffer.
        """
        if not self.__is_empty():
            return self.__first_element.value
        else:
            raise Exception('The buffer is empty.')

    def tail(self):
        """Returns the last element of the buffer.
        """
        if not self.__is_empty():
            return self.__last_element.value
        else:
            raise Exception('The buffer is empty.')

    def __is_full(self):
        return self.__num_elements == self.__max_size

    def __is_empty(self):
        return self.__num_elements == 0
