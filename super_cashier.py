from sqlalchemy import create_engine, Table, MetaData, Integer, String, Float, Column
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cashier_data.db')
metadata = MetaData()

transaksi = Table('transaksi', metadata, 
                  Column('no_id', Integer), 
                  Column('nama_item', String), 
                  Column('jumlah_item', Integer),
                  Column('harga', Float),
                  Column('total_harga', Float),
                  Column('diskon', Float),
                  Column('harga_diskon', Float),
                  extend_existing=True)

metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

items = []

def add_item(name, qty, price):
    items.append({"name": name, "qty": qty, "price": price, "total": qty * price})

def delete_item(name):
    global items
    items = [item for item in items if item["name"] != name]

def reset_transaction():
    global items
    items = []

def check_order():
    for item in items:
        if not item["name"] or not item["qty"] or not item["price"]:
            return "Terdapat kesalahan input data"
    return "Pemesanan sudah benar"

def check_out():
    items_bought = {item["name"]: [item["qty"], item["price"]] for item in items}
    print("Item yang dibeli adalah: ", items_bought)
    
    total = sum(item["total"] for item in items)
    if total > 500000:
        disc = 0.07
    elif total > 300000:
        disc = 0.06
    elif total > 200000:
        disc = 0.05
    else:
        disc = 0
    total_after_disc = total - (total * disc)

    insert_to_table(total_after_disc, disc)
    return total_after_disc, disc

def insert_to_table(total_after_disc, disc):
    try:
        for item in items:
            ins = transaksi.insert().values(no_id=1, 
                                            nama_item=item["name"], 
                                            jumlah_item=item["qty"], 
                                            harga=item["price"], 
                                            total_harga=item["total"], 
                                            diskon=disc, 
                                            harga_diskon=total_after_disc)
            session.execute(ins)
        session.commit()
    except Exception as e:
        print(f'Error: {e}')

# Test Cases
add_item('Ayam Goreng', 2, 20000)
add_item('Pasta Gigi', 3, 15000)
print(items) 

delete_item('Pasta Gigi')
print(items) 

reset_transaction()
print(items)

add_item('Ayam Goreng', 2, 20000)
add_item('Pasta Gigi', 3, 15000)
add_item('Mainan Mobil', 1, 200000)
add_item('Mie Instan', 5, 3000)
total, disc = check_out()
print("Total belanja yang harus dibayarkan adalah: ", total)
