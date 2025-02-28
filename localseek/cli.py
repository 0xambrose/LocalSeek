import click
from .search import FileSearcher


@click.command()
@click.option('--pattern', '-p', help='Search pattern')
@click.option('--path', default='.', help='Search path (default: current directory)')
@click.option('--content', '-c', is_flag=True, help='Search file contents instead of names')
@click.option('--regex', '-r', is_flag=True, help='Use regex pattern for content search')
@click.version_option()
def main(pattern, path, content, regex):
    """LocalSeek - Find files locally"""
    if not pattern:
        click.echo("LocalSeek v0.1.0")
        click.echo("Use --pattern to search")
        return

    searcher = FileSearcher(path)

    if content:
        results = searcher.search_content(pattern, use_regex=regex)
        if results:
            click.echo(f"Found {len(results)} matches:")
            for file_path, line_num, line in results:
                click.echo(f"{file_path}:{line_num} {line}")
        else:
            click.echo("No content matches found.")
    else:
        results = searcher.search_by_name(pattern)
        if results:
            click.echo(f"Found {len(results)} files:")
            for result in results:
                click.echo(result)
        else:
            click.echo("No files found matching pattern.")


if __name__ == "__main__":
    main()