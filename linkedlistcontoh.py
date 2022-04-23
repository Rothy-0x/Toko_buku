class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getData(self):
        return self.value

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.value = newData

    def setNext(self, newNext):
        self.next = newNext


class OrderedList:

    def __init__(self):
        self.head = None

    def show(self):
        current = self.head
        print('Head->', end="")
        while current != None:
            print(current.getData(), end="->")
            current = current.getNext()
        print('None')

    def search(self, item):
        current = self.head
        count = 0

        while current is not None:
            if current.value == item:
                count += 1
                print('data ditemukan')
                print('jumlah iterasi : ', count)

                return True
            if current.value < item:
                count += 1
                print('data tidak ditemukan')
                print('jumlah iterasi : ', count)
                return False

            current = current.next

        return False

    def add(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.value > item:
                break
            previous, current = current, current.next

        temp = Node(item)
        if previous is None:
            temp.next, self.head = self.head, temp
        else:
            temp.next, previous.next = current, temp

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
                print(item, "Ditemukan")
            else:
                previous = current
                current = current.getNext()
        if found == False:
            print(item, "tidak Ditemukan")
        elif previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(2)
mylist.show()
mylist.remove(32)
mylist.show()
mylist.remove(31)
mylist.show()
