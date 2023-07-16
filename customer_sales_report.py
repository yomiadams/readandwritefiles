import csv

sales = open('sales.csv','r')
outfile = open('customer_sales_report.csv', 'w', newline='')

sales_files = csv.reader(sales, delimiter=',')  
outfile_writer = csv.writer(outfile, delimiter=',')

outfile_writer.writerow(['CustomerID', 'Total'])

next(sales_files)  

current_id = None
current_total = 0.0

for record in sales_files:
    customer_id = record[0]
    subtotal = float(record[3])
    tax = float(record[4])
    freight = float(record[5])

    if current_id is None:
        current_id = customer_id

    if customer_id != current_id:
        outfile_writer.writerow([current_id, "{:.2f}".format(current_total)])
        current_id = customer_id
        current_total = 0.0

    current_total += subtotal + tax + freight

outfile_writer.writerow([current_id, "{:.2f}".format(current_total)])

sales.close()
outfile.close()
