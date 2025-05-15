from sqlalchemy.orm import Session
from sqlalchemy import text
from database.base import engine, Base
from database.models import Categories, Products


def init_db():
    with engine.connect() as conn:
        conn.execute(text('CREATE SCHEMA IF NOT EXISTS public'))
        conn.commit()
    print('='*40)
    print('Создание базы данных')
    Base.metadata.create_all(engine)

    categories = ('Молочные продукты', 'Фрукты и овощи', 'Хлебобулочные изделия')
    products = (
    ('Молочные продукты', 'Молоко', 2.25, 'Савушкин', 'media/milk_products/milk_savushkin.jpg'),
    ('Молочные продукты', 'Сыр', 5.40, 'Брест-Литовский', 'media/milk_products/Brest-Litovsk.jpg'),
    ('Молочные продукты', 'Кефир', 2.15, 'Мозырский', 'media/milk_products/kefir-Mozyrsky.jpg'),
    ('Фрукты и овощи', 'Апельсин', 6.85, 'Гавайский', 'media/fruits_and_vegetables/apelsin.jpg'),
    ('Фрукты и овощи', 'Помидор', 9.60, 'Минский', 'media/fruits_and_vegetables/pomidor.jpg'),
    ('Фрукты и овощи', 'Банан', 6.40, 'Африканский', 'media/fruits_and_vegetables/banana.jpg'),
    ('Хлебобулочные изделия', 'Хлеб', 2.55, 'Калинковичский', 'media/bakery_products/bread.jpg'),
    ('Хлебобулочные изделия', 'Батон', 2.98, 'Нежный', 'media/bakery_products/loaf.jpg'),
    ('Хлебобулочные изделия', 'Пряник', 3.15, 'Шоколадный', 'media/bakery_products/gingerbread.jpg'),
    )

    with Session(engine) as session:
        category_map = {}
        for name in categories:
            category = session.query(Categories).filter_by(category_name=name).first()
            if not category:
                category = Categories(category_name=name)
                session.add(category)
                session.flush()
            category_map[name] = category.id
        for category_name, name, price, desc, image in products:
            category_id = category_map.get(category_name)
            if category_id:
                # Проверяем, существует ли продукт
                product = session.query(Products).filter_by(product_name=name).first()
                if not product:
                    product = Products(
                        category_id=category_id,
                        product_name=name,
                        price=price,
                        description=desc,
                        image=image)
                    session.add(product)
        session.commit()
        print('База данных создана')

if __name__ == "__main__":
    init_db()



