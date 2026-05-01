seats = 50
bookings = {}

def check_availability():
    print("Available seats:", seats)

def book_ticket():
    global seats
    if seats <= 0:
        print("No seats available!")
        return
    
    name = input("Enter name: ")
    age = input("Enter age: ")
    
    booking_id = len(bookings) + 1
    bookings[booking_id] = {"name": name, "age": age}
    
    seats -= 1
    print("Ticket booked successfully!")
    print("Booking ID:", booking_id)

def view_ticket():
    bid = int(input("Enter Booking ID: "))
    if bid in bookings:
        print(bookings[bid])
    else:
        print("Not found")

def cancel_ticket():
    global seats
    bid = int(input("Enter Booking ID: "))
    if bid in bookings:
        del bookings[bid]
        seats += 1
        print("Cancelled successfully")
    else:
        print("Invalid ID")

while True:
    print("\n1.Check Availability\n2.Book Ticket\n3.View Ticket\n4.Cancel Ticket\n5.Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        check_availability()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        view_ticket()
    elif choice == "4":
        cancel_ticket()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
