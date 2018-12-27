***All work: chitai-gorod.ipynb***  


# Домашнее задание №4

В этом задании требуется обкачать книжный магазин [Читай.Город](https://www.chitai-gorod.ru/) с использованием библиотек [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) и [Selenium](https://selenium-python.readthedocs.io/). Ваша программа должна скачать информацию обо всех книгах в магазине следующих авторов:
 - Макс Фрай;
 - Эрин Хантер;
 - Дмитрий Емец.

Результатом работы вашей программы должен быть файл `hw_4.csv` с таблицей из всех найденных книг.

## Общий подход к решению задачи

Задачу условно можно разделить на два этапа. На первом этапе требуется получить все ссылки на книги автора, на втором — получить информацию о каждой из книг.

### Этап 1. Получение ссылок на книги автора

Для поиска всех книг автора мы будем пользоваться поисковой строкой сайта. Обратите внимание на формат URL-ов запросов:
```
https://www.chitai-gorod.ru/search/result.php?q={author}&type=author
```
где вместо `{author}` подставляется имя автора.

Рекомендуемые варианты значения для `{author}`: `Фрай М.`, `Хантер Э.`, `Емец Д.`.

**Замечание:** URL [не позволяет](https://ru.wikipedia.org/wiki/URL#%D0%9A%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_URL) использовать кириллические символы, поэтому для кодирования части URL-а, содержащей кириллицу, стоит воспользоваться функцией `urllib.parse.quote` с использованием, в данном случае, кодировки `windows-1251`.

Попробуйте пролистать [страничку](https://www.chitai-gorod.ru/search/result.php?q=%D4%F0%E0%E9%20%CC.&type=author) вниз, и вы увидите, что новые книги подгружаются динамически. В некоторый момент появляется кнопка _"Показать ещё"_, нажав на которую можно дополнительно подгрузить выдачу.

Чтобы получить все ссылки на карточки с книгами, нужно подгрузить полную выдачу по запросу. Один из возможных критериев полной  выдачи: число карточек с книгами на странице равно заявленному на сайте числу найденных товаров (например, _"Найдено 153 товара"_). 

Существует несколько способов получить ссылку на карточку:
1. получить атрибут `data-product` одного из тегов с классом `product-card` и использовать знание о формате URL-ов страничек с книгами;
2. непосредственно найти ссылку.

### Этап 2. Получение информации о книгах

Рассмотрим в качестве примера [карточку](https://www.chitai-gorod.ru/catalog/book/1059170/) книги Макса Фрая "Мертвый ноль".

![скриншот](/images/1059170.png)

На скриншоте выделены 4 области, из каждой области требуется извлечь следующие элементы:
1. поле "ID карточки";
2. поля "Название", "Автор", "Рейтинг", "Голоса";
3. поле "Цена";
4. вся таблица.

Дополнительно требуется создать поле "Обложка", которое будет хранить ссылку на обложку книги (расположена слева на скриншоте).

Таким образом карточка из примера представима в виде следующего словаря:
```json
{
    "ID карточки": 1059170,
    "Название": "Мертвый ноль",
    "Автор": "Фрай М.",
    "Рейтинг": 4.0,
    "Голоса": 16,
    "Цена": 375,
    "Серия": "Сновидения Ехо",
    "Издательство": "АСТ",
    "Год издания": 2018,
    "Кол-во страниц": 448,
    "ISBN": "9785171089733",
    "Тираж": 30000,
    "Формат": "20.5 x 13 x 2.5",
    "Тип обложки": "Твердая бумажная",
    "Возраст": "16+",
    "ID товара": 2659485,
    "Обложка": "https://img-gorod.ru/upload/iblock/aec/aec2cfaece8a6190f319f1853cad7cf5.jpg"
}
```
Обратите внимание, что некоторые поля, например: "Художник", "Переводчик", "Редактор" — отсутвуют именно для этой карточки, но могут присутсвовать в других карточках, см. таблицы, например, [карточки #1](https://www.chitai-gorod.ru/catalog/book/1002042/) и [карточки #2](https://www.chitai-gorod.ru/catalog/book/1004240/).

Предположим, что у нас есть функция `extract_book_info(card_id)`, которая для карточки с номером `card_id` возвращает описанный выше словарь. Тогда требуемую таблицу можно получить следующим образом:
```python
import pandas as pd

result = list(map(extract_book_info, card_ids))

df = pd.DataFrame(result)
df.sort_values(by='ID карточки', inplace=True)

with open('data/hw_4.csv', mode='w', encoding='utf-8') as f_csv:
    df.to_csv(f_csv, index=False)
```

Пример результата работы программы можно найти [здесь](hw_4_sample.csv).