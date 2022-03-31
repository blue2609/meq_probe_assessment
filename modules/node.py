class Node:
	def __init__(self, label: str, tcp_server):
		"""
		Initiate the state of the node and assign a label to it

		Parameters
		----------
		label : str
			The label of the node. This label will always be a single capital letter like 'A' for instance
		
		tcp_server : TcpServer
			The 'TcpServer' session that this node belongs to
		"""

		self.label = label
		self.tcp_server = tcp_server
		self.possible_actions = ['1', '2', '3']
	
	def get_next_possible_action(self):
		if len(self.possible_actions) > 0:
			return self.possible_actions[0]
		else:
			return None

	def move_to_next_node(self, action: str):
		destination_node_label = self.tcp_server.send_message(action)[0]
		self.possible_actions.remove(action)
		self.tcp_server.graph.add_edge(self.label, destination_node_label, label=action)
		return destination_node_label 
		

	
