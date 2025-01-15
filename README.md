# Taaza Khabr

Taaza Khabr is a web application that delivers daily news updates. Built with FastAPI and Jinja2, this project focuses on providing a dynamic, user-friendly interface for accessing news articles.

## Features
- **Dynamic News Updates:** Fetch and display the latest news.
- **Fast and Lightweight:** Powered by FastAPI for high performance.
- **Customizable Templates:** Use of Jinja2 for rendering dynamic HTML templates.

## Prerequisites
To run this project, ensure you have the following installed:
- Python 3.8 or later
- pip (Python package manager)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/taza-khabr.git
   cd taaza_khabr
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
1. Start the FastAPI development server:
   ```bash
   uvicorn main:app --reload
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

## Project Structure
```
.
├── app
│   ├── templates          # Jinja2 templates for HTML rendering
│   ├── static             # Static files (CSS, JavaScript, images)
│   ├── routers            # API route handlers
│   └── main.py            # Application entry point
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── .gitignore             # Ignored files for Git
```

## Dependencies
- **FastAPI**: Web framework for building APIs.
- **Jinja2**: Template engine for rendering dynamic HTML.
- **Uvicorn**: ASGI server for running the FastAPI application.

Install all dependencies via `requirements.txt`:
```
fastapi
jinja2
uvicorn
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

**Happy Coding!**
