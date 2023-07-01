from super_cashier import Transaction

# Test 1
t = Transaction(1)
t.add_item('Ayam Goreng', 2, 20000)
t.add_item('Pasta Gigi', 3, 15000)
print(t.items)  # Anda seharusnya melihat daftar item di sini

# Test 2
t.delete_item('Pasta Gigi')
print(t.items)  # Anda seharusnya hanya melihat 'Ayam Goreng' di sini

# Test 3
t.reset_transaction()
print(t.items)  # Anda seharusnya melihat daftar item kosong di sini

# Test 4
t.add_item('Ayam Goreng', 2, 20000)
t.add_item('Pasta Gigi', 3, 15000)
total, disc = t.check_out()
print(total, disc)  # Anda seharusnya melihat total belanjaan setelah diskon dan persentase diskon
