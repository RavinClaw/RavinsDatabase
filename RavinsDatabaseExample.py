from RavinsDatabase import Database as db
from RavinsDatabase import Add, Remove, List

def Adding():
  Add('Test 1')
  Add('Test 2')
  Add('Test 3')
  Add('Test 4')
  Add('Test 5')
  Add('Test 9')
  db()

def Removing():
  Remove('Test 9')
  db()

def Listing():
  print(List('Test 1'))
  print(List('Test 2'))
  print(List('Test 3'))
  print(List('Test 4'))
  print(List('Test 5'))
  db()