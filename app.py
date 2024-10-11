#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for projects (could be stored in a database)
projects = [
    {
        'title': 'API for E-commerce',
        'description': 'A REST API for managing products and orders using Flask and SQLite.',
        'technologies': 'Flask, SQLite, JWT, Docker',
        'github_url': 'https://github.com/yourusername/ecommerce-api'
    },
    {
        'title': 'Task Manager',
        'description': 'A web-based task management tool using Flask, PostgreSQL, and Redis.',
        'technologies': 'Flask, PostgreSQL, Redis, Docker',
        'github_url': 'https://github.com/yourusername/task-manager'
    },
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def project_list():
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission (for now, just redirect to homepage)
        return redirect(url_for('home'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
