import csv

customers = open('customers.csv','r')
outfile = open('customer_country.csv', 'w', newline='')

customer_file = csv.reader(customers, delimiter=',')
outfile_writer = csv.writer(outfile, delimiter=',')

outfile_writer.writerow(['First Name', 'Last Name', 'Country'])

next(customer_file)

for record in customer_file:

    outfile_writer.writerow([record[1], record[2], record[4]])


customers.close()
outfile.close()








