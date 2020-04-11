class MusicVideo:
    url = "https://youtube.com/"

    def __init__(self, author=None, title=None, duration=None, views=None, genre=None, year=None, country=None):
        self.author = author
        self.title = title
        self.duration = duration
        self.views = views
        self.genre = genre
        self.year = year
        self.country = country

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
