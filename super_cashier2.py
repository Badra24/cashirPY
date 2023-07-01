import sqlite3

item = []

def add_item(name,qty,price) : 
    item.append({"name":name, "price":price,"qty":qty})
    
def delet_items(name):
    global item
    item = [i for i in item if i["name"] != name]


def reset_trans():
    global item
    item = []

def check_orders():
    for i in item :
        if not i["name"] or not i["qty"] or not i["price"] :
            return " Terdapat kesalahan input"
    return "Pemesanan benar "


def check_outs():
    item_bought = {i["name"]: [i["qty"], i["price"]] for i in item}
    print("Item yg di beli adalah:" ,item_bought)

    total = sum(i["price"] * i["qty"] for i in item)
    if total > 500000 :
        discount = 0.07
    elif total > 300000:
        discount = 0.05
    elif total > 100000:
        discount = 0.03
    else :
        discount = 0
        
    total_after = total - (total * discount)
    insert_tabel(total_after ,discount)
    return total_after, discount
def insert_tabel(total_after,discount):
    try:
        conect = sqlite3.connect('trans.db')
        set= conect.cursor()
        
        set.execute("""
        CREATE TABLE IF NOT EXISTS transaksi (
            no_id INTEGER,
            nama_item TEXT,
            jumlah_item INTEGER,
            harga REAL,
            total_harga REAL,
            diskon REAL,
            harga_diskon REAL
        );
        """)
        
       
        for items in item:
            set.execute("INSERT INTO transaksi (no_id, nama_item, jumlah_item, harga, total_harga, diskon, harga_diskon) VALUES(?,?,?,?,?,?,?)",
                (1, items["name"], items["qty"], items["price"], items["price"] * items["qty"], discount, total_after))
        conect.commit()
        conect.close()
    except Exception as error:
        print(f'Error : {error}')

# eksekusi
add_item("Ayam Bakar",2,30000)
add_item("Nasi Goreng",1,30000)
print(item)

delet_items('Ayam Bakar')
print(item)
reset_trans()
print(item)
check_orders()
print(item)

add_item("Ayam nasi " , 4, 50000)
add_item("Nasi goreng",1,50000)
add_item("Nasi padang",2,50000)
add_item("Ayam goreng " , 4, 50000)
add_item("Nasi timbel",1,50000)
add_item("Nasi liwet",2,50000)
total,discount = check_outs()
print("total belanja adalah :" , total)