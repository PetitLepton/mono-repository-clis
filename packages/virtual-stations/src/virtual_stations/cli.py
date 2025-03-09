import click

@click.command()
@click.option("--name", required=True)
def cli(name: str) -> None:
    print(f"Hello from virtual-stations, my dear {name}!")

if __name__ == "__main__":
    cli()
