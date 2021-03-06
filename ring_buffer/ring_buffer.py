# class RingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass

class RingBuffer:
    """ class that implements a not-yet-full buffer """
    def __init__(self,capacity): # size max > capacity
        self.capacity = capacity
        self.data = []

    # class __Full(RingBuffer):
    #     """ class that implements a full buffer """
    #     def append(self, x):
    #         """ Append an element overwriting the oldest one. """
    #         self.data[self.cur] = x
    #         self.cur = (self.cur+1) % self.max
    #     def get(self):
    #         """ return list of elements in correct order """
    #         return self.data[self.cur:]+self.data[:self.cur]

# if capacity ==  len(list)
# list.replace(0, x)

    def append(self,item): # x > item
        """append an element at the end of the buffer"""
        if len(self.data) == self.capacity:
            self.data[0] = item
            # for n in self.data:
            #     if self.data[n] != item:
            #         self.data[n] = item
        else:
            self.data.append(item)
        # if len(self.data) == self.capacity:
        #     self.cur = 0
        #     self.data[self.cur] = item #
        #     self.cur = (self.cur+1) % self.capacity #            
            # Permanently change self's class from non-full to full
            # self.__class__ = self.__Full
        #

    def get(self):
        """ Return a list of elements from the oldest to the newest. """
        return self.data