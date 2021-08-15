from dataclasses import dataclass, field
from json import dumps
from pickle import dumps as p_dumps
from yaml import dump
import requests
from bs4 import BeautifulSoup


@dataclass()
class Driver:
    position: int
    name: str
    country: str
    racing_team: str
    points: int

    def as_dict(self):
        return {'position': self.position, 'name': self.name, 'country': self.country,
                'racing_team': self.racing_team, 'points': self.points}

    def as_json(self):
        return dumps(self.as_dict())

    def as_yaml(self):
        return dump(self.as_dict())

    def as_pickle(self):
        return p_dumps(self.as_dict())

    def __gt__(self, other):
        return self.points > other.points

    def __ge__(self, other):
        return self.points >= other.points

    def __lt__(self, other):
        return self.points < other.points

    def __le__(self, other):
        return self.points <= other.points

    def __str__(self):
        return f'{self.position}. {self.name.capitalize()} {self.country}, {self.racing_team} => {self.points}'


@dataclass()
class Team:
    position: int
    name: str
    points: int

    def as_dict(self):
        return {'position': self.position, 'name': self.name, 'points': self.points}

    def as_json(self):
        return dumps(self.as_dict())

    def as_yaml(self):
        return dump(self.as_dict())

    def as_pickle(self):
        return p_dumps(self.as_dict())

    def __gt__(self, other):
        return self.points > other.points

    def __ge__(self, other):
        return self.points >= other.points

    def __lt__(self, other):
        return self.points < other.points

    def __le__(self, other):
        return self.points <= other.points

    def __str__(self):
        return f'{self.position}. {self.name.capitalize()} => {self.points}'


@dataclass()
class LapTime:
    race: str
    driver: str
    racing_team: str
    time: str

    def as_dict(self):
        return {'race': self.race, 'driver': self.driver, 'racing_team': self.racing_team, 'time': self.time}

    def as_json(self):
        return dumps(self.as_dict())

    def as_yaml(self):
        return dump(self.as_dict())

    def as_pickle(self):
        return p_dumps(self.as_dict())

    def get_milliseconds(self):
        minutes, seconds, milliseconds = self.time.split('.')
        return int(milliseconds) + 1000 * int(seconds) + 60 * 1000 * int(minutes)

    def __gt__(self, other):
        return self.get_milliseconds() > other.get_milliseconds()

    def __ge__(self, other):
        return self.get_milliseconds() >= other.get_milliseconds()

    def __lt__(self, other):
        return self.get_milliseconds() < other.get_milliseconds()

    def __le__(self, other):
        return self.get_milliseconds() <= other.get_milliseconds()

    def __str__(self):
        return f'{self.driver.capitalize()}, {self.racing_team} => {self.race}, {self.time}'


class F1:
    def __init__(self):
        self._current_drivers = self._get_current()
        self._current_teams = self.get_teams(2021)
        self._current_laps = self.get_fastest_laps(2021)

    @staticmethod
    def _get_current():
        r = requests.get('https://www.formula1.com/en/results.html/2021/drivers.html')
        soup = BeautifulSoup(r.content, 'html.parser')
        ul = (soup.body.find('div', class_='site-wrapper').main.article.
              div.find('div', class_='ResultArchiveContainer').
              find('div', class_='resultsarchive-content').div.table.tbody.find_all('tr'))
        content = []
        for i in ul:
            fields = i.find_all('td')[1:-1]
            pos = fields[0].text
            name = ' '.join(fields[1].a.text.strip().replace('\n', ' ').split()[:-1])
            country = fields[2].text
            racing_team = fields[3].text.strip()
            points = fields[4].text
            content.append(Driver(pos, name, country, racing_team, points))
        return content

    @staticmethod
    def get_drivers_by_year(year):
        if year > 2021 or year < 1950:
            raise ValueError('You have to enter a correct value')
        r = requests.get(f'https://www.formula1.com/en/results.html/{year}/drivers.html')
        soup = BeautifulSoup(r.content, 'html.parser')
        lst = (soup.body.find('div', class_='site-wrapper').main.article.
               div.find('div', class_='ResultArchiveContainer').
               find('div', class_='resultsarchive-wrapper').
               find('div', class_='resultsarchive-content').div.table.tbody.find_all('tr'))
        content = []
        for i in lst:
            fields = i.find_all('td')[1:-1]
            pos = fields[0].text
            name = fields[1].a.text.strip().replace('\n', ' ')
            name = name[:-1]
            country = fields[2].text
            racing_team = fields[3].text.strip()
            points = fields[4].text
            content.append(Driver(pos, name, country, racing_team, points))
        return content

    @staticmethod
    def get_teams(year):
        if year > 2021 or year < 1958:
            raise ValueError('You have to enter a correct value')
        r = requests.get(f'https://www.formula1.com/en/results.html/{year}/team.html')
        soup = BeautifulSoup(r.content, 'html.parser')
        lst = (soup.body.find('div', class_='site-wrapper').main.article.
               div.find('div', class_='ResultArchiveContainer').
               find('div', class_='resultsarchive-wrapper').
               find('div', class_='resultsarchive-content').div.table.tbody.find_all('tr'))
        content = []
        for i in lst:
            fields = i.find_all('td')[1:-1]
            pos = fields[0].text
            team = fields[1].text.strip()
            points = fields[2].text
            content.append(Team(pos, team, points))
        return content

    @staticmethod
    def get_fastest_laps(year):
        if year > 2021 or year < 1950:
            raise ValueError('You have to enter a correct value')
        r = requests.get(f'https://www.formula1.com/en/results.html/{year}/fastest-laps.html')
        soup = BeautifulSoup(r.content, 'html.parser')
        lst = (soup.body.find('div', class_='site-wrapper').main.article.
               div.find('div', class_='ResultArchiveContainer').
               find('div', class_='resultsarchive-wrapper').
               find('div', class_='resultsarchive-content').div.table.tbody.find_all('tr'))
        content = []
        for i in lst:
            fields = i.find_all('td')[1:-1]
            race = fields[0].text
            name = ' '.join(fields[1].text.strip().replace('\n', ' ').split()[:-1])
            team = fields[2].text
            lap_time = fields[3].text.replace(':', '.')
            content.append(LapTime(race, name, team, lap_time))
        return content

    @property
    def fastest_laps(self):
        return self._current_laps

    @property
    def drivers_standings(self):
        return self._current_drivers

    @property
    def teams_standings(self):
        return self._current_teams

    def __iter__(self):
        for i in self.drivers_standings:
            yield i

    def __len__(self):
        return len(self.drivers_standings)


if __name__ == '__main__':
    f1 = F1()
    lap1 = f1.drivers_standings
    print(getattr(lap1[0], 'as_dict')())
