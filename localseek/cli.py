import click
from .search import FileSearcher
from .highlight import Highlighter


@click.command()
@click.option('--pattern', '-p', help='Search pattern')
@click.option('--path', default='.', help='Search path (default: current directory)')
@click.option('--content', '-c', is_flag=True, help='Search file contents instead of names')
@click.option('--regex', '-r', is_flag=True, help='Use regex pattern for content search')
@click.option('--ext', '-e', multiple=True, help='Filter by file extensions (e.g. -e py -e js)')
@click.option('--no-highlight', is_flag=True, help='Disable syntax highlighting')
@click.version_option()
def main(pattern, path, content, regex, ext, no_highlight):
    """LocalSeek - Find files locally"""
    if not pattern:
        click.echo("LocalSeek v0.1.0")
        click.echo("Use --pattern to search")
        return

    searcher = FileSearcher(path)
    ext_filter = list(ext) if ext else None

    if content:
        results = searcher.search_content(pattern, use_regex=regex, file_ext_filter=ext_filter)
        if results:
            click.echo(f"Found {len(results)} matches:")
            for file_path, line_num, line in results:
                if not no_highlight:
                    highlighted_line = Highlighter.highlight_text(line, pattern, use_regex=regex)
                    click.echo(f"{file_path}:{line_num} {highlighted_line}")
                else:
                    click.echo(f"{file_path}:{line_num} {line}")
        else:
            click.echo("No content matches found.")
    else:
        results = searcher.search_by_name(pattern, file_ext_filter=ext_filter)
        if results:
            click.echo(f"Found {len(results)} files:")
            for result in results:
                click.echo(result)
        else:
            click.echo("No files found matching pattern.")


if __name__ == "__main__":
    main()