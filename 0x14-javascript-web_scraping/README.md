0x14-javascript-web_scraping
# JavaScript Web Scraping Project

This project is part of the ALX Software Engineering Foundations curriculum, focusing on JavaScript web scraping techniques. It consists of a set of JavaScript scripts designed to accomplish various tasks related to web scraping, API interaction, file handling, and more.

## Table of Contents

- [Requirements](#requirements)
- [Tasks](#tasks)
  - [Task 0: Readme](#task-0-readme)
  - [Task 1: Write me](#task-1-write-me)
  - [Task 2: Status code](#task-2-status-code)
  - [Task 3: Star Wars movie title](#task-3-star-wars-movie-title)
  - [Task 4: Star Wars Wedge Antilles](#task-4-star-wars-wedge-antilles)
  - [Task 5: Loripsum](#task-5-loripsum)
  - [Task 6: How many completed?](#task-6-how-many-completed)

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the project folder, is mandatory
- Your code should be semistandard compliant, following the rules of Standard JS with semicolons
- All files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`

## Tasks

### Task 0: Readme

Write a script that reads and prints the content of a file.

- The first argument is the file path
- The content of the file must be read in UTF-8
- If an error occurred during the reading, print the error object

### Task 1: Write me

Write a script that writes a string to a file.

- The first argument is the file path
- The second argument is the string to write
- The content of the file must be written in UTF-8
- If an error occurred during while writing, print the error object

### Task 2: Status code

Write a script that displays the status code of a GET request.

- The first argument is the URL to request (GET)
- The status code must be printed like this: `code: <status code>`
- You must use the `request` module

### Task 3: Star Wars movie title

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

- The first argument is the movie ID
- You must use the Star Wars API with the endpoint `https://swapi-api.alx-tools.com/api/films/:id`
- You must use the `request` module

### Task 4: Star Wars Wedge Antilles

Write a script that prints the number of movies where the character “Wedge Antilles” is present.

- The first argument is the API URL of the Star Wars API: `https://swapi-api.alx-tools.com/api/films/`
- Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
- You must use the `request` module

### Task 5: Loripsum

Write a script that gets the contents of a webpage and stores it in a file.

- The first argument is the URL to request
- The second argument is the file path to store the body response
- The file must be UTF-8 encoded
- You must use the `request` module

### Task 6: How many completed?

Write a script that computes the number of tasks completed by user id.

- The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`
- Only print users with completed tasks
- You must use the `request` module

**Copyright © 2024 ALX. All rights reserved.**
