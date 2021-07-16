line_counter=0
data_header=[]
data_list=[]

c = open("data_handling\customers.csv", "r", encoding="utf8")

while True:
    data = c.readline()
    if not data:
        break

    #first data is header
    if line_counter == 0:
        data_header = data.split()
    else:
        #all
        data_list.append(data.split(","))

        # #only customer from USA 
        # customer =data.split(",")
        # if customer[10].upper()=="USA":
        #     data_list.append(customer)
        
    line_counter += 1

c.close()

print("Header: \t", data_header)
for i in range(0,10):
    print("Data", i, ":\t", data_list[i])

print("Total: ", len(data_list))
