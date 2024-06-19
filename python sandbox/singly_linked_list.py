class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return "<Node: %s>" % self.data


class Linked_List:
    def __init__(self, args):
        self.__size = 0
        if args is None or not args:
            self.head = None
            return

        self.head = Node(args[0])
        current_node = self.head
        for item in args[1:]:
            current_node.next = Node(item)
            current_node = current_node.next
        self.__set_size(len(args))

    # getter
    def size(self):
        return self.__size

    # setter
    def __set_size(self, size):
        self.__size = size

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            size = self.__get_size()
            self.__set_size(size + 1)
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        size = self.size()
        self.__set_size(size + 1)

    def prepend(self, data):
        new_node = Node(data)
        tmp = self.head
        new_node.next = tmp
        self.head = new_node
        size = self.size()
        self.__set_size(size + 1)

    def pop(self):
        last = self.head
        if last.next is None:
            self.head = None
        while last.next.next is not None:
            last = last.next
        last.next = None
        size = self.size()
        self.__set_size(size - 1)

    def unshift(self):
        self.head = self.head.next
        size = self.size()
        self.__set_size(size - 1)

    def __repr__(self) -> str:
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(nodes) + " -> None"


# Test

if __name__ == "__main__":
    lm = Linked_List([1, 2, 3, 4, 5, 6, 7])
    # lm.append(1)
    # lm.append(2)
    # lm.append(3)
    # lm.append(4)
    # lm.append(5)
    # lm.append(6)
    # lm.append(7)
    lm.append(8)
    lm.prepend(0)
    lm.pop()
    lm.unshift()
    print(lm)  # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None
    print(lm.size())  # 7

# Gyaan

"""
What is the actual use for linkedlist, or it just has academic value?

Linked lists have both academic and practical value, and they are used in various real-world scenarios. Some common applications and use cases for linked lists include:

Dynamic Memory Allocation: Linked lists are often used in memory management systems, especially in languages like C and C++, where dynamic memory allocation is prevalent. They allow for efficient allocation and deallocation of memory blocks of varying sizes.

Implementation of Other Data Structures: Linked lists serve as fundamental building blocks for implementing more complex data structures such as stacks, queues, and hash tables. For example, stacks and queues can be efficiently implemented using linked lists due to their constant-time insertion and deletion operations at either end.

Undo Functionality in Text Editors: Many text editors implement undo functionality using a linked list of changes. Each edit is stored as a node in the linked list, allowing users to traverse backward through the list to undo previous actions.

Music and Video Playlists: Linked lists are used to implement playlists in music and video players. Each item (song or video) in the playlist is represented by a node in the linked list, allowing users to navigate through the playlist in a sequential manner.

Sparse Matrix Representation: Linked lists can be used to represent sparse matrices, which are matrices with a large number of zero elements. Instead of storing all elements in a two-dimensional array, linked lists store only the non-zero elements along with their row and column indices, resulting in reduced memory usage.

Symbol Table in Compilers: Linked lists are used to implement symbol tables in compilers and interpreters. Each symbol (variable or function) in the program is stored as a node in the linked list, allowing for efficient lookup and management of symbols during compilation or interpretation.

Operating System Kernel Data Structures: Linked lists are used extensively in operating system kernels to manage various system resources such as processes, threads, and file descriptors. They provide efficient ways to organize and traverse these resources.
"""
