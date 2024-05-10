class Bottle:
    def __init__(self, capacity=12):
        if capacity < 0 and isinstance(capacity, int):
            raise ValueError
        self.capacity = capacity

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity):
        if new_capacity > 0 and isinstance(new_capacity, int):
            self._capacity = new_capacity


coke = Bottle(13)
print(coke.capacity)
