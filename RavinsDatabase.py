import os
import time

infos = []

def Database():
  global infos
  os.system('clear')
  num_infos = len(infos)
  print("Ravin's Database\n")
  print(f'Number of Entries\t[{num_infos}]')
  print(f'All Entries: {infos}')
  print('\nDatabase Display Front')

def database():
  global infos
  os.system('clear')
  num_infos = len(infos)
  print("Ravin's Database\n")
  print(f'Number of Entries\t[{num_infos}]')
  print(f'All Entries: {infos}')
  print('\nCommands: add / remove / list')
  select = input('#: ')
  if select == 'add':
    add()
  if select == 'remove':
    remove()
  if select == 'list':
    list()
  if select == 'leave':
    exit()
  else:
    reload()

def reload():
  os.system('clear')
  database()

def list():
  global infos
  os.system('clear')
  print("Ravin's Database")
  print(f'Existing Entries: {infos}\n')
  print('List Entry\n')
  info = input('#: ')
  if info == info:
    print(f'Entry Number: {infos.index(info)}')
    time.sleep(5)
    database()
  else:
    database()

def add():
  global infos
  os.system('clear')
  print("Ravin's Database")
  print(f'Existing Entries: {infos}\n')
  print('Add Entry\n')
  info = input('#: ')
  if info == info:
    infos.append(info)
    database()
  else:
    database()

def remove():
  global infos
  os.system('clear')
  print("Ravin's Database")
  print(f'Existing Entries: {infos}\n')
  print('Remove Entry\n')
  info = input('#: ')
  if info == info:
    infos.remove(info)
    database()
  else:
    database()

def Add(add):
  global infos
  infos.append(add)

def Remove(remove):
  global infos
  infos.remove(remove)

def List(list):
  global infos
  infos.index(list)

def Save():
  with open(a[0], 'w') as user_file_name:
    user_file_name.writelines(open(the_existing_file_to_save))