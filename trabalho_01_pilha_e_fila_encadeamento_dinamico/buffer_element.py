class BufferElement:

    def __init__(self, value):
        self.__value = value
        self.__next_element = None

    @property
    def value(self):
        return self.__value

    @property
    def next_element(self):
        return self.__next_element

    @next_element.setter
    def next_element(self, next_element):
        self.__next_element = next_element
