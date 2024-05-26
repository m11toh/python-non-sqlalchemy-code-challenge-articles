class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
       def __init__(self, name):
        self._name = name

        @property
        def name(self):
            return self._name

        def articles(self):
            return [article for article in Article.all_articles if article.author == self]

        def magazines(self):
            return list(set(article.magazine for article in self.articles()))

        def add_article(self, magazine, title):
            return Article(self, magazine, title)

        def topic_areas(self):
            articles = self.articles()
            if not articles:
                return None
            return list(set(article.magazine.category for article in articles))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass