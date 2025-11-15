class Book:
    def __init__(self, name: str='Неизвестно', author: str='Неизвестно', pages_number: int=0) -> None:
        try:
            if name == 'Неизвестно' or author == 'Неизвестно' or pages_number == 0:

                raise ValueError("Все параметры должны быть указаны: name, author, pages_number")

            self.__name = name
            self.__author = author
            self.__pages_number = 0
            self.set_pages_number(pages_number)

        except ValueError as e:
            print(f"Ошибка создания книги: {e}")

            raise


    def get_name(self) -> str:

        return self.__name


    def get_author(self) -> str:

        return self.__author


    def get_pages_number(self) -> int:

        return self.__pages_number


    def set_author(self, author) -> None:
        if author and author.strip():
            self.__author = author
        else:
            print('Автор не может быть пустым')


    def set_name(self, name) -> None:
        if name and name.strip():
            self.__name = name
        else:
            print('Название не может быть пустым')


    def set_pages_number(self, pages_number) -> None:
        if pages_number > 0:
            self.__pages_number = pages_number
        else:
            print('Количество страниц должно быть больше 0')
            self.__pages_number = 0


    def info(self) -> None:
        print('Информация о книге:')
        print(f'Название: {self.__name}')
        print(f'Автор: {self.__author}')
        print(f'Количество страниц: {self.__pages_number}')


    def get_page_info(self, page_number: int) -> str:

        return f'{page_number}-ья страница.' if page_number % 10 == 3 and page_number != 13 \
        else f'{page_number}-ая страница.'


    def time_to_read(self, speed: int=20) -> str:
        hours = self.__pages_number / speed

        return f'Чтобы прочитать книгу, вам понадобится {hours:.1f} ч'


    def thick_book(self) -> str:

        return 'Книга большая' if self.__pages_number > 200 else 'Книга небольшая'


class Main:
    def test_empty_book() -> None:
        """Тест создания книги с ошибкой"""

        try:
            book = Book()

            print(book.time_to_read())

            print()

            book.info()

            print()

            print('========= проверка ошибки количества страниц =========')
            print()
            book.set_pages_number(-100)

        except ValueError:
            print("Программа остановлена из-за ошибки создания книги")


    def test_book_operations() -> None:
        """Тест операций с книгой"""

        book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 480)

        print(f"get_name(): {book2.get_name()}")
        print(f"get_author(): {book2.get_author()}")
        print(f"get_pages_number(): {book2.get_pages_number()}")

        print()

        print(f"Медленная скорость (10 стр/ч): {book2.time_to_read(10)}")
        print(f"Быстрая скорость (30 стр/ч): {book2.time_to_read(30)}")
        print(f"Очень быстрая (50 стр/ч): {book2.time_to_read(50)}")

        print()

        print(book2.thick_book(), '- проверка метода thick_book()')

        print()

        book2.set_name("Белая гвардия")
        book2.set_author("М.А. Булгаков")
        book2.set_pages_number(320)

        print('========== проверка после внесения изменений ==========')
        print(f"Финальное название: {book2.get_name()}")
        print(f"Финальный автор: {book2.get_author()}")
        print(f"Финальное количество страниц: {book2.get_pages_number()}")


    def run() -> None:
        """Основной метод запуска тестов"""

        # Запуск первого теста (с ошибкой)
        Main.test_empty_book()
        # Запуск второго теста (операции с книгой)
        Main.test_book_operations()

        print("\n" + "=" * 50)
        print("ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ")


class BookManager:
    def __init__(self) -> None:
        self.current_book = None


    def menu(self) -> None:
        flag = True
        while flag:
            print("=== МЕНЮ КНИГ ===")
            print("1. Создать книгу")
            print("2. Информация о книге")
            print("3. Изменить книгу")
            print("4. Время чтения")
            print("0. Выход")

            choice = input("Выберите (введите цифру от 0 до 4 (включительно)): ")

            if choice == '1':
                self.create_book()
            elif choice == '2':
                self.show_book_info()
            elif choice == '3':
                self.modify_book()
            elif choice == '4':
                self.calculate_time()
            elif choice == '0':
                print("Выход из программы")
                flag = False
            else:
                print("Неверный выбор!")


    def create_book(self) -> None:
        name = input("Название: ")
        author = input("Автор: ")
        pages_number = int(input("Количество страниц(целое число): "))
        self.current_book = Book(name, author, pages_number)

        print("Книга создана!")


    def show_book_info(self) -> None:
        if self.current_book:
            self.current_book.info()
        else:
            print("Сначала создайте книгу!")


    def modify_book(self) -> None:
        if self.current_book:
            new_name = input("Введите новое название: ")
            new_author = input("Введите новый автор: ")
            new_pages_number = int(input("Введите новое количество страниц: "))
            self.current_book.set_name(new_name)
            self.current_book.set_author(new_author)
            self.current_book.set_pages_number(new_pages_number)
            print("Книга изменена!")
        else:
            print("Сначала создайте книгу!")


    def calculate_time(self) -> None:
        if self.current_book:
            user_input = input("Введите скорость (по умолчанию 20): ")
            if not user_input.strip():  # Если пользователь ничего не ввел
                new_speed = 20
            else:
                new_speed = int(user_input)

            time_to_read = self.current_book.time_to_read(new_speed)

            print(time_to_read)

        else:
            print("Сначала создайте книгу!")


if __name__ == "__main__":
    # Сначала демонстрация тестов
    Main.run()
    # Потом запуск меню
    manager = BookManager()
    manager.menu()