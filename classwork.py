class Student:
    # Class attribute
    school = "Bright Future Academy"

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.__score = score  # Private attribute for encapsulation

    # Property Getter for score
    @property
    def score(self):
        return self.__score

    # Property Setter for score with validation (0 to 100)
    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError("Score must be between 0 and 100.")

    # Class Method to change the school name for all students
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    # Static Method to check if a score is a passing score (50 or above)
    @staticmethod
    def is_passed(score):
        return score >= 50

    # Instance Method to display student information
    def display_info(self):
        status = "Passed" if self.is_passed(self.__score) else "Failed"
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Score: {self.__score}")
        print(f"School: {Student.school}")
        print(f"Status: {status}\n")


# --- Testing the Program ---
if __name__ == "__main__":
    # 1. Creating student objects
    student1 = Student("Ada", 16, 75)
    student2 = Student("John", 17, 42)

    print("--- Initial Student Information ---")
    student1.display_info()
    student2.display_info()

    # 3. Testing Property Setter (Updating John's score)
    print("--- Updating John's Score ---")
    student2.score = 55
    student2.display_info()

    # 4. Testing Class Method (Changing School Name)
    print("--- Changing School Name ---")
    Student.change_school("Bright Academy")
    student1.display_info()
    student2.display_info()