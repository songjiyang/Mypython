class Node():

	def __init__(self, data):
		self.data = data
		self.next = None

	def get_data(self):
		return self.data

	def set_data(self, new_data):
		self.data = new_data

	def get_next(self):
		return self.next

	def set_next(self, new_next):
		self.next = new_next

class LinkedList():

	def __init__(self):
		self.head = None
		self.tail = None

	def get_head(self):
		return self.head

	def is_empty(self):
		return self.head is None and self.tail is None

	def add(self,node):
		new_node = Node(node)
		if self.is_empty():
			self.head = self.tail = new_node
		else:
			new_node.set_next(self.head)
			self.head = new_node 

	def size(self):
		current = self.head()
		num = 0
		while current:
			num += 1
			current = current.get_next()

	def search(self,item):
		current = self.head 
		found = False
		while current and not found:
			if current.get_data()==item:
				found = True
			else:
				current = current.get_next()
		return found

	def append(self, item):
		new_node = Node(item)
		if self.is_empty():
			self.head = self.tail = new_node
		else:
			self.tail.set_next(new_node) 
			self.tail = new_node

	def remove(self, item):
		current = self.head
		previous = None
		while current:

			if current.get_data() == item:
				if previous == None:			#head node
					self.head = current.get_next()
				else:
					previous.next = current.get_next()
				break
			else:
				previous = current
				current = current.get_next()

	def printl(self):
		result = []
		current = self.head
		while current:
			result.append(current.get_data())
			current = current.get_next()
		print('print linkedlist:')
		print(result)

if __name__ == '__main__':

	link_list_1 = LinkedList()
	print("is_empty",link_list_1.is_empty())
	link_list_1.append('a')
	print("is_empty",link_list_1.is_empty())
	link_list_1.append('b')
	link_list_1.append('c')
	link_list_1.append('d')
	link_list_1.add('z')
	print("search_exist",link_list_1.search('a'))
	print("search_no_exist",link_list_1.search('y'))
	link_list_1.printl()

	link_list_1.remove('1')
	link_list_1.printl()
	link_list_1.remove('b')
	link_list_1.printl()
