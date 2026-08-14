class_type = input("enter a class_type (Bussiness / Economy) :")
luggage_weight = int(input("enter a luggage_weight in kg :"))

if class_type == "Economy":
    if luggage_weight <= 20 :
        print("your luggage_weight is oaky, safar mubarak ho!!!")
    else:
        print("your luggage_weight is extra, you can pay extra charges")
elif class_type == "Bussiness":
    if luggage_weight <= 40:
        print("Ticket price 15000.vip logo kayliya access shamil ha")
    else:
        print("luggae_weight ziyada ha to extra charges ho gay")
else:
    print("Galat class type ki ha ")




    