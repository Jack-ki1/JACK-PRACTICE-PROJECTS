class MedicalCentre:
    def __init__(self):
        self.services = {
            "1": "Mental Health",
            "2": "Oral Health",
            "3": "Common Check-up",
            "4": "Family Health",
            "5": "Specialist Appointment",
            "6": "Emergency",
            "7": "Visiting a Patient",
            "8": "Pharmacy",
            "9": "Laboratory Tests",
            "10": "Radiology",
            "11": "Physiotherapy",
            "12": "Dental Care"
        }

    def display_services(self):
        print("We offer the following services:")
        for key, value in self.services.items():
            print(f"{key}. {value}")

    def get_patient_name(self):
        return input("Enter your name: ")

    def get_service_choice(self):
        while True:
            choice = input("Choose a service (1-12): ")
            if choice in self.services:
                return choice
            else:
                print("Invalid choice. Please choose a number between 1 and 12.")

    def get_appointment_time(self):
        while True:
            time = input("Choose an appointment time (morning/afternoon/evening): ")
            if time.lower() in ["morning", "afternoon", "evening"]:
                return time
            else:
                print("Invalid time. Please choose morning, afternoon, or evening.")

    def book_appointment(self, name, service, time):
        print(f"Booking appointment for {name} for {self.services[service]} at {time}...")
        print("Appointment booked successfully!")

    def main(self):
        print("Welcome to our medical centre!")
        name = self.get_patient_name()
        self.display_services()
        service = self.get_service_choice()
        time = self.get_appointment_time()
        self.book_appointment(name, service, time)

if __name__ == "__main__":
    medical_centre = MedicalCentre()
    medical_centre.main()