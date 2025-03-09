import typer

cli = typer.Typer()

@cli.command()
def main(name: str = typer.Option()) -> None:
    print(f"Hello from forecasts, my dear {name}!")

if __name__ == "__name__":
    cli()