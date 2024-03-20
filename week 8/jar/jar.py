class Jar:
#Initialize a cookie
    def __init__(self, capacity=12):
        self.capacity = capacity
#Initial size = 0
        self.size = 0

#n = nb of cookies in the cookie jar (emoji)
    def __str__(self):
        return f"{'🍪' * self.size}"

#Add n cookies to the cookie jar
    def deposit(self, n):
#Raise ValueError if negative deposit
        if n < 0:
            raise ValueError ("Negative deposit")
#Raise ValueError if deposit > capacity
        if n + self.size > self.capacity:
            raise ValueError ("Enough cookies!")
#Otherwise we can increase the size
        else:
            self._size += n

#Remove n cookies from the cookie jar
    def withdraw(self, n):
#Raise ValueError if negative withdrawal
        if n < 0:
            raise ValueError ("Negative withdrawal")
#Raise ValueError if withdraw > size
        if n > self.size:
            raise ValueError ("Not enough cookies")
#Otherwise we can decrease the size
        else:
            self._size -= n

#Return the cookie jar's capacity
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity (self, capacity):
#Raise ValueError if capacity != -int
        if capacity < 0:
            raise ValueError ("Invalid capacity")
        self._capacity = capacity


#return the nb of cookies actually in the cookie jar
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

#Test printing
def main():
    jar = Jar()
    print(jar)

if __name__ == "__main__":
    main()
