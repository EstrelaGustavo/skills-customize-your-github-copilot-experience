# 📘 Assignment: Consuming REST APIs with Python

## 🎯 Objective

Write a Python client that retrieves and processes data from a public REST API. Practice sending HTTP requests, reading JSON responses, and handling request errors.

## 📝 Tasks

### 🛠️ Fetch a Single Resource

#### Description
Use the JSONPlaceholder API to retrieve one post and display selected fields from its JSON response.

#### Requirements
Completed program should:

- Install and import the `requests` package.
- Send a `GET` request to `https://jsonplaceholder.typicode.com/posts/1`.
- Parse the response as JSON and display the post's title and body.


### 🛠️ Request a Filtered Collection

#### Description
Retrieve posts for one user by passing a query parameter to the API, then display the titles returned.

#### Requirements
Completed program should:

- Send a `GET` request to `https://jsonplaceholder.typicode.com/posts` with the `userId` query parameter set to `1`.
- Parse the response as a JSON list.
- Display the title of each returned post.


### 🛠️ Handle Request Errors

#### Description
Make the client more reliable by detecting unsuccessful HTTP responses and handling connection or timeout errors.

#### Requirements
Completed program should:

- Set a timeout on each request.
- Call `raise_for_status()` so unsuccessful HTTP responses are treated as errors.
- Catch `requests.RequestException` and display a clear error message instead of crashing.
