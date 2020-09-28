class MinIntHeap:
    capacity = 10
    size = 0
    items = [0] * capacity

    def getLeftChildIndex(self, pI):
        return pI * 2 + 1

    def getRightChildIndex(self, pI):
        return pI * 2 + 2

    def getParentIndex(self, cI):
        return (cI - 1) // 2

    def hasLeftChild(self, i):
        return self.getLeftChildIndex(i) < self.size

    def hasRightChild(self, i):
        return self.getRightChildIndex(i) < self.size

    def hasParent(self, i):
        return self.getParentIndex(i) >= 0

    def leftChild(self, i):
        return self.items[self.getLeftChildIndex(i)]

    def rightChild(self, i):
        return self.items[self.getRightChildIndex(i)]

    def parent(self, i):
        return self.items[self.getParentIndex(i)]

    def ensureCapacity(self):
        if self.size == self.capacity:
            self.items += [0] * self.capacity
            self.capacity += self.capacity

    def peek(self):
        return self.items[0] if self.size > 0 else None

    def heapifyDown(self):
        i = 0
        while self.hasLeftChild(i):
            smallerChildI = self.getLeftChildIndex(i)
            if self.hasRightChild(i) and self.rightChild(i) < self.getLeftChildIndex(i):
                smallerChildI = self.getRightChildIndex(i)

            if self.items[i] < self.items[smallerChildI]:
                break
            else:
                self.items[i], self.items[smallerChildI] = self.items[smallerChildI], self.items[i]

            i = smallerChildI

    def pop(self):
        if self.size == 0:
            return None

        aux = self.items[0]

        self.size -= 1
        self.items[0] = self.items[size]
        self.heapifyDown()
        return aux

    def heapifyUp(self):
        i = self.size - 1
        while self.hasParent(i) and self.parent(i) > self.items[i]:
            aux, self.items[i] = self.items[i], aux
            i = self.getParentIndex(i)

    def add(self, item):
        self.ensureCapacity()
        self.items[size] = item
        self.size += 1
        self.heapifyUp()
