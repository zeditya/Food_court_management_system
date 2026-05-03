from mydb import start_db

def setup():
    db=start_db()
    menu=db["food_items"]
    menu.delete_many({})
    item1={"name":"Burger","price":100,"type":"Snacks"}
    item2={"name":"Pizza","price":200,"type":"Main"}
    item3={"name":"Coke","price":50,"type":"Drink"}
    item4={"name":"Samosa","price":20,"type":"Snacks"}
    item5={"name":"Fries","price":80,"type":"Snacks"}
    item6={"name":"Pasta","price":150,"type":"Main"}
    item7={"name":"Coffee","price":40,"type":"Drink"}
    item8={"name":"Sandwich","price":60,"type":"Snacks"}
    item9={"name":"Brownie","price":90,"type":"Dessert"}
    item10={"name":"Tea","price":15,"type":"Drink"}
    menu.insert_one(item1)
    menu.insert_one(item2)
    menu.insert_one(item3)
    menu.insert_one(item4)
    menu.insert_one(item5)
    menu.insert_one(item6)
    menu.insert_one(item7)
    menu.insert_one(item8)
    menu.insert_one(item9)
    menu.insert_one(item10)
    print("food added to database")

setup()