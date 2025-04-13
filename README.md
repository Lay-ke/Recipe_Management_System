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

## 🛠️ API Usage Examples

### Register User

**Endpoint:** `/api/auth/register/`  
**Method:** `POST`  

**Request Body:**
```json
{
    "username": "jacob",
    "email": "jacob@gmail.com",
    "password": "qwerty123",
    "first_name": "Jacob",
    "last_name": "Wood",
    "password2": "qwerty123"
}
```

**Response:**
```json
{
    "message": "User registered successfully", 
    "user": {
        "id": 1,
        "username": "jacob",
        "email": "jacob@gmail.com",
        "first_name": "Jacob",
        "last_name": "Wood"
    }
}
```

---

### Login User

**Endpoint:** `/api/auth/login/`  
**Method:** `POST`  

**Request Body:**
```json
{
    "email": "jacob@gmail.com",
    "password": "qwerty123"
}
```

**Response:**
```json
{
    "message": "Login successful",
    "refresh": "<refresh_token>",
    "token": "<access_token>"
}
```

---

### Create Category

**Endpoint:** `/api/categories/`  
**Method:** `POST`  

**Request Body:**
```json
{
    "name": "Cakes",
    "description": "Foods made with a mix of eggs and flour"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Cakes",
    "description": "Foods made with a mix of eggs and flour"
}
```

---

### Create Ingredients

**Endpoint:** `/api/ingredients/`  
**Method:** `POST`  

**Request Body:**
```json
[
    {
        "name": "eggs",
        "description": "An oval-shaped and fragile commodity"
    },
    {
        "name": "sugar",
        "description": "Gives a sweetened taste to food"
    },
    {
        "name": "flour",
        "description": "A whitish powder"
    }
]
```

**Response:**
```json
[
    {
        "id": 1,
        "name": "eggs",
        "description": "An oval-shaped and fragile commodity"
    },
    {
        "id": 2,
        "name": "sugar",
        "description": "Gives a sweetened taste to food"
    },
    {
        "id": 3,
        "name": "flour",
        "description": "A whitish powder"
    }
]
```

---

### Create Recipe

**Endpoint:** `/api/recipes/`  
**Method:** `POST`  

**Request Body:**
```json
{
    "title": "Chocolate Lava Cake",
    "description": "A rich, gooey chocolate cake with a molten center that is sure to satisfy any chocolate lover.",
    "ingredients": [
        {
            "ingredient_id": 1,
            "unit": "1 cup",
            "quantity": "10 grams"
        },
        {
            "ingredient_id": 2,
            "unit": "1/2 cup",
            "quantity": "10 grams"
        },
        {
            "ingredient_id": 3,
            "unit": "1/4 crate",
            "quantity": "2"
        }
    ],
    "instructions": "1. Preheat the oven to 350°F (175°C). 2. Grease and flour a muffin tin. 3. In a bowl, melt the butter and mix in the cocoa powder, sugar, eggs, vanilla, and milk. 4. Gradually add in the flour, baking powder, and salt, mixing until smooth. 5. Pour the batter into the muffin tin, filling each mold about halfway. 6. Bake for 10-12 minutes until the edges are set but the center is still soft. 7. Serve warm with a scoop of vanilla ice cream.",
    "cook_time": "15 minutes",  
    "prep_time": "10 minutes",  
    "photo": null, 
    "difficulty": 4,
    "servings": "Six persons",
    "user_id": 2,  
    "category_id": 1
}
```

**Response:**
```json
{
    "id": 1,
    "title": "Chocolate Lava Cake",
    "description": "A rich, gooey chocolate cake with a molten center that is sure to satisfy any chocolate lover.",
    "ingredients": [
        {
            "ingredient_id": 1,
            "name": "eggs",
            "unit": "1 cup",
            "quantity": "10 grams"
        },
        {
            "ingredient_id": 2,
            "name": "sugar",
            "unit": "1/2 cup",
            "quantity": "10 grams"
        },
        {
            "ingredient_id": 3,
            "name": "flour",
            "unit": "1/4 crate",
            "quantity": "2"
        }
    ],
    "instructions": "1. Preheat the oven to 350°F (175°C). 2. Grease and flour a muffin tin. 3. In a bowl, melt the butter and mix in the cocoa powder, sugar, eggs, vanilla, and milk. 4. Gradually add in the flour, baking powder, and salt, mixing until smooth. 5. Pour the batter into the muffin tin, filling each mold about halfway. 6. Bake for 10-12 minutes until the edges are set but the center is still soft. 7. Serve warm with a scoop of vanilla ice cream.",
    "cook_time": "15 minutes",  
    "prep_time": "10 minutes",  
    "photo": null, 
    "difficulty": 4,
    "servings": "Six persons",
    "user_id": 2,  
    "category_id": 1
}
```

