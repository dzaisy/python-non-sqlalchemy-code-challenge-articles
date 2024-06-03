class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError('Name must be a string')
        if len(name) == 0:
            raise ValueError('Name must be longer than 0 characters')
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))
    
    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError('Magazine must be an instance of Magazine')
        article = Article(self, magazine, title)
        return article
    
    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError('Name must be a string')
        if len(name) < 2 or len(name) > 16:
            raise ValueError('Name must be between 2 and 16 characters')
        if not isinstance(category, str):
            raise ValueError('Category must be a string')
        if not len(category) > 0:
            raise ValueError('Category must be longer than 0 characters')
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @property
    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))
    
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        authors = [author for author in self.contributors() if sum(1 for article in self._articles if article.author == author) > 2]
        if not authors:
            return None
        return authors


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError('Author must be an instance of Author')
        if not isinstance(magazine, Magazine):
            raise ValueError('Magazine must be an instance of Magazine')
        if not isinstance(title, str):
            raise ValueError('Title must be a string')
        if len(title) < 5 or len(title) > 50:
            raise ValueError('Title must be between 5 and 50 characters')
        self.author = author
        self.magazine = magazine
        self.title = title
        author.articles.append(self)
        magazine.articles.append(self)