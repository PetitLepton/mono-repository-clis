import typer

cli = typer.Typer()

@cli.command()
def main(name: str = typer.Option()) -> None:
    message = f"Hello from forecasts, my dear {name}!"
    print(message)
    return message


if __name__ == "__name__":
    cli()
