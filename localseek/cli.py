import click


@click.command()
@click.version_option()
def main():
    """LocalSeek - Find files locally"""
    click.echo("LocalSeek v0.1.0")
    click.echo("File search utility - coming soon!")


if __name__ == "__main__":
    main()