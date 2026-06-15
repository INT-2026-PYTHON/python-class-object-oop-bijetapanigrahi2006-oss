"""
## 2. Bank Account Class  *(Medium)*

=================================================
BANK ACCOUNT CLASS
=================================================

Problem Statement:
Write a Python CLASS called `BankAccount`
that represents a simple bank account. Each
account has an account holder's name, a
unique account number, and a balance that
starts at 0 unless an opening balance is
given.

The class must support deposits, withdrawals,
and balance checks. Reject invalid operations
(negative amounts, overdrafts) by printing a
clear message — do NOT crash.

-------------------------------------------------
Instructions:
1. Define a class:
      class BankAccount:
2. Constructor:
      def __init__(self, name, account_number,
                   opening_balance=0):
          - validate that opening_balance >= 0
          - store name, account_number, balance
            on `self`
3. Instance methods:
      - deposit(self, amount)
            * reject amount <= 0 with a message
            * otherwise add to balance
      - withdraw(self, amount)
            * reject amount <= 0
            * reject if amount > balance
            * otherwise subtract from balance
      - get_balance(self)
            * return the current balance
      - __str__(self)
            * return a friendly string like:
              "Account[001 - Alice]: $500"
4. In the driver code:
      - create AT LEAST TWO accounts
      - perform some valid deposits / withdraws
      - perform AT LEAST ONE invalid operation
        (negative amount or overdraft) on each
        account to show the rejection message
      - print each account using print(acc),
        which triggers __str__
5. Do NOT use:
   - class-level mutable defaults (e.g. a list
     as default argument)
   - global variables

-------------------------------------------------
Input Example:
a1 = BankAccount("Alice", "001", 500)
a2 = BankAccount("Bob",   "002")
a1.deposit(200)
a1.withdraw(100)
a1.withdraw(2000)   # overdraft -> rejected
a2.deposit(-50)     # invalid   -> rejected
a2.deposit(300)

Output Example:
Insufficient funds for Alice (balance=600, asked=2000)
Deposit amount must be > 0 (got -50)
Account[001 - Alice]: $600
Account[002 - Bob]:   $300

-------------------------------------------------
Explanation:
- `self.balance` is independent for every
  object, so Alice and Bob keep separate
  balances.
- Validation in `deposit` and `withdraw` shows
  how methods use `self` to read AND update
  state on the same object.
- `__str__` returns the human-readable form
  used by print().
=================================================

"""

def find_words_from_letters(file_path, allowed_letters):
    
    allowed_set = set(allowed_letters.lower())
    matching_words = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip()
                if not word:
                    continue

                word_set = set(word.lower())
                
                if word_set.issubset(allowed_set):
                    matching_words.append(word)
                    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []

    print(f"Words made entirely from '{allowed_letters}':")
    print(matching_words)
    return matching_words


# --- Simulation / Driver Code ---
_name_ = " "
if _name_ == "_main_":
  
    sample_filename = "sowpods.txt"
    sample_words = [
        "apple",
        "pool",
        "loop",
        "pop",
        "polo",
        "banana"
    ]
    
    with open(sample_filename, "w", encoding="utf-8") as f:
        f.write("\n".join(sample_words))
        
    # Execute the function searching for words made only from letters in "orlop"
    find_words_from_letters(sample_filename, "orlop")