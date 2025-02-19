# Gas Utility Service Portal

## Overview

The Gas Utility Service Portal is a web application built with Django that allows users to manage their gas utility service requests efficiently. Users can submit new service requests, track their status, and view updates provided by the support team.

## Features

- User registration and authentication
- Create new service requests
- View and track existing service requests
- Admin panel for managing service requests and customers
- Real-time updates on service request status

## Technologies Used

- Python 3.x
- Django 5.x
- SQLite (or your preferred database)
- HTML, CSS, Bootstrap for frontend
- Font Awesome for icons

## Installation

### Prerequisites

- Python 3.x installed on your machine
- pip (Python package installer)

### Steps to Set Up

1. **Clone the Repository**

   ```bash
   git clone https://github.com/jet-niraj/gas-utility-service-portal.git
   cd gas-utility-service-portal
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser (for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

7. **Access the Application**

   Open your web browser and go to `http://127.0.0.1:8000/` to access the application.

   For the admin panel, go to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you created.

## Usage

- **User Registration**: New users can register by clicking on the "Register" link on the homepage.
- **Submitting Requests**: After logging in, users can submit new service requests.
- **Tracking Requests**: Users can view their submitted requests and see updates on their status.

## Admin Panel

The admin panel allows administrators to manage customers and service requests. Admins can view all service requests, update their status, and manage customer information.


```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django documentation for guidance on building web applications.
- Bootstrap for responsive design.
- Font Awesome for icons.

## Screenshots 📸

### Home Page  
[![Home Page](screenshots/homepage.png)](screenshots/homepage.png)

### Service Request Page  
[![Service Request](screenshots/service_request.png)](screenshots/service_request.png)

### User Registration Page  
[![User Registration](screenshots/user_registration.png)](screenshots/user_registration.png)

### User Login Page  
[![User Login](screenshots/user_login.png)](screenshots/user_login.png)

### User Request List  
[![User Request List](screenshots/user_request_list.png)](screenshots/user_request_list.png)

### Service Request Detail  
[![Service Request Detail](screenshots/service_request_detail.png)](screenshots/service_request_detail.png)

[![Home Page](https://raw.githubusercontent.com/jet-niraj/gas-utility-django/main/screenshots/home.png)](https://raw.githubusercontent.com/jet-niraj/gas-utility-django/main/screenshots/home.png)

### Add New Request  
[![Add New Request](https://raw.githubusercontent.com/jet-niraj/gas-utility-django/main/screenshots/add_new_request.png)](https://raw.githubusercontent.com/jet-niraj/gas-utility-django/main/screenshots/add_new_request.png)



















