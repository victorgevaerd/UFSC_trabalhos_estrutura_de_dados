class StackElement:

    def __init__(self, value, prev_element):
        self.__value = value
        self.__prev_element = prev_element

    @property
    def value(self):
        return self.__value

    @property
    def prev_element(self):
        return self.__prev_element    
