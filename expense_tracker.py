"""
Project 2: Expense Tracker
DecodeLabs Industrial Training Kit
Concept: Accumulator Pattern + Defensive Coding
"""

def expense_tracker():
    # ---------- INITIALIZATION (State) ----------
    total = 0.0      # accumulator, initialized OUTSIDE the loop
    count = 0         # tracks how many valid expenses were entered

    print("=" * 40)
    print("       WELCOME TO EXPENSE TRACKER")
    print("=" * 40)
    print("Enter your expenses one by one.")
    print("Type 'done' when you are finished.\n")

    # ---------- PROCESS (Continuous Audit Loop) ----------
    while True:
        entry = input("Enter expense amount: ").strip()

        if entry == "":
            print("Empty input. Please enter a number or 'done'.\n")
            continue

        # Sentinel value check — graceful exit
        if entry.lower() == "done":
            break

        # Defensive coding — validate input before processing
        try:
            expense = float(entry)

            if expense < 0:
                print("Invalid: Expense cannot be negative. Try again.\n")
                continue

            total += expense        # accumulator pattern: total = total + new_expense
            count += 1
            print(f"Added Rs. {expense:.2f} | Running Total: Rs. {total:.2f}\n")

        except ValueError:
            print("Invalid input. Please enter a valid number (e.g. 100 or 49.5).\n")

    # ---------- OUTPUT (Final Report) ----------
    print("=" * 40)
    print("           FINAL REPORT")
    print("=" * 40)
    print(f"Total Transactions : {count}")
    print(f"Total Spent        : Rs. {total:.2f}")
    if count > 0:
        print(f"Average Expense    : Rs. {total/count:.2f}")
    print("=" * 40)


if __name__ == "__main__":
    expense_tracker()
