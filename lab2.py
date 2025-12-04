# HW2 - Students Class 

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passed(self):
        if self.grade >= 50:
            return "ناجح"
        else:
            return "راسب"


# إنشاء قائمة طلاب
group = [
    Student("Lama", 80),
    Student("Raghad", 45),
    Student("Dina", 90),
    Student("Aya", 30),
    Student("Hadeel", 60)
]

passed = []
failed = []

for s in group:
    if s.is_passed() == "ناجح":
        passed.append(s.name)
    else:
        failed.append(s.name)

print("Passed Students:", passed)
print("Failed Students:", failed)

print("Total Passed:", len(passed))
print("Total Failed:", len(failed))
