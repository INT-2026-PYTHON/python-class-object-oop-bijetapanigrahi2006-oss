"""
## 3. Student Class with Marks List  *(Medium)*

=================================================
STUDENT CLASS WITH MARKS LIST
=================================================

Problem Statement:
Write a Python CLASS called `Student` that
stores a student's name, roll number, and a
LIST of subject marks. The class should be
able to compute statistics about the marks
and decide a grade.

This problem reinforces:
   - storing a LIST as an instance attribute
   - mutating that list through methods
   - calling one instance method from another
     using `self`

-------------------------------------------------
Instructions:
1. Define a class:
      class Student:
2. Constructor:
      def __init__(self, name, roll, marks=None):
          - if marks is None, set self.marks = []
            (do NOT use marks=[] as a default
             argument — it is a shared mutable
             default)
          - store self.name and self.roll
3. Instance methods:
      - add_mark(self, mark)
            * append a single mark to self.marks
            * reject negative marks or marks > 100
              with a message
      - total(self)          -> sum of marks
      - average(self)        -> total / count,
                                 0 if no marks
      - grade(self)          -> use self.average():
                                  >= 90 -> "A"
                                  >= 75 -> "B"
                                  >= 50 -> "C"
                                  else  -> "F"
      - report(self)         -> return a TUPLE:
              (name, roll, total, average, grade)
4. In the driver code:
      - create AT LEAST TWO students
      - add marks for each student using
        add_mark() in a for loop
      - print each student's report tuple
5. Do NOT use:
   - statistics / numpy modules
   - class attributes for marks (must be on
     each instance)

-------------------------------------------------
Input Example:
s1 = Student("Alice", 101)
for m in [90, 85, 95]:
    s1.add_mark(m)

s2 = Student("Bob", 102)
for m in [40, 55, 60]:
    s2.add_mark(m)

Output Example:
('Alice', 101, 270, 90.0, 'A')
('Bob',   102, 155, 51.666..., 'C')

-------------------------------------------------
Explanation:
- `self.marks` is a SEPARATE list for each
  student object, so Alice's marks do not mix
  with Bob's.
- `grade(self)` calls `self.average()`, which
  shows how one method can use another method
  on the SAME object through `self`.
=================================================

"""
from collections import Counter

def find_words_in_grid(file_path, grid):
    # Step 1: Flatten the grid and count the available frequency of each letter
    flat_grid_chars = []
    for row in grid:
        for char in row:
            flat_grid_chars.append(char.lower())
            
    grid_counts = Counter(flat_grid_chars)
    matching_words = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip()
                if not word:
                    continue
                
                # Step 2: Count the frequency of characters in the current word
                word_lower = word.lower()
                word_counts = Counter(word_lower)
                
                # Step 3: Verify if the grid can completely supply the word
                can_form_word = True
                for char, count in word_counts.items():from collections import Counter

def find_words_in_grid(file_path, grid):
    # Step 1: Flatten the grid and count the available frequency of each letter
    flat_grid_chars = []
    for row in grid:
        for char in row:
            flat_grid_chars.append(char.lower())
            
    grid_counts = Counter(flat_grid_chars)
    matching_words = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip()
                if not word:
                    continue
                
                # Step 2: Count the frequency of characters in the current word
                word_lower = word.lower()
                word_counts = Counter(word_lower)
                
                # Step 3: Verify if the grid can completely supply the word
                can_form_word = True
                for char, count in word_counts.items():
                    # If a letter is missing or required more times than available
