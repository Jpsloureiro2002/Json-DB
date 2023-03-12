from pathlib import Path
import json
import os
import JsonDBcmdlib as p

clear = lambda: os.system('cls')



def create_db():
	try:
		Path("DB/").mkdir(parents=True, exist_ok=True)
		db_name = input("Insert DB name:\n> ")
		file = open(r"DB/"+f"{db_name}.json", "w")
		file.write("{")
		file.close()
		file = open(r"DB/"+f"{db_name}.json", "a")

		content = ""
		while True:
			clear()
			table = input("Type the name of the Table (Q to stop):\n> ")
			if table == "Q":
				break
			content = f'{content}"{table}":' + r"{"
			campos = []
			clear()
			while True:
				types = input(f"Type the fields from the table{table} (Q to stop):\n> ")
				if types == "Q":
					content_l1 = list(content)
					content_l1.pop()
					content = "".join(content_l1)
					#print(content)
					break
				content = f'{content}"{types}":[],'
				#print(content)
			content += r'},'
			#print(content)
		content_l = list(content)
		content_l.pop()
		#print(content_l)
		content = "".join(content_l)
		#print(content)
		file.write(content.replace("'",'"'))
		file.write("}")
	except:
		return False

def use_db(db_name):
	Path("DB/").mkdir(parents=True, exist_ok=True)
	db_path = r"DB/"+ db_name +".json"
	my_file = Path(db_path)
	if not my_file.is_file():
		return False,"File Not Found"
	json_file = open(db_path)
	
	db_json = json.loads(json_file.read())
	db = dict(db_json)
	error = ""
	while True:
		clear()
		print(error)
		error = ""
		print("Choose one of the options:\n\n(1)Show All Tables\n(2)View Values From Tables\n(3)Insert Tabbles\n(4)Commands\n(0)Quit")
		choice = input("\n> ")
		if choice == "0":
			break
		if choice == "1":
			clear()
			p.print_tables(db)
		if choice == "3":
			clear()
			Select_table = input("\nType the name of the table:\n\n> ")
			table = db.get(Select_table)
			clear()
			while True:
				try:
					for keys, value in table.items():
						data = input(f"Type the value in the field {keys}\n\n> ")
						db_json[Select_table][keys].append(data)
						with open(db_path, 'w') as f:
							json.dump(db_json, f)
					x = input("Want to add more(Y,N)?\n\n> ")
					if x == "n" or x == "N":
						break
				except:
					error = "Table Unknown!"
					break
		if choice == "2":
			clear()
			Select_table = input("\nType the name of the table:\n\n> ")
			table = db.get(Select_table)
			out = p.print_table_content(table, Select_table,db)
			if not out[0]:
				error = out[1]
			pass
		if choice == "4":
			while True:
				clear()
				command = input("Type the command (h for help or h-command):\n\n> ")
				if command[0] =="h" or command[0]=="H":
					clear()
					print("Command List:\n\n> SELECT\n> INSERT\n")
				else:
					break
	return True, "Finished"

