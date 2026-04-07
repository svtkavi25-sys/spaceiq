**SpaceIQ - Occupancy Detection System**
SpaceIQ is a Django-based web application for real-time occupancy detection using computer vision. It leverages OpenCV and AI-powered people detection to monitor and track people in spaces, providing insights into occupancy levels.
 
**Features** 
Real-time people detection using computer vision
Web-based dashboard for monitoring occupancy
Camera integration for live video feed
Historical data tracking and analytics
RESTful API for integration with other systems
Configurable detection parameters
Installation
Prerequisites
Python 3.9 or higher
Virtual environment (recommended)
Setup
Clone the repository:

Create and activate a virtual environment:

Install dependencies:

Run database migrations:

Create a superuser (optional, for admin access):

**Usage**
Start the Django development server:

Open your browser and navigate to http://127.0.0.1:8000/

Access the admin panel at http://127.0.0.1:8000/admin/ (if superuser created)

Testing the People Counter
Run the standalone people counter script:

Or run the test script:
 
**Project Structure **
occupancy - Main Django app
ai/detect_people.py - AI-powered people detection logic
camera.py - Camera handling utilities
models.py - Database models
views.py - Web views and API endpoints
spaceiq - Django project settings
people_counter.py - Standalone people counter script
test_camera.py - Camera testing utilities
API Endpoints
GET /api/occupancy/ - Get current occupancy data
POST /api/occupancy/ - Update occupancy data
GET /api/camera/status/ - Check camera status
Configuration
Update settings in settings.py:

**Database configuration**
Camera settings
Detection parameters
Contributing
Fork the repository
Create a feature branch
Make your changes
Submit a pull request
License
This project is licensed under the MIT License - see the LICENSE file for details.

**Technologies Used**
Django 4.2
OpenCV 4.13
NumPy 2.0
Pillow 11.3
Matplotlib 3.9
Hugging Face Transformers (for AI detection)
