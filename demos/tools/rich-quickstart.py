from rich import print
from rich import pretty
from rich.console import Console
from rich import inspect

if __name__ == '__main__':
    pretty.install()
    console = Console()
    print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())
    console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")
    my_list = ["foo", "bar"]
    inspect(my_list, methods=True)
