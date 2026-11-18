# Case Study 4: The Fraudulent Event Ticket Scanner 🎟️
# The Logic Focus: Membership testing (in / not in) and list operations.
# The Scenario: A music festival uses digital tickets. The system holds a list of officially generated ticket codes: valid_tickets = ["TX101", "TX102", "TX103", "TX104"]. They also have an empty list called scanned_tickets = [].
# The Rules:
# Simulate a line of guests entering code strings.
# If the code is in valid_tickets and not in scanned_tickets, print "Access Granted!" and add the code to scanned_tickets.
# If the code is in scanned_tickets, print "Access Denied: Ticket already used!".
# If the code is not in valid_tickets
# at all, print "Access Denied: Invalid Ticket!".


# Step 1: Create a list of officially valid tickets
Valid_tickets = ['TX101', 'TX102', 'TX103', 'TX104']

# Step 2: Create an empty list to store scanned tickets
Scanned_tickets = []

# Step 3: Keep the ticket scanner running
while True:

    # Step 4: Get a ticket code from the guest
    ticket = input('Enter your ticket: ')

    # Step 5: Check if the ticket has already been used
    if ticket in Scanned_tickets:
        print('Ticket already used!')
        break  # Stop the loop

    # Step 6: Check if the ticket is not in the valid ticket list
    if ticket not in Valid_tickets:
        print('Invalid Ticket!')
        break  # Stop the loop

    # Step 7: If the ticket is valid and unused, grant access
    else:
        print('Access Granted!')

        # Step 8: Add the successfully scanned ticket to the list
        Scanned_tickets.append(ticket)
