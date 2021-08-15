import click
from f1.f1 import F1

f1 = F1()


@click.group()
def main():
    ...


@main.command()
@click.argument('year', type=int)
@click.option('--type_format', '-f', type=str)
def driver_by_year(year, type_format):
    """Get drivers by provided year"""
    if type_format is not None and type_format in ['yaml', 'json', 'pickle', 'dict']:
        for i in f1.get_drivers_by_year(year):
            print(getattr(i, f'as_{type_format}')())
    else:
        for i in f1.get_drivers_by_year(year):
            print(i)


@main.command()
@click.argument('year', type=int)
@click.option('--type_format', '-f', type=str)
def fastest_laps(year, type_format):
    """Get fastest laps by provided year"""
    if type_format is not None and type_format in ['yaml', 'json', 'pickle', 'dict']:
        for i in f1.get_fastest_laps(year):
            print(getattr(i, f'as_{type_format}')())
    else:
        for i in f1.get_fastest_laps(year):
            print(i)


@main.command()
@click.argument('year', type=int)
@click.option('--type_format', '-f', type=str)
def teams_by_year(year, type_format):
    """Get teams by provided year"""
    if type_format is not None and type_format in ['yaml', 'json', 'pickle', 'dict']:
        for i in f1.get_teams(year):
            print(getattr(i, f'as_{type_format}')())
    else:
        for i in f1.get_teams(year):
            print(i)


@main.command()
@click.option('--type_format', '-f', type=str)
def current_fastest(type_format):
    """Get fastest laps in current season"""
    if type_format is not None and type_format in ['yaml', 'json', 'pickle', 'dict']:
        for i in f1.fastest_laps:
            print(getattr(i, f'as_{type_format}')())
    else:
        for i in f1.fastest_laps:
            print(i)


@main.command()
@click.option('--type_format', '-f', type=str)
def driver_standings(type_format):
    """Get driver standings in current season"""
    if type_format is not None and type_format in ['yaml', 'json', 'pickle', 'dict']:
        for i in f1.drivers_standings:
            print(getattr(i, f'as_{type_format}')())
    else:
        for i in f1.drivers_standings:
            print(i)


@main.command()
@click.option('--type_format', '-f', type=str)
def team_standings(type_format):
    """Get team standings in current season"""
    if type_format is not None and type_format in ['yaml', 'json', 'pickle', 'dict']:
        for i in f1.teams_standings:
            print(getattr(i, f'as_{type_format}')())
    else:
        for i in f1.teams_standings:
            print(i)


if __name__ == '__main__':
    main()
