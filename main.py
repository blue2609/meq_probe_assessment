from modules.tcp_server import TcpServer
import logging

def main():
	logging.basicConfig(level=logging.DEBUG)
	tcp_server = TcpServer()
	tcp_server.get_server_structure()
	tcp_server.draw_visualisation('server_state_machine_viz')

if __name__ == "__main__":
	main()