import csv



items_sold = {}
items_key_value = {}

SALES = ['JOE', 'KAREN', 'MIA', 'PEGY', 'LESTER', 'FANCY', 'EDWARD', 'WENSON']

country_balance_counter = {} # global sold per country
tool_balance_sold = {} # total sold per tool

sales_balance_counter = {} # total sold per person
sales_item_counter = {}
sales_country_counter = {} #

delimeter='@'
output_delimiter=","
# 商品编码@    商品名称@    数量@    国家@    金额@   谁

with open('simple_4.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=delimeter)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are {", ".join(row)}')
            line_count += 1
        else:
            if row[0] in items_key_value:
                pass
            else:
                items_key_value[row[0]] = row[1]
            if row[0] in items_sold:
                items_sold[row[0]] += int(row[2])
            else:
                items_sold[row[0]] = int(row[2])

            if row[3] in country_balance_counter:
                country_balance_counter[row[3]] += float(row[4].replace(',','.'))
            else:
                country_balance_counter[row[3]] = float(row[4].replace(',','.'))

            if row[0] in tool_balance_sold:
                tool_balance_sold[row[0]] += float(row[4].replace(',','.'))
            else:
                tool_balance_sold[row[0]] = float(row[4].replace(',','.'))

            if row[5] in sales_balance_counter:
                sales_balance_counter[row[5]] += float(row[4].replace(',','.'))
            else:
                sales_balance_counter[row[5]] = float(row[4].replace(',','.'))


            if row[5] in sales_item_counter:
                if row[1] in sales_item_counter:
                    sales_item_counter[row[5]][row[1]] += int(row[2].replace(',','.'))
                else:
                    sales_item_counter[row[5]][row[1]] = int(row[2].replace(',','.'))

            else:
                sales_item_counter[row[5]] = {}
                if row[1] in sales_item_counter:
                    sales_item_counter[row[5]][row[1]] += int(row[2].replace(',','.'))
                else:
                    sales_item_counter[row[5]][row[1]] = int(row[2].replace(',','.'))
                pass

            # row[3] # country
            # row[4] # sum
            # row[5] # who

            line_count += 1
    print('Processed {line_count} lines.')

# Simple Item Counter
with open('SoldPerItem.csv', mode='w') as item_sale_file:
    employee_writer = csv.writer(item_sale_file, delimiter=output_delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['ID', 'Name', 'Items Sold'])

    for item in items_sold:
        # print(items_key_value[item], items_sold[item])
        employee_writer.writerow([item, items_key_value[item], items_sold[item]])

# Items Sold per Country
with open('SoldPerCountry.csv', mode='w') as item_sale_file:
    employee_writer = csv.writer(item_sale_file, delimiter=output_delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['Country', 'Balance Sold'])

    for item in country_balance_counter:
        employee_writer.writerow([item, int(country_balance_counter[item])])

# Tool Balance Sold
with open('ToolBalanceSold.csv', mode='w') as item_sale_file:
    employee_writer = csv.writer(item_sale_file, delimiter=output_delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['Tool', 'Balance Sold'])
    for item in tool_balance_sold:
        employee_writer.writerow([items_key_value[item],  int(tool_balance_sold[item])])

# Sold Per Person
with open('SoldPerPerson.csv', mode='w') as item_sale_file:
   employee_writer = csv.writer(item_sale_file, delimiter=output_delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
   employee_writer.writerow(['Who', 'Balance Sold'])
   for item in sales_balance_counter:
       employee_writer.writerow([item, int(sales_balance_counter[item])])


# country share by member
with open('ToolItemSold.csv', mode='w') as item_sale_file:
   employee_writer = csv.writer(item_sale_file, delimiter=output_delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
   employee_writer.writerow(['Who', 'Item', 'Units' ])
   for sales in sales_item_counter:
       for item in sales_item_counter[sales]:
        employee_writer.writerow([sales, item, sales_item_counter[sales][item]])
