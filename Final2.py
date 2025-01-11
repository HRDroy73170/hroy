def main():
    records = []
    
    while True:

        print("\nMenu:")
        print("1. Add")
        print("2. View All")
        print("3. Search")
        print("4. Edit")
        print("5. Delete")
        print("6. Exit")
        
        
        choice = input("Enter your choice (1-6): ")
        
      
        if choice == "1":
            add_record(records)
        elif choice == "2":
            view_records(records)
        elif choice == "3":
            search_record(records)
        elif choice == "4":
            edit_record(records)
        elif choice == "5":
            delete_record(records)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_record(records):
    """Add a new record to the list."""
    record_id = input("Enter an ID for the record: ")
    record_name = input("Enter a name for the record: ")
    records.append({"ID": record_id, "Name": record_name})
    print("Record added successfully.")

def view_records(records):
    """View all records in the list."""
    if not records:
        print("No records available.")
    else:
        print("\nAll Records:")
        for record in records:
            print(f"ID: {record['ID']}, Name: {record['Name']}")

def search_record(records):
    """Search for a record by ID or name."""
    query = input("Enter the ID or Name to search: ")
    found = [record for record in records if query.lower() in record["ID"].lower() or query.lower() in record["Name"].lower()]
    if found:
        print("\nSearch Results:")
        for record in found:
            print(f"ID: {record['ID']}, Name: {record['Name']}")
    else:
        print("No matching records found.")

def edit_record(records):
    """Edit an existing record."""
    record_id = input("Enter the ID of the record to edit: ")
    for record in records:
        if record["ID"] == record_id:
            new_name = input("Enter the new name: ")
            record["Name"] = new_name
            print("Record updated successfully.")
            return
    print("Record not found.")

def delete_record(records):
    """Delete a record by ID."""
    record_id = input("Enter the ID of the record to delete: ")
    for record in records:
        if record["ID"] == record_id:
            records.remove(record)
            print("Record deleted successfully.")
            return
    print("Record not found.")

if __name__ == "__main__":
    main()