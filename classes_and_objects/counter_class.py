"""
## 4. Counter Class with Class vs Instance Attributes  *(Medium)*

=================================================
COUNTER WITH CLASS VS INSTANCE ATTRIBUTES
=================================================

Problem Statement:
Write a Python CLASS called `Counter` that
maintains:
   - an INSTANCE counter for the current
     object (its own count)
   - a CLASS counter shared across ALL objects
     (the total count across the program)

The goal of this problem is to understand the
difference between:
   - INSTANCE attributes  (one per object,
     stored on `self`)
   - CLASS attributes     (one for the whole
     class, stored on the class itself)

-------------------------------------------------
Instructions:
1. Define the class:
      class Counter:
          total = 0       # CLASS attribute

          def __init__(self, name):
              self.name  = name
              self.count = 0   # INSTANCE attribute
2. Instance methods:
      - increment(self, step=1)
            * self.count  += step
            * Counter.total += step
        (note: use Counter.total, NOT self.total,
         when UPDATING the class attribute)
      - reset(self)
            * sets self.count back to 0
            * does NOT touch Counter.total
      - __str__(self)
            * "<name>: count=<count>"
3. Class method (regular method that touches
   class attribute):
      - show_total() can be a @staticmethod or
        a regular function inside the class
        that returns Counter.total
4. In the driver code:
      - create at least THREE Counter objects
      - call increment() a different number of
        times on each
      - reset ONE of them
      - print each object using print(c)
      - print the overall Counter.total
5. Do NOT use:
   - the global keyword
   - any external library

-------------------------------------------------
Input Example:
c1 = Counter("clicks")
c2 = Counter("views")
c3 = Counter("downloads")

for _ in range(3):
    c1.increment()
for _ in range(5):
    c2.increment()
c3.increment(10)
c1.reset()

Output Example:
clicks:    count=0
views:     count=5
downloads: count=10
Total across all counters: 18

-------------------------------------------------
Explanation:
- `c1.count`, `c2.count`, and `c3.count` are
  three SEPARATE numbers, because each lives
  on its own object.
- `Counter.total` is a SINGLE number shared by
  the whole class. Every increment() call adds
  to it, including the ones that were later
  reset on the instance.
- This is why c1 shows 0 but the class total
  is still 18 (3 + 5 + 10).
=================================================

"""
def find_single_vowel_words(file_path):
    # Define the set of recognized standard vowels
    vowels_set = {'a', 'e', 'i', 'o', 'u'}
    matching_words = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip()
                if not word:
                    continue
                
                # Extract all unique vowels present in the current word
                word_vowels = set(word.lower()) & vowels_set
                
                # The word is a match if it contains exactly ONE unique vowel type
                if len(word_vowels) == 1:
                    matching_words.append(word)
                    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []

    # Print results matching the assignment requirements
    print("Words containing exactly one unique vowel:")
    print(matching_words)
    return matching_words


# --- Simulation / Driver Code ---
_name_ = " "
if _name_ == "_main_":
    # Create a temporary file to replicate your example context
    sample_filename = "sowpods.txt"
    sample_words = [
        "apple",    # Vowels: 'a', 'e' (2 unique) -> Skip
        "banana",   # Vowels: 'a' only (1 unique)  -> Match
        "cherry",   # Vowels: 'e' only (1 unique)  -> Match
        "cool",     # Vowels: 'o' only (1 unique)  -> Match
        "education" # Vowels: 'a', 'e', 'i', 'o', 'u' -> Skip
    ]
    
    with open(sample_filename, "w", encoding="utf-8") as f:
        f.write("\n".join(sample_words))
        
    # Run the function on the sample file
    find_single_vowel_words(sample_filename)
