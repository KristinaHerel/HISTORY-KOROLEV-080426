#!/usr/bin/env python3
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import engine
from sqlalchemy import text, inspect

def check_database():
    print("🔍 Проверка подключения и таблиц...")
    
    try:
        with engine.connect() as conn:
            # Проверка версии PostgreSQL
            result = conn.execute(text("SELECT version()"))
            version = result.fetchone()
            print(f"✅ Подключено к: {version[0].split(',')[0]}")
            
            # Получение списка всех таблиц
            inspector = inspect(engine)
            tables = inspector.get_table_names()
            
            if tables:
                print(f"\n📊 Существующие таблицы ({len(tables)}):")
                for table in sorted(tables):
                    # Получаем количество строк в таблице
                    try:
                        count_result = conn.execute(text(f"SELECT COUNT(*) FROM {table}"))
                        count = count_result.fetchone()[0]
                        print(f"  - {table}: {count} записей")
                    except:
                        print(f"  - {table}")
            else:
                print("\n⚠️ Таблицы не найдены. Запустите init_db.py для создания таблиц.")
                
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False
    
    return True

if __name__ == "__main__":
    check_database()