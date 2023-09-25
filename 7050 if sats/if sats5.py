tal1 = int(input("mata in ett tal"))
tal2 = int(input("mata in ett till tal"))
tal3 = int(input("mata in det tredje talet"))
if tal1 > tal2 and tal3:
    print("det första talet är störst")
elif tal2 > tal1 and tal3:
    print("det andra talet är det största")
elif tal3 > tal1 and tal2:
    print("det tredje talet är störst")
else:
    print("lika stora")