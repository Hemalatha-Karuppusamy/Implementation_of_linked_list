class node_creation:
  def __init__(self,data):
    self.data = data
    self.next = None

class linked_list:
  def __init__(self):
    self.head = None

  def display(self):
    temp = self.head
    while temp != None:
      print(temp.data)
      temp = temp.next

  def insert(self,data, position = 'end', node = None):
    if position == 'start':
      temp = self.head
      self.head = node_creation(data)
      self.head.next = temp
    if position =='end':
      if self.head is None:
          self.head = node_creation(data)
      else:
        temp = self.head
        while temp.next is not None:
          temp = temp.next
        temp.next = node_creation(data)
    if position =='mid':
        temp = node.next
        node.next = node_creation(data)
        node.next.next = temp
          
  def delete(self,data):
    if (self.head.data == data):
      self.head = self.head.next
    else:
      temp = self.head
      if temp:
        while temp.data != data:
            prevnode = temp
            temp = temp.next
        prevnode.next = temp.next
      else:
          print("no such element present in the list")

  def search(self,data):
      temp = self.head
      while(temp):
        if temp.data == data:
          print("Element  is present")
          break
        else:
          temp = temp.next
      else:
        print("Element is not present")

  def reverse(self):
    prev = None
    current = self.head
    while(current is not None):
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev
