#!/usr/bin/env python3
import sys
import os

# Добавляем текущую директорию в путь Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import engine, Base
from app import models  # Это импортирует все ваши модели

def init_database():
    print("🔄 Подключение к Supabase...")
    try:
        # Проверка подключения
        with engine.connect() as conn:
            print("✅ Подключение успешно установлено!")
        
        # Создание всех таблиц
        print("📊 Создание таблиц в Supabase...")
        Base.metadata.create_all(bind=engine)
        print("✅ Все таблицы успешно созданы!")
        
        # Вывод списка созданных таблиц
        print("\n📋 Созданные таблицы:")
        for table_name in Base.metadata.tables.keys():
            print(f"  - {table_name}")
            
        print(f"\n📈 Всего создано таблиц: {len(Base.metadata.tables)}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        print("\nПроверьте:")
        print("1. Правильность DATABASE_URL в .env")
        print("2. Интернет соединение")
        print("3. Доступность Supabase")
        return False
    
    return True

if __name__ == "__main__":
    success = init_database()
    sys.exit(0 if success else 1)