# InfoSphere
InfoSphere is a mini social platform built with Python, Django, and Bootstrap, allowing users to share their thoughts, images, and text posts while staying connected with the world. Users can also engage with trending content, upvote/downvote posts, and enjoy daily updates and jokes for entertainment.

## Features
- User Registration & Authentication: Register, log in, and manage your profile.
- Post Sharing: Share thoughts, images, and stories with the community.
- Upvote/Downvote: Engage with posts by liking or disliking content.
- Trending Content: Stay updated with the latest and trending posts.
- News Updates: Get the latest news on various topics.
- Random Jokes: Enjoy a dose of humor with daily jokes.
- Search Functionality: Easily search for posts, users, and topics of interest.
- Responsive Design: Optimized for both desktop and mobile devices.
- Profanity Filter: Added a profanity filter to automatically detect and block offensive language in tweets, ensuring a safe and respectful experience for all users.
  
## Tech Stack
- Backend: Python, Django
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite (can be expanded to other databases)
- Authentication: Django's built-in authentication system
- Third-Party Libraries:
    - `better_profanity`: A library for filtering offensive language in user posts.
- External APIs:
    - News API: Provides real-time news updates on various topics.
    - JokeAPI: Delivers random jokes for entertainment.
  
## Home page
![Screenshot 2024-12-25 014338](https://github.com/user-attachments/assets/21ac2c08-30a1-4a4e-b9a2-a5fac0495bf3)

## News section
![Screenshot 2024-12-25 014436](https://github.com/user-attachments/assets/e38ab664-2a69-4a18-8c08-3c89cfff9eb8)

## Joke section
![Screenshot 2024-12-25 014452](https://github.com/user-attachments/assets/eb32f548-5fcd-4c8b-90a6-e5d61a8bcd8d)

## Installation

To run InfoSphere locally, follow the steps below:

### Prerequisites
- Python 3.x
- Django
- Required Python packages listed in requirements.txt
  
## Steps
1. Clone the repository:

```
git clone https://github.com/yourusername/infosphere.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run migrations:
```
python manage.py migrate
```
4. Run the development server:
```
python manage.py runserver
```
Open your browser and go to:
```
http://127.0.0.1:8000/
```

## Running the InfoSphere Project with Docker
1. Clone the repository:

```
git clone https://github.com/yourusername/infosphere.git
```
2. Run the following command to build and start the containers:
```
docker-compose up --build
```

3. Open your browser and go to:
```
http://localhost:8001/
```
4. This will build the Docker images and start the application. You can stop it anytime with CTRL+C and remove containers using:
```
docker-compose down
```

## Contact
Feel free to reach out to me with any questions or feedback at:
- Email: alokkumarjipura9973@gmail.com
- GitHub: https://github.com/alok1304

## License

[MIT License](LICENSE)
