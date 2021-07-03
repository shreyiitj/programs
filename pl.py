import csv

filename = 'trades.csv'

rows = []

def get_float(num):
	return float(num) if num else None

with open(filename, 'r') as csvfile:
  csvreader = csv.reader(csvfile)
  cols = next(csvreader)
  for row in csvreader:
    rows.append(row)

total_buy_qty = 0
total_sell_qty = 0

total_buy_amount = 0
total_sell_amount = 0

for row in rows:
  buy_qty = get_float(row[0])
  buy_price = get_float(row[1])
  sell_qty = get_float(row[2])
  sell_price = get_float(row[3])
  
  if buy_qty:
    total_buy_qty += buy_qty
    total_buy_amount += buy_qty*buy_price
  if sell_qty:
    total_sell_qty += sell_qty
    total_sell_amount += sell_qty*sell_price

print(total_buy_qty)
print(total_buy_amount)
print(total_sell_qty)
print(total_sell_amount)

if total_buy_qty == 0 or total_sell_qty == 0:
  print('Qty is 0')
  sys.exit(0)

buy_avg = float(total_buy_amount/total_buy_qty)
sell_avg = float(total_sell_amount/total_sell_qty)

qty_to_consider = min(total_buy_qty, total_sell_qty)

realised_pl = qty_to_consider*(sell_avg - buy_avg)
print(f"Net p&l {realised_pl}")

if total_buy_qty > total_sell_qty:
  print(f"Standing Net Buy: {total_buy_qty - total_sell_qty} , Avg Buy rate {buy_avg}")
elif total_buy_qty < total_sell_qty:
  print(f"Standing Net Sell: {total_sell_qty - total_buy_qty} , Avg Sell rate {sell_avg}")
else:
  print("No Standing")