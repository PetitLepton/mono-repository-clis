from forecasts.cli import main

def test_main() -> None:
    name = "Jane"
    assert name in main(name=name)
