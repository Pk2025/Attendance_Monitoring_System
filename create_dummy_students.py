import os
import sys
import django
import random
from datetime import datetime
from django.core.files.storage import FileSystemStorage

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

from student_management_app.models import CustomUser, Students, Courses, SessionYearModel

def create_dummy_students(num_students=10):
    """Create dummy student records"""
    
    # Sample data
    first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'James', 'Emma', 'Robert', 'Olivia', 
                  'William', 'Sophia', 'Joseph', 'Ava', 'Thomas', 'Isabella', 'Charles', 'Mia', 'Daniel', 'Charlotte']
    
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez',
                 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin']
    
    addresses = [
        '123 Main St, Anytown, AN',
        '456 Elm St, Somewhere, SO',
        '789 Oak St, Nowhere, NO',
        '101 Pine St, Everywhere, EV',
        '202 Maple St, Anywhere, AW',
        '303 Cedar St, Someplace, SP',
        '404 Birch St, Noplace, NP',
        '505 Walnut St, Everyplace, EP',
        '606 Cherry St, Anyplace, AP',
        '707 Spruce St, Somewhere Else, SE'
    ]
    
    # Get available courses and session years
    courses = list(Courses.objects.all())
    session_years = list(SessionYearModel.object.all())
    
    if not courses:
        print("Error: No courses found. Please create at least one course first.")
        return
    
    if not session_years:
        print("Error: No session years found. Please create at least one session year first.")
        return
    
    # Default profile pic - use an existing profile picture from media
    profile_pics = ['python-student-8_TPtYOmi.png', 'python-student20.jpg', 'python-student5.png', 'python-student6.png']
    
    successful_creations = 0
    
    # Create students
    for i in range(num_students):
        try:
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            username = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 999)}"
            email = f"{username}@example.com"
            
            # Check if user with this email already exists
            if CustomUser.objects.filter(email=email).exists():
                print(f"Skipping {email} - email already exists")
                continue
                
            # Create CustomUser
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password="test123",  # Default password for all dummy students
                first_name=first_name,
                last_name=last_name,
                user_type=3  # 3 for student
            )
            
            # Update student details
            student = Students.objects.get(admin=user)
            student.gender = random.choice(['Male', 'Female'])
            student.address = random.choice(addresses)
            student.course_id = random.choice(courses)
            student.session_year_id = random.choice(session_years)
            
            # Random profile pic from available ones
            student.profile_pic = random.choice(profile_pics)
            
            student.save()
            
            successful_creations += 1
            print(f"Created student: {first_name} {last_name} ({email})")
            
        except Exception as e:
            print(f"Error creating student: {str(e)}")
    
    print(f"\nSuccessfully created {successful_creations} students")

if __name__ == "__main__":
    print("Creating dummy student records...")
    create_dummy_students() 