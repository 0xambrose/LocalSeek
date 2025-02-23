import click
from .search import FileSearcher


@click.command()
@click.option('--pattern', '-p', help='Search pattern for file names')
@click.option('--path', default='.', help='Search path (default: current directory)')
@click.version_option()
def main(pattern, path):
    """LocalSeek - Find files locally"""
    if not pattern:
        click.echo("LocalSeek v0.1.0")
        click.echo("Use --pattern to search for files")
        return

    searcher = FileSearcher(path)
    results = searcher.search_by_name(pattern)

    if results:
        click.echo(f"Found {len(results)} files:")
        for result in results:
            click.echo(result)
    else:
        click.echo("No files found matching pattern.")


if __name__ == "__main__":
    main()