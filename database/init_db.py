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
    ('Молочные продукты', 'Молоко', 2, 'Савушкин', 'media/milk_products/milk_savushkin.jpg'),
    ('Молочные продукты', 'Сыр', 5, 'Брест-Литовский', 'media/milk_products/Brest-Litovsk.jpg'),
    ('Молочные продукты', 'Кефир', 2, 'Мозырский', 'media/milk_products/kefir-Mozyrsky.jpg'),
    )

    with Session(engine) as session:
        category_map = {}
        for name in categories:
            category = Categories(category_name=name)
            session.add(category)
            session.flush()
            category_map[name] = category.id
        for category_name, name, price, desc, image in products:
            category_id = category_map.get(category_name)
            if category_id:
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



