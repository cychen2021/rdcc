import click

@click.group("rdcc")
def rdcc() -> None:
    pass

@rdcc.command("init")
@click.option("--manifest", "-i", type=click.Path(exists=True, readable=True, file_okay=True, dir_okay=False), required=True, help="Path to the dev container manifest file.")
@click.option("--output", "-o", type=click.Path(exists=False, writable=True, dir_okay=False), required=False, default="Dockerfile", help="Path to the output directory for the generated component info.")
def init(manifest: str, output: str) -> None:
    pass

def main():
    """Main entry point for the rdcc command line interface."""
    rdcc()
