import json

filename = "lotto_db.json"

def write_json(data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def main_menu_print():
    print("1 - Edit database")
    print("2 - Check results")

def db_menu_print():
    print("1 - Add ticket")
    print("2 - Delete last ticket")
    print("3 - Edit ticket")
    print("4 - Delete all tickets")
    print("5 - View tickets")
    print("6 - Return")

def add_ticket():
    with open (filename) as json_file:
        data = json.load(json_file)
        lst = []
        print("Enter ticket numbers")
        for i in range(0, 6):
            ele = int(input())
            lst.append(ele)
        ticket_count = len(data)

    
        y = {f"{ticket_count+1}": lst}
        data.append(y)

        write_json(data)

def delete_last_ticket():
    with open (filename) as json_file:
        data = json.load(json_file)
        if len(data) == 0:
            print("You dont have any tickets registered")
            return
        else:
            data.pop()
            write_json(data)

def delete_all_tickets():
    data = []
    write_json(data)

def edit_ticket():
    new_data = []
    lst = []
    with open(filename, "r") as f:
        data = json.load(f)
    print(f"Which ticket would you like to edit? (1 - {len(data)}) ")
    edit_option = input()
    i = 1
    for entry in data:
        if i == int(edit_option):
            print("Input new numbers ")
            for x in range(0, 6):
                ele = int(input())
                lst.append(ele)
            y = {f"{i}": lst}
            new_data.append(y)
            i += 1
        else:
            new_data.append(entry)
            i += 1
    write_json(new_data)

def view_tickets():
    with open(filename, "r") as f:
        data = json.load(f)
    for entry in data:
        print(entry)


def db_menu():
    while True:
        db_menu_print()
        choice = input()
        if choice == '1':
            add_ticket()
        elif choice == '2':
            delete_last_ticket()
        elif choice == '3':
            edit_ticket()
        elif choice == '4':
            delete_all_tickets()
        elif choice == '5':
            view_tickets()
        elif choice == '6':
            return
        else:
            print("Wrong input")
            continue




def win_check():
    win_numbers = []
    print("Input win numbers ")
    for i in range(0, 6):
        ele = int(input())
        win_numbers.append(ele)
    
    
    with open(filename, "r") as f:
        data = json.load(f)
    i = 0
    for entry in data:
        right_numbers = 0
        for x in range(0,6):
            for y in range(0,6):
                if win_numbers[x] == data[i][f"{i+1}"][y]:
                    right_numbers += 1
        print(f"You have {right_numbers} right numbers in {entry}")
        i += 1


if __name__ == '__main__':
    while True:
        main_menu_print()
        choice = input()
        if choice == '1':
            db_menu()
        elif choice == '2':
            win_check()
        else:
            print("Wrong input")
            continue