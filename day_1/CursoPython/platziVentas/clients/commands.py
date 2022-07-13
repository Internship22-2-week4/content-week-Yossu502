import click
from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
  """Manages the clients lifecycle"""
  pass


@clients.command()
@click.option('-n', '--name', type=str, prompt=True, help='The Client Name')
@click.option('-c', '--company', type=str, prompt=True, help='The Client Company')
@click.option('-e', '--email', type=str, prompt=True, help='The Client email')
@click.option('-p', '--position', type=str, prompt=True, help='The Client position')
@click.pass_context
def create(ctx, name, company, email, position):
  """Creates a new client"""
  client = Client(name, company, email, position)
  client_service = ClientService(ctx.obj['clients_table'])
  client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
  """List alll clients"""
  client_service =  ClientService(ctx.obj['clients_table'])
  client_list = client_service.list_clients()
  click.echo('   ID    |   NAME    |   COMPANY   |   EMAIL   |   POSITION    ')
  click.echo('-'*15)
  for client in client_list:
    click.echo(f"{client['uid']}   {client['name']}   {client['company']}     {client['email']}   {client['position']}")

@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def update(ctx, client_uid):
  """Update a client"""
  clients_service = ClientService(ctx.obj['clients_table'])
  client_list = clients_service.list_clients()
  client = [client for client in client_list if client['uid'] == client_uid]
  if client:
    client = _update_client_flow(Client(**client[0]))
    clients_service.update(client)
    click.echo('Client updated')
  else:
    click.echo('Client not founded')

def _update_client_flow(client):
  click.echo('Leave empty if you dont wat to modify the value')
  client.name = click.prompt('New name', type=str, default=client.name)
  client.company = click.prompt('New Company', type=str, default=client.company)
  client.email = click.prompt('New email', type=str, default=client.email)
  client.position = click.prompt('New position', type=str, default=client.position)
  return client

@clients.command()
@click.pass_context
def delete(ctx, id):
  """Delete a client"""


all = clients
