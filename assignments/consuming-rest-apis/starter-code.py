import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_post(post_id):
    """Fetch a post by ID and return its JSON data."""
    # TODO: Send a GET request with a timeout, check the response, and return its JSON.
    pass


def fetch_user_posts(user_id):
    """Fetch posts for a user and return the JSON list."""
    # TODO: Send a GET request with userId as a query parameter.
    pass


def main():
    try:
        post = fetch_post(1)
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")

        posts = fetch_user_posts(1)
        print("\nPosts by user 1:")
        for item in posts:
            print(f"- {item['title']}")
    except requests.RequestException as error:
        print(f"Could not retrieve data from the API: {error}")


if __name__ == "__main__":
    main()
