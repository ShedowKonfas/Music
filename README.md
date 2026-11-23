# Music

Небольшой консольный поиск треков SoundCloud: запрашивает название, выводит первые 5 результатов — исполнителя, заголовок и ссылку.

## Быстрый старт

```bat
python -m venv venv
venv\Scripts\pip install -r requirements.txt
start.cmd
```

Или напрямую: `venv\Scripts\python main.py`. `start.cmd` рассчитан на `venv\Scripts\python.exe` и жмёт `pause` в конце.

## Пример

```text
Название трека для поиска: interstellar
1. Artist — Track
   Ссылка: https://soundcloud.com/...
```

## Настройки

- Зависимость одна: `soundcloud-v2` (клиент сам получает `client_id` с сайта SoundCloud, поэтому API-ключи не нужны).
- `.env` в репозитории пустой и кодом не читается; интернет для поиска обязателен.
- Если поиск не удался, ошибка печатается в консоль (`Произошла ошибка: ...`).

## Структура

| Файл | Роль |
|---|---|
| `main.py` | функция `search_music()` и точка входа с `input()` |
| `requirements.txt` | `soundcloud-v2` |
| `start.cmd` | запуск через venv |
| `.env` | пустая заготовка |

## Тесты

Автотестов нет; проверка — ручной поиск по известному запросу.
