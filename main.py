import psycopg2

from dbConnection import get_cursor, close_connection, get_conn
#TODO update rest of functions and reset Primary keys to 1, get edit and delete functions to print each row with corresponding ID for edit or deletion

def add_character(first_name, last_name, classes):
    cursor = get_cursor()
    try:
        cursor.execute("INSERT INTO characters (first_name, last_name, classes) VALUES(%s, %s, %s);", (first_name, last_name, classes))
        get_conn().commit()
        print("Added character")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        print("character added")
        cursor.close()
def edit_character(first_name, last_name, classes, characters_id):
    cursor = get_cursor()
    try:
        cursor.execute("UPDATE characters SET first_name = %s, last_name = %s, classes = %s WHERE characters_id = %s;", (first_name, last_name, classes, characters_id))
        get_conn().commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        print("character edited")
        cursor.close()
def delete_character(characters_id):
    cursor = get_cursor()
    try:
        cursor.execute("DELETE FROM characters WHERE characters_id = %s;", (characters_id,))
        get_conn().commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        print("character deleted")
        cursor.close()
def add_combat(dice_roll, actual_roll, encounter_description, character_level, characters_id):
    cursor = get_cursor()
    try:
        cursor.execute("INSERT INTO combat_rolls (dice_roll, actual_roll, encounter_description, character_level, characters_id) VALUES(%s, %s, %s, %s, %s);", (dice_roll,actual_roll,encounter_description,character_level,characters_id))
        get_conn().commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        print("combat roll added")
        cursor.close()
def edit_combat(dice_roll, actual_roll, encounter_description, character_level, combatroll_id):
    cursor = get_cursor()
    try:
        cursor.execute("UPDATE combat_rolls SET dice_roll = %s, actual_roll = %s, encounter_description = %s, character_level = %s WHERE combatroll_id = %s;", (dice_roll, actual_roll, encounter_description, character_level, combatroll_id) )
        get_conn().commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        print("combat roll edited")
        cursor.close()
def delete_combat(combatroll_id):
    cursor = get_cursor()
    try:
        cursor.execute("DELETE FROM combat_rolls WHERE combatroll_id = %s;", combatroll_id)
        get_conn().commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        print("combat roll deleted")
        cursor.close()

#Prints all values in table by primary key number. Makes editing and deleting much easier
def print_table(table_name, primary_key):
    cursor = get_cursor()
    try:
        cursor.execute("SELECT * FROM " + table_name + " ORDER BY " + primary_key)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        cursor.close()
if __name__ == '__main__':
    while(True):
        print("Main Menu")
        print("1. Add a character")
        print("2. Edit a character")
        print("3. Delete a character")
        print("4. Add a combat encounter")
        print("5. Edit a combat encounter")
        print("6. Delete a combat encounter")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if(choice == "1"):
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")
            className = input("Enter class name: ")
            add_character(firstName, lastName, className)
        if(choice == "2"):
            print_table('characters', 'characters_id')
            firstName = input("Enter new first name: ")
            lastName = input("Enter new last name: ")
            className = input("Enter new class name: ")
            characters_id = input("Enter characters id: ")
            edit_character(firstName, lastName, className, characters_id)
        if(choice == "3"):
            print_table('characters', 'characters_id')
            characters_id = input("Enter characters id: ")
            delete_character(characters_id)
        if(choice == "4"):
            diceRoll = input("Enter dice roll: ")
            actualRoll = input("Enter actual roll: ")
            encounterDescription = input("Enter encounter description: ")
            characterLevel = input("Enter character level: ")
            charactersID = input("Enter characters id: ")
            add_combat(diceRoll, actualRoll, encounterDescription, characterLevel)
        if(choice == "5"):
            print_table('combat_rolls', 'combatroll_id')
            diceRoll = input("Enter new dice roll: ")
            actualRoll = input("Enter new actual roll: ")
            encounterDescription = input("Enter new encounter description: ")
            characterLevel = input("Enter new character level: ")
            charactersID = input("Enter new characters id: ")
            edit_combat(diceRoll, actualRoll, encounterDescription, characterLevel, charactersID)
        if(choice == "6"):
            print_table('combat_rolls', 'combatroll_id')
            combatRoll_id = input("Enter combat roll id: ")
            delete_combat(combatRoll_id)
        if(choice == "7"):
            close_connection()
            break;
