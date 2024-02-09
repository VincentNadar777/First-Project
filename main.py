import click
import requests

API_URL = "https://openlibrary.org/search.json"

@click.command()
@click.option("--title", prompt="Enter the title of the book", help="Title of the book to search")
def search_books(title):
    """Search for books on Open Library"""
    try:
        params = {"title": title}
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise an exception if the response status code indicates an error
        data = response.json()
        
        # Process the response and display the results
        click.echo("Search Results:")
        for doc in data.get("docs", []):
            click.echo(f"- {doc.get('title')} by {', '.join(doc.get('author_name', []))}")
        click.echo(f"Total results found: {data.get('numFound', 0)}")

    except requests.exceptions.RequestException as e:
        click.echo("An error occurred while making the API request:", err=True)
        click.echo(str(e), err=True)
        # Handle the exception as needed, e.g., display an error message or perform alternative actions.

if __name__ == "__main__":
    search_books()
