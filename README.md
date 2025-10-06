# Book Tracker & Reading Journal

A full-stack web application that allows users to track their reading progress, maintain a personal reading journal, and get book recommendations.

## Table of Contents

- [About The Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)

## About The Project

Book Tracker & Reading Journal is a comprehensive web application designed for book lovers to organize their reading journey. Users can search from over 40 million books using the Google Books API, track their reading progress, and maintain detailed reading journals.

**Key Highlights:**
* Integrated with Google Books API for book discovery
* JWT-based authentication for secure user access
* Responsive design for seamless use across all devices
* RESTful API architecture with Falcon framework

## Features

* **Book Search:** Search and add books from Google Books API's extensive catalog
* **Reading Progress Tracking:** Track current reads, mark books as finished, and monitor reading progress
* **Personal Library:** Maintain a curated collection of books you've read, are reading, or want to read
* **User Authentication:** Secure JWT-based login and registration system
* **Book Recommendations:** Get personalized book suggestions based on a simple questionnaire

## Tech Stack

### Backend
* **Framework:** Python with Falcon
* **Database:** PostgreSQL
* **Authentication:** JWT (JSON Web Tokens)
* **API Integration:** Google Books API

### Frontend
* **Framework:** React 
* **Styling:** Tailwind CSS
* **State Management:** React Hooks
* **HTTP Client:** Axios/Fetch API

## Installation

### Prerequisites
* Python 3.8+
* Node.js 16+
* PostgreSQL
* npm

### Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/book-tracker.git
```
2. Split your terminal into two windows/tabs:
   - One for the backend
   - One for the frontend
3. Backend setup
```bash
cd backend
python app.py
```
4. Frontend setup
```bash
cd frontend
npm run dev
```
