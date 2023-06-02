import click
import requests

API_URL = "https://openlibrary.org/search.json"


@click.command()
@click.option("--title", prompt="Enter the title of the book", 
              help="Title of the book to search")
def search_books(title):
    """Search for books on Open Library"""
    params = {"title": title}
    response = requests.get(API_URL, params=params)
    data = response.json()
    
    # Process the response and display the results
    click.echo("Search Results:")
    for doc in data.get("docs", []):
        click.echo(f"- {doc.get('title')} by {', '.join(doc.get('author_name', []))}")
    click.echo(f"Total results found: {data.get('numFound', 0)}")


if __name__ == "__main__":
    search_books()
