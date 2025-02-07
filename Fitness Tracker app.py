class Workout:
    def __init__(self, exercise_type, duration, calories_burned):
        self.exercise_type = exercise_type
        self.duration = duration  # in minutes
        self.calories_burned = calories_burned  # in kcal

    def __str__(self):
        return f"{self.exercise_type} for {self.duration} minutes, burned {self.calories_burned} kcal"
import json

class FitnessTracker:
    def __init__(self):
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def view_summary(self):
        total_duration = sum([workout.duration for workout in self.workouts])
        total_calories = sum([workout.calories_burned for workout in self.workouts])
        print(f"Total Workouts: {len(self.workouts)}")
        print(f"Total Duration: {total_duration} minutes")
        print(f"Total Calories Burned: {total_calories} kcal")

    def save_data(self, filename="workouts.json"):
        data = [{"exercise_type": w.exercise_type, "duration": w.duration, "calories_burned": w.calories_burned} for w in self.workouts]
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"Data saved to {filename}")

    def load_data(self, filename="workouts.json"):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            self.workouts = [Workout(d['exercise_type'], d['duration'], d['calories_burned']) for d in data]
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print("No previous data found.")
def main():
    tracker = FitnessTracker()
    tracker.load_data()

    while True:
        print("\n1. Add Workout")
        print("2. View Summary")
        print("3. Save Data")
        print("4. Load Data")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            exercise_type = input("Enter exercise type (e.g., Running, Cycling): ")
            duration = int(input("Enter duration (in minutes): "))
            calories_burned = int(input("Enter calories burned: "))
            workout = Workout(exercise_type, duration, calories_burned)
            tracker.add_workout(workout)
            print("Workout added successfully!")

        elif choice == "2":
            tracker.view_summary()

        elif choice == "3":
            tracker.save_data()

        elif choice == "4":
            tracker.load_data()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
