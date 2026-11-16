from soundcloud import SoundCloud

def search_music(query):
    # Создаем клиент
    sc = SoundCloud()
    
    print(f"\nИщу трек: {query}...\n")
    
    try:
        # Ищем треки. Результат сохраняем в переменную search_result
        search_result = sc.search_tracks(query)
        
        # Достаем список треков из объекта
        tracks = search_result.collection
        
        # Проверяем, есть ли вообще результаты
        if not tracks:
            print("Ничего не найдено.")
            return
            
        # Выводим только первые 5 треков, чтобы не засорять консоль
        for i, track in enumerate(tracks[:5], start=1):
            print(f"{i}. {track.user.username} — {track.title}")
            print(f"   Ссылка: {track.permalink_url}\n")
            
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    user_query = input("Название трека для поиска: ")
    search_music(user_query)