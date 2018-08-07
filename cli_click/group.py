import click


@click.group()
def cli():
    pass


@click.command()
def init_db():
    click.echo('Initialized the database')


@click.command()
def drop_db():
    click.echo('Dropped the database')


cli.add_command(init_db)
cli.add_command(drop_db)
