class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value
    

class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
  
  # adding a node to the head
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    # If the list has a head (the list is not empty), set the links
    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)
    
    # Set the list's head to the new_head
    self.head_node = new_head

    # If the list doesn't have a tail (the list is empty), set the list's tail to the new head
    if self.tail_node == None:
      self.tail_node = new_head
  
  # Adding a node to the tail
  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    # If the list has a tail (the list is not empty), set the links
    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)

    # Set the list's tail to the new_tail
    self.tail_node = new_tail

    # If the list doesn't have a head (the list is empty), set the list's head to the new tail
    if self.head_node == None:
      self.head_node = new_tail
  
  # Removing a head node and returing a removed node's value
  def remove_head(self):
    removed_head = self.head_node
    
    # If the list is empty, return None
    if removed_head == None:
      return None
    
    # Set the list's head node to the next node and remove the very head node
    self.head_node = removed_head.get_next_node()
    
    # If the head now still has a value, remove the former tail node
    if self.head_node != None:
      self.head_node.set_prev_node(None)
    
    # If the removed head was also the tail of the list (meaning there was only one element in the list), call remove tail function:
    if removed_head == self.tail_node:
      self.remove_tail()
    
    # Return the removed head's value
    return removed_head.get_value()
    
  # Removing a tail node and returning a removed node's value
  def remove_tail(self):
    removed_tail = self.tail_node
    
    # If the list is empty, return None
    if removed_tail == None:
      return None
    
    # Set the list's tail node to the next node
    self.tail_node = removed_tail.get_prev_node()
    
    # If the tail now still has a value, remove the former tail node
    if self.tail_node != None:
      self.tail_node.set_next_node(None)
    
    # If the removed tail was also the head of the list (meaning there was only one element in the list), call remove head function:
    if removed_tail == self.head_node:
      self.remove_head()
    
    # Return the removed tail's value
    return removed_tail.get_value()
  
  # Removing a node with the specified value
  def remove_by_value(self, value_to_remove):
    node_to_remove = None
    current_node = self.head_node

    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        if node_to_remove == self.head_node:
          self.remove_head()
        elif node_to_remove == self.tail_node:
          self.remove_tail()
        else:
          next_node = node_to_remove.get_next_node()
          prev_node = node_to_remove.get_prev_node()
          next_node.set_prev_node(prev_node)
          prev_node.set_next_node(next_node)
        return node_to_remove

      current_node = current_node.get_next_node()

    if node_to_remove == None:
      return None


# Create your subway line here:
subway = DoublyLinkedList()
subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")

subway.add_to_tail("Penn Station")
subway.add_to_tail("Wall Street")
subway.add_to_tail("Brooklyn Bridge")

subway.remove_head()
subway.remove_tail()

subway.remove_by_value("Times Square")
print(subway.stringify_list())
