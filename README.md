# Recipe Management API

A comprehensive Django REST API for managing recipes, ingredients, categories, and reviews.

## 📋 Overview

Recipe Management API is a powerful backend solution for recipe-focused applications. It enables users to create, discover, and share recipes, search by ingredients, categorize culinary creations, and provide feedback through ratings and reviews.

## ✨ Features

- **User Authentication** - Secure registration and token-based authentication
- **Recipe Management** - Full CRUD operations for recipes with detailed information
- **Ingredient System** - Searchable ingredient database with quantities and measurements
- **Categorization** - Organize recipes by categories for easy discovery
- **Reviews & Ratings** - Allow users to rate and review recipes
- **Advanced Search** - Find recipes by title, ingredients, or category
- **User Profiles** - Personalized profiles with user-created recipe collections

## 🔧 Technology Stack

- **Django** - Web framework
- **Django REST Framework** - API toolkit
- **PostgreSQL** - Database (recommended)
- **Token Authentication** - Secure API access
- **Heroku/PythonAnywhere** - Deployment options

## 📦 Project Structure

```
recipe_api/
├── accounts/         # User authentication and profiles
├── recipes/          # Core recipe functionality
├── ingredients/      # Ingredient management
├── categories/       # Recipe categorization
├── reviews/          # Ratings and reviews
├── api/              # API configuration
├── config/           # Project settings
└── requirements.txt  # Dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

1. **Clone the repository**

    ```sh
    git clone https://github.com/yourusername/recipe-management-api.git
    cd recipe-management-api
    ```

2. **Set up a virtual environment**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**

    ```sh
    cp .env.example .env
    # Edit .env with your configuration
    ```

5. **Run migrations**

    ```sh
    python manage.py migrate
    ```

6. **Create a superuser**

    ```sh
    python manage.py createsuperuser
    ```

7. **Start the development server**

    ```sh
    python manage.py runserver
    ```

    Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the API.

## 📚 API Documentation

Once the server is running, visit [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/) for interactive API documentation.

### Main Endpoints

- `/api/auth/` - Authentication endpoints
- `/api/recipes/` - Recipe management
- `/api/categories/` - Category management
- `/api/ingredients/` - Ingredient management
- `/api/reviews/` - Reviews and ratings