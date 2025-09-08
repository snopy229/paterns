from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self, message):
        pass

class News(Subject):
    def __init__(self):
        self._observer = []

    def attach(self, observer):
        self._observer.append(observer)

    def detach(self, observer):
        self._observer.remove(observer)

    def notify(self, message):
        for observer in self._observer:
            observer.update(message)

    def add_news(self, news):
        print("The news was published: {news}")
        self.notify(news)

class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(F"{self.name} got notification: {message}")

if __name__ == "__main__":
    news = News()
    user1 = User("John")
    user2 = User("Bob")

    news.attach(user1)
    news.attach(user2)

    news.add_news("News1")

    news.detach(user1)

    news.add_news("News2")

    