class MusicVideo:
    url = "https://youtube.com/"

    def __init__(self, author=None, title=None, duration=None, views=None, genre=None, year=None, country=None):
        self._author = author
        self._title = title
        self._duration = duration
        self._views = views
        self._genre = genre
        self._year = year
        self._country = country

    def __str__(self):
        title = "Title: {0}\n".format(self.title)
        author = "Author: {0}\n".format(self.author)
        duration = "Duration: {0}\n".format(self.duration)
        views = "Views on YouTube: {0}\n".format(self.views)
        genre = "Genre: {0}\n".format(self.duration)
        year = "Year: {0}\n".format(self.year)
        country = "Country: {0}\n".format(self.country)
        url = "URL: {0}\n".format(MusicVideo.url)
        return title + author + duration + views + genre + year + country + url

    def __repr__(self):
        classname = str(self.__class__.__name__)
        main_arguments = [self.author, self.title, self.duration, self.views]
        add_arguments = [self.genre, self.year, self.country, MusicVideo.url]
        arguments = ', '.join(list(map(str, main_arguments + add_arguments)))
        return classname + '(%s)' % arguments

    def __del__(self):
        print("Deleted " + self.__class__.__name__ + " | ID: " + str(id(self)))
        return

    @staticmethod
    def get_url():
        return MusicVideo.url

    @staticmethod
    def main():
        full_data = MusicVideo('Hans Zimmer', 'A Way of Life', 8.04, 14967445, 'Instrumental', 2003, "USA")
        partial_data = MusicVideo("M83", "Wait", 5.56)
        no_data = MusicVideo()
        objects = [full_data, partial_data, no_data]
        [(print(repr(x)), print(x)) for x in objects]

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @property
    def views(self):
        return self._views

    @views.setter
    def views(self, views):
        self._views = views

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        self._genre = genre

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country
