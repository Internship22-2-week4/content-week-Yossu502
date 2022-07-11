import sys

clients = 'Pablo,Ricardo,'

def createClient(clientName):
  global clients
  if clientName not in clients:
    clients += clientName
    _addComma()
  else:
    print('Client already is in the clients list')


def listClients():
  global clients
  print(clients)


def updateClient(clientName, updateClientName):
  global clients
  if clientName in clients:
    clients = clients.replace(clientName + ',', updateClientName + ',')
  else:
    print('Client is not in clients list')


def searchClient(clientName):
  global clients
  clientList =  clients.split(',')
  for client in clientList:
    if client != clientName:
      continue
    else:
      return True


def deleteClient(clientName):
  global clients
  if clientName in clients:
    clients = clients.replace(clientName + ',', '')
  else:
    print('Client is not in clients list')


def _addComma():
  global clients
  clients += ','


def _printWelcome():
  print('WELCOME TO PLATZI VENTAS')
  print('*' * 15)
  print('What would you like to do today?')
  print('[C]reate cliente')
  print('[U]pdate cliente')
  print('[S]earch client')
  print('[D]elete client')

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
    clientName = _getClientName()
    createClient(clientName)
    listClients()
  elif command == 'D':
    clientName = _getClientName()
    deleteClient(clientName)
    listClients()
  elif command == 'U':
    clientName = _getClientName()
    updatedClientName = input('What is the new name? ')
    updateClient(clientName, updatedClientName)
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