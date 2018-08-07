import click


@click.command()
@click.option('--gender', type=click.Choice(['man', 'woman']))
def choose(gender):
    click.echo('gender: %s' % gender)


if __name__ == '__main__':
    choose()
