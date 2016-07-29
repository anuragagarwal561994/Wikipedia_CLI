import click
import wikipedia


@click.command()
@click.option('--query', '-q', prompt='Search',
              help='Wikipedia article to search')
def main(query):
    """Search wikipedia articles on your terminal"""
    print wikipedia.search(query)
