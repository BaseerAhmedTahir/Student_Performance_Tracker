class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

    def is_passing(self, passing_threshold=40):
        return all(score >= passing_threshold for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        if not self.students:
            return 0
        return sum(student.calculate_average() for student in self.students.values()) / len(self.students)

    def display_student_performance(self):
        if not self.students:
            print("No students in the tracker.")
            return

        print("\n--- Student Performance Report ---")
        for student in self.students.values():
            avg_score = student.calculate_average()
            pass_status = "PASSING" if student.is_passing() else "NEEDS IMPROVEMENT"
            print(f"Name: {student.name}")
            print(f"Average Score: {avg_score:.2f}")
            print(f"Status: {pass_status}")
            print("Scores:", ", ".join(map(str, student.scores)))
            print()

        print(f"Class Average: {self.calculate_class_average():.2f}")


def main():
    tracker = PerformanceTracker()

    while True:
        try:
            name = input("Enter student name (or 'done' to finish): ").strip()
            
            if name.lower() == 'done':
                break

            scores = []
            subjects = ['Math', 'Science', 'English']
            for subject in subjects:
                while True:
                    try:
                        score = int(input(f"Enter {subject} score: "))
                        if 0 <= score <= 100:
                            scores.append(score)
                            break
                        else:
                            print("Score must be between 0 and 100.")
                    except ValueError:
                        print("Invalid input. Please enter a numeric score.")

            tracker.add_student(name, scores)

        except Exception as e:
            print(f"An error occurred: {e}")

    tracker.display_student_performance()


if __name__ == "__main__":
    main()
