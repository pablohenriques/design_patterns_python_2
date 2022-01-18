"""
from connection_factory import get_connection
connection = get_connection()
"""

from connection_factory import ConnectionFactory


connection = ConnectionFactory().get_connection()

# acoes

connection.close()