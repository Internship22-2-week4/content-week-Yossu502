import sys
from turtle import position

clients = [
  {
    'name': 'Pablo',
    'company': 'Google',
    'email': 'pablo@gmail.com',
    'position': 'Software engineer'
  },
  {
    'name': 'Ricardo',
    'company': 'Facebook',
    'email': 'pablo@facebook.com',
    'position': 'Data engineer'
  },
]

def createClient(client):
  global clients
  if client not in clients:
    clients.append(client)
  else:
    print('Client already is in the clients list')


def listClients():
  for idx, client in enumerate(clients):
    print(f"{idx} | {client['name']} | {client['company']}  | {client['email']} | {client['position']}")


def updateClient(clientName, newClient):
  for idx, client in enumerate(clients):
    if client['name'] == clientName:
      clients[idx] = newClient

def searchClient(clientName):
  for client in clients:
    if client['name'] != clientName:
      continue
    else:
      return True

def deleteClient(clientName):
  for idx, client in enumerate(clients):
    if client['name'] == clientName:
      clients.pop(idx)


def _printWelcome():
  print('WELCOME TO PLATZI VENTAS')
  print('*' * 15)
  print('What would you like to do today?')
  print('[C]reate client')
  print('[L]ist clients')
  print('[U]pdate client')
  print('[S]earch client')
  print('[D]elete client')

def _getClientField(field_name):
  field = None
  while not field:
    field = input(f'What is the client {field_name}: ')
  return field


def _getClientName():
  clientName = None
  while not clientName:
    clientName = input('What is the client name? ')
    if clientName == 'exit':
      clientName = None
      break
  
  if not clientName:
    sys.exit()
  return clientName 


if __name__ == '__main__':
  _printWelcome()
  command = input()
  command = command.upper()

  if command == 'C':
    client = {
      'name': _getClientField('name'),
      'company': _getClientField('company'),
      'email': _getClientField('email'),
      'position': _getClientField('position')
    }
    createClient(client)
    listClients()

  elif command == 'L':
    listClients()

  elif command == 'D':
    clientName = _getClientName()
    deleteClient(clientName)
    listClients()

  elif command == 'U':
    clientName = _getClientName()
    clientNew = {
      'name': _getClientField('name'),
      'company': _getClientField('company'),
      'email': _getClientField('email'),
      'position': _getClientField('position')
    }
    updateClient(clientName, clientNew)
    listClients()

  elif command == 'S':
    clientName = _getClientName()
    found = searchClient(clientName)
    if found:
      print('The client is in the client list')
    else:
      print(f'The client: {clientName} is not in the client list')
  else:
    print('Invalid command')