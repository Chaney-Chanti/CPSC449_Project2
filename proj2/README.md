# CPSC 449 - Project 2: Micrblogging Service

## Group Members:

Chaney Chantipaporn

Nhat Nguyen

Tony Nguyen

## Project Requirements
This project will run using Tuffix 2020 using Python 3.8.10 and will be implemented using Hug, sqlite_tils, and Request libraries. 
An installation of ruby-foreman, httpie, sqlite3, sqlite-utils, hug, and gunicorn may be required. 

## Project Description

In this project we are creating two RESTful microservices. One for users, and one for timelines. Only authenticated users may create a post, and only authenticated users may view their home timeline.

## How to Run the Program

The following steps are required to prepare to run the project.
1. Install the pip package installer and other tools by running the following commands:
    sudo apt update
    sudo apt install --yes python3-pip ruby-foreman httpie sqlite3

2. Install the Hug and sqlite-utils libraries by running the following command:
    python3 -m pip install hug sqlite-utils

3. Log out then back in to pick up changes to your PATH before trying to run the hug or sqlite-utils commands.
Install the HAProxy and Gunicorn servers by running the following commands:
    sudo apt install --yes haproxy gunicorn

4. Once everything has installed, locate the project folder in the terminal. Use the cd command to the project folder.

5. Then run the command:
    python3 sqlite.py
    foreman start

6. The application will run on two different ports. The application can be tested using HTTPie.
