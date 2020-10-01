import sys
import shelve


def store_person(db):
    pid = input('eNTER UNIQUE id number')
    person = {}
    person['name'] = input('enter name:')
    person['age'] = input('enter age:')
    person['phone'] = input('enter phone number:')
    db[pid] = person


def lookup_person(db):
    pid = input('Enter ID number')
    field = input('what you want to know?(name,age,phone):')
    field = field.strip().lower()
    print(field.capitalize()+':', db[pid][field])
# def print


def enter_command():
    cmd = input('enter command')
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open('a.data')
    try:
        while True:
          cmd = enter_command()
          if cmd == 'store':
						store_person(database)
          elif cmd == 'lookup':
						lookup_person(database)
          elif cmd == '?':
						pass
					elif cmd == 'quit':
						return
		finally:
			database.close()	
