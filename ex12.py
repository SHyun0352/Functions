def main_routine():
    adult_tickets = 0
    child_tickets = 0
    student_tickets = 0
    gift_tickets = 0
    total_sales = 0
    tickets_sold = 0

    ticket_purchase = input("Do you want to sell a ticket? (Y/N): ").upper()
    while ticket_purchase != "N":
        ticket = ticket_selling()
        amount_tickets = int(input("How many of these tickets do you want?: "))
        confirm_amount = input(f"confirm purchases of {amount_tickets} type {ticket} "
                               f"ticket(s)? (Y/N)").upper()
        if confirm_amount == "Y":
            price = num_tickets * float(get_price(ticket))
            total_sales += price
            tickets_sold += num_tickets
            if ticket == "A":
                adult_tickets += num_tickets
            elif ticket == "C":


