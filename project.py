class InteriorDesignProject:
    def __init__(self):
        self.client_info = {}
        self.room_dimensions = {}
        self.flooring_preferences = []
        self.budget = None
        self.store_visit = {}

    def gather_client_info(self):
        self.client_info['name'] = input("Please enter the client's name: ")
        self.client_info['contact'] = input("Please enter the client's contact information: ")

    def gather_room_dimensions(self):
        length = float(input("Please enter the bedroom length (in feet): "))
        width = float(input("Please enter the bedroom width (in feet): "))
        extra_percentage = 0.15  # Standard 15% for waste, etc.
        area = length * width
        total_area = area * (1 + extra_percentage)
        self.room_dimensions['length'] = length
        self.room_dimensions['width'] = width
        self.room_dimensions['total_area'] = total_area
        print(f"Total floor area needed (including waste): {total_area} square feet")

    def gather_flooring_preferences(self):
        while True:
            preference = input("Enter a flooring preference (type 'done' when finished): ")
            if preference.lower() == 'done':
                break
            self.flooring_preferences.append(preference)

    def set_budget(self):
        self.budget = float(input("Please enter the client's budget for flooring: "))

    def plan_store_visit(self):
        self.store_visit['date'] = input("Enter the date for the store visit (MM/DD/YYYY): ")
        self.store_visit['time'] = input("Enter the preferred time for the store visit (HH:MM AM/PM): ")

    def display_project_summary(self):
        with open('projectSummary.md', 'w') as f:
            f.write("\nProject Summary:\n")
            f.write(f"Client Name: {self.client_info.get('name')}\n")
            f.write(f"Contact Information: {self.client_info.get('contact')}\n")
            f.write(f"Room Dimensions: Length - {self.room_dimensions.get('length')} ft, Width - {self.room_dimensions.get('width')} ft, Total Area - {self.room_dimensions.get('total_area')} square feet\n")
            f.write(f"Flooring Preferences: {', '.join(self.flooring_preferences)}\n")
            f.write(f"Budget: ${self.budget}\n")
            f.write(f"Store Visit Scheduled on {self.store_visit.get('date')} at {self.store_visit.get('time')}\n")


# Running the program to interact with the user and gather information
project = InteriorDesignProject()

project.gather_client_info()
project.gather_room_dimensions()
project.gather_flooring_preferences()
project.set_budget()
project.plan_store_visit()

project.display_project_summary()