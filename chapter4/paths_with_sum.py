class BTNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None


def create_bt():
	node_minus_one = BTNode(-1)
	node_zero = BTNode(0)
	node_one = BTNode(1)
	node_two = BTNode(2)
	node_three = BTNode(3)

	node_one.left = node_two
	node_two.right = node_minus_one
	node_one.right = node_zero
	node_zero.left = node_three

	return node_one


def paths_with_sum(node, sum):
	nodes_in_order = []

	in_order_traversal(node, nodes_in_order)

	num_paths = 0

	for node in nodes_in_order:
		num_paths += paths(node, sum)

	return num_paths


def paths(node, sum):
	if node is None:
		return 0
	if node.data == sum:
		return 1
	num_paths = 0
	if node.left is not None:
		num_paths += paths(node.left, sum - node.data)
	if node.right is not None:
		num_paths += paths(node.right, sum - node.data)
	return num_paths


def in_order_traversal(node, result_set):
	if node is None:
		return []

	in_order_traversal(node.left, result_set)
	result_set.append(node)
	in_order_traversal(node.right, result_set)

	return result_set


if __name__ == '__main__':
	print('Paths with Sum')
	root = create_bt()

	# In Order Traversal check
	nodes = []
	in_order_traversal(root, nodes)
	for node in nodes:
		print(node.data, end="->")
	print(end="\n")

	# Num Paths
	print(f"Num paths: {paths_with_sum(root, 2)}")
