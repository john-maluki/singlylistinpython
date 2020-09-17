class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self, value):
    self.head = Node(value)
    self.tail = self.head
    self.length = 1

  def append(self, value):
    
    new_head = Node(value)
    self.tail.next = new_head
    self.tail = new_head
    self.length += 1
  
  def prepend(self, value):
    new_head = Node(value)
    sw = self.head
    self.head = new_head
    self.head.next = sw
    self.length += 1

  def print_list(self):
    values = []
    current_node = self.head
    while current_node != None:
      values.append(current_node.value)
      current_node = current_node.next

    return values

  def insert(self, index, value):
    if index == 0:
      self.prepend(value)
      return self.print_list()
    if index >= self.length:
      self.append(value)
      return self.print_list()
    leader_node = self._traverse_list(index)
    cn = leader_node.next
    new_node = Node(value)
    leader_node.next = new_node
    new_node.next = cn
    self.length += 1
    
    return self.print_list()

  def remove(self, index):
    leader_node = self._traverse_list(index)
    remove_node = leader_node.next
    leader_node.next = remove_node.next
    self.length -= 1
    
    
    return self.print_list()

  def _traverse_list(self, index):
    current_node = self.head
    i = 0
    while current_node != None:
      if index - 1 == i:
        break
      
      current_node = current_node.next
      i += 1

    return current_node

link = LinkedList(10)
link.append(5)
link.append(16)
link.prepend(2)
link.insert(1, 100)
link.insert(5, 101)
link.remove(1)

print(link.print_list())



