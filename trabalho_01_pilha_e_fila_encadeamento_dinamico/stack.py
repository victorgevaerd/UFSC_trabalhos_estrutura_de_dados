from stack_element import StackElement


class Stack:

    """This class represents a stack structure
    """

    def __init__(self, max_size: int=1000):
        self.__top_element = None
        if not isinstance(max_size, int) or max_size <= 0:
            print('Setting the maximum size of the stack to default value because "{}" is not valid.'.format(max_size))
            max_size = 1000
        print('Stack maximum size was set to {}'.format(max_size))
        self.__max_size = max_size
        self.__num_elements = 0

    @property
    def num_elements(self):
        print('Getting size of the stack')
        return self.__num_elements

    def push(self, element):

        """This method will push the element to the top of the stack if
        it is not full.
        """

        if not self.__is_full():
            print('Setting the top value to: {}'.format(element))
            self.__top_element = StackElement(element, self.__top_element)
            self.__num_elements += 1
        else:
            raise Exception('Stack is already full')

    def pop(self):

        """This method will pop and return the element from the top of 
        the stack if it is not empty.
        """
        
        if not self.__is_empty():
            print('Deleting the top value of the stack...')
            temp = self.__top_element.value
            self.__top_element = self.__top_element.prev_element
            self.__num_elements -= 1
            return temp
        else:
            raise Exception('Stack is empty')

    def top(self):

        """Returns the top element from the stack.
        """

        if not self.__is_empty():
            print('Getting top element...')
            return self.__top_element.value
        else:
            raise Exception('Stack is empty')

    def __is_full(self):

        """This method will return a boolean value indicating whether
        is full or not.
        """

        return self.__num_elements == self.__max_size

    def __is_empty(self):

        """This method will return a boolean value indicating whether
        is empty or not.
        """

        return self.__num_elements == 0
