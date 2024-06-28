import rich_click as click


@click.group()
def cli():
    """My CLI Application"""
    pass

@cli.command()
@click.option("-s", "--string-to-echo", type=str, required=True, help="String to repeat")
@click.option("-n", "--num", type=int, required=False, help="Number of times to repeat [2]", default=2)
def rep(string_to_echo:str, num:int):
    """Simple example of usage"""
    click.echo(f"{string_to_echo} "*num)

if __name__ == "__main__":
    cli()
