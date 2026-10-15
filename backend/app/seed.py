# Run this once to fill the employees table with sample data:
#   python -m app.seed
from datetime import date

from app.core.database import Base, engine, SessionLocal
from app.database_models import Employee

sample_employees = [
    {"name": "Michael Verma", "email": "michael.verma1@example.com", "department": "Marketing", "designation": "Content Manager", "date_of_joining": date(2025, 11, 26)},
    {"name": "Michael Sharma", "email": "michael.sharma2@example.com", "department": "Sales", "designation": "Sales Manager", "date_of_joining": date(2025, 7, 7)},
    {"name": "William Brown", "email": "william.brown3@example.com", "department": "Product", "designation": "Product Designer", "date_of_joining": date(2022, 5, 25)},
    {"name": "Aavya Smith", "email": "aavya.smith4@example.com", "department": "HR", "designation": "HR Manager", "date_of_joining": date(2025, 3, 20)},
    {"name": "Vihaan Miller", "email": "vihaan.miller5@example.com", "department": "Engineering", "designation": "QA Engineer", "date_of_joining": date(2021, 6, 21)},
    {"name": "Robert Miller", "email": "robert.miller6@example.com", "department": "Operations", "designation": "Operations Coordinator", "date_of_joining": date(2022, 5, 10)},
    {"name": "Emma Joshi", "email": "emma.joshi7@example.com", "department": "HR", "designation": "HR Specialist", "date_of_joining": date(2024, 7, 6)},
    {"name": "Mia Mehta", "email": "mia.mehta8@example.com", "department": "Engineering", "designation": "Software Engineer", "date_of_joining": date(2023, 10, 24)},
    {"name": "Sai Singh", "email": "sai.singing9@example.com", "department": "Sales", "designation": "Account Executive", "date_of_joining": date(2024, 6, 2)},
    {"name": "Aavya Jones", "email": "aavya.jones10@example.com", "department": "Sales", "designation": "Sales Development Rep", "date_of_joining": date(2022, 10, 21)},
    {"name": "Arjun Jones", "email": "arjun.jones11@example.com", "department": "Finance", "designation": "Financial Analyst", "date_of_joining": date(2023, 7, 24)},
    {"name": "Vivaan Joshi", "email": "vivaan.joshi12@example.com", "department": "Finance", "designation": "Accountant", "date_of_joining": date(2024, 6, 2)},
    {"name": "Mia Singh", "email": "mia.singh13@example.com", "department": "Product", "designation": "Product Manager", "date_of_joining": date(2022, 8, 20)},
    {"name": "Riya Williams", "email": "riya.williams14@example.com", "department": "Product", "designation": "Product Designer", "date_of_joining": date(2023, 11, 23)},
    {"name": "Ava Mehta", "email": "ava.mehta15@example.com", "department": "Engineering", "designation": "Senior Engineer", "date_of_joining": date(2023, 1, 9)},
    {"name": "David Brown", "email": "david.brown16@example.com", "department": "Engineering", "designation": "DevOps Engineer", "date_of_joining": date(2021, 5, 12)},
    {"name": "Sophia Verma", "email": "sophia.verma17@example.com", "department": "HR", "designation": "Recruiter", "date_of_joining": date(2021, 10, 6)},
    {"name": "Emma Kumar", "email": "emma.kumar18@example.com", "department": "Engineering", "designation": "QA Engineer", "date_of_joining": date(2025, 4, 18)},
    {"name": "Riya Miller", "email": "riya.miller19@example.com", "department": "Engineering", "designation": "Senior Engineer", "date_of_joining": date(2025, 11, 25)},
    {"name": "Ananya Johnson", "email": "ananya.johnson20@example.com", "department": "HR", "designation": "HR Manager", "date_of_joining": date(2023, 11, 17)},
    {"name": "Aditya Smith", "email": "aditya.smith21@example.com", "department": "Sales", "designation": "Sales Manager", "date_of_joining": date(2023, 12, 19)},
    {"name": "Robert Smith", "email": "robert.smith22@example.com", "department": "Operations", "designation": "Operations Coordinator", "date_of_joining": date(2022, 12, 5)},
    {"name": "Sophia Smith", "email": "sophia.smith23@example.com", "department": "Operations", "designation": "Operations Manager", "date_of_joining": date(2024, 7, 26)},
    {"name": "Riya Singh", "email": "riya.singh24@example.com", "department": "HR", "designation": "HR Specialist", "date_of_joining": date(2023, 5, 15)},
    {"name": "Vivaan Kumar", "email": "vivaan.kumar25@example.com", "department": "Finance", "designation": "Finance Manager", "date_of_joining": date(2021, 9, 23)},
    {"name": "Olivia Miller", "email": "olivia.miller26@example.com", "department": "Marketing", "designation": "SEO Expert", "date_of_joining": date(2022, 2, 28)},
    {"name": "John Johnson", "email": "john.johnson27@example.com", "department": "Engineering", "designation": "QA Engineer", "date_of_joining": date(2024, 9, 13)},
    {"name": "Sai Johnson", "email": "sai.johnson28@example.com", "department": "Engineering", "designation": "Software Engineer", "date_of_joining": date(2023, 4, 8)},
    {"name": "Riya Brown", "email": "riya.brown29@example.com", "department": "Sales", "designation": "Sales Manager", "date_of_joining": date(2024, 5, 11)},
    {"name": "William Joshi", "email": "william.joshi30@example.com", "department": "Marketing", "designation": "Marketing Specialist", "date_of_joining": date(2021, 6, 26)},
    {"name": "Sophia Miller", "email": "sophia.miller31@example.com", "department": "Finance", "designation": "Finance Manager", "date_of_joining": date(2021, 9, 16)},
    {"name": "Emma Verma", "email": "emma.verma32@example.com", "department": "Engineering", "designation": "Senior Engineer", "date_of_joining": date(2023, 5, 17)},
    {"name": "David Singh", "email": "david.singh33@example.com", "department": "Engineering", "designation": "DevOps Engineer", "date_of_joining": date(2022, 6, 11)},
    {"name": "Arjun Kumar", "email": "arjun.kumar34@example.com", "department": "Marketing", "designation": "SEO Expert", "date_of_joining": date(2024, 6, 30)},
    {"name": "Diya Jones", "email": "diya.jones35@example.com", "department": "Marketing", "designation": "Content Manager", "date_of_joining": date(2021, 10, 1)},
    {"name": "Aavya Sharma", "email": "aavya.sharma36@example.com", "department": "Finance", "designation": "Accountant", "date_of_joining": date(2021, 4, 18)},
    {"name": "David Miller", "email": "david.miller37@example.com", "department": "Product", "designation": "Product Manager", "date_of_joining": date(2023, 8, 12)},
    {"name": "Reyansh Brown", "email": "reyansh.brown38@example.com", "department": "HR", "designation": "Recruiter", "date_of_joining": date(2023, 9, 17)},
    {"name": "Ava Williams", "email": "ava.williams39@example.com", "department": "Engineering", "designation": "Senior Engineer", "date_of_joining": date(2025, 9, 3)},
    {"name": "Diya Williams", "email": "diya.williams40@example.com", "department": "Product", "designation": "Product Manager", "date_of_joining": date(2025, 4, 15)},
    {"name": "Isabella Smith", "email": "isabella.smith41@example.com", "department": "Sales", "designation": "Account Executive", "date_of_joining": date(2021, 11, 23)},
    {"name": "Aarav Kumar", "email": "aarav.kumar42@example.com", "department": "Operations", "designation": "Operations Coordinator", "date_of_joining": date(2025, 8, 15)},
    {"name": "Ananya Sharma", "email": "ananya.sharma43@example.com", "department": "Sales", "designation": "Account Executive", "date_of_joining": date(2025, 7, 20)},
    {"name": "Emma Smith", "email": "emma.smith44@example.com", "department": "Engineering", "designation": "Software Engineer", "date_of_joining": date(2024, 2, 6)},
    {"name": "Aditya Williams", "email": "aditya.williams45@example.com", "department": "Engineering", "designation": "DevOps Engineer", "date_of_joining": date(2021, 8, 25)},
    {"name": "David Mehta", "email": "david.mehta46@example.com", "department": "Marketing", "designation": "Marketing Specialist", "date_of_joining": date(2021, 12, 19)},
    {"name": "Aavya Jones", "email": "aavya.jones47@example.com", "department": "Finance", "designation": "Financial Analyst", "date_of_joining": date(2022, 11, 14)},
    {"name": "Riya Johnson", "email": "riya.johnson48@example.com", "department": "Marketing", "designation": "SEO Expert", "date_of_joining": date(2024, 10, 8)},
    {"name": "Olivia Verma", "email": "olivia.verma49@example.com", "department": "Product", "designation": "Product Designer", "date_of_joining": date(2023, 1, 19)},
    {"name": "Michael Singh", "email": "michael.singh50@example.com", "department": "HR", "designation": "HR Specialist", "date_of_joining": date(2024, 1, 2)},
]


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(Employee).count() > 0:
            print("Employees already exist. Skipping seed.")
            return

        for emp in sample_employees:
            db.add(Employee(**emp))
        db.commit()
        print(f"Added {len(sample_employees)} employees.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
