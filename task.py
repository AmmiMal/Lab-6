class Book:
    className = 'Book'

    def __init__(self, title, number_pages, time_for_one, number_images):
        self.title = title
        self.number_pages = number_pages
        self.time_for_one = time_for_one
        self.number_images = number_images

    def reading_time(self):
        total_time = self.time_for_one * self.number_pages
        return total_time

    def number_articles_per_page(self):
        return 0

    def __add__(self, other):
        if isinstance(other, Book):
            return Book(
                title = f"{self.title} & {other.title}",
                number_pages = self.number_pages+other.number_pages,
                time_for_one = self.time_for_one+other.time_for_one,
                number_images = self.number_images+other.number_images
                        )




class Encyclopedia(Book):
    className = 'Encyclopedia'

    def __init__(self, title, number_pages, time_for_one, number_images, number_articles):
        super().__init__(title, number_pages, time_for_one, number_images)
        self.number_articles = number_articles

    def number_articles_per_page(self):
        if self.number_articles == 0:
            return 0
        return self.number_articles/self.number_pages


class PhoneDirectory(Book):
    className = 'PhoneDirectory'

    def __init__(self, title, number_pages, time_for_one, number_images, number_numbers):
        super().__init__(title, number_pages, time_for_one, number_images)
        self.number_numbers = number_numbers

    def number_phone_numbers_per_page(self):
        if self.number_numbers == 0:
            return 0
        return self.number_numbers / self.number_pages


if __name__ == '__main__':
    encyclopedia = Encyclopedia("Большая детская энциклопедия", 192, 2.5, 140, 50)
    phone_directory = PhoneDirectory("Телефонный справочник", 96, 1, 0, 7200)

    combining_books = encyclopedia + phone_directory

    print(f"Объединенная книга: {combining_books.title}")
    print(f"Количество страниц: {combining_books.number_pages}")
    print(f"Время чтения книги: {combining_books.reading_time()} минут")
    print(f"Количество картинок: {combining_books.number_images}")