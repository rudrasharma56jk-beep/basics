total_bill = float(input("Total amount of bill "))
tip_percent = float(input("Tip u want to give "))
no_people = int(input("no of people "))
tip_paaid = (total_bill*tip_percent)/100
new_total = tip_paaid+total_bill
header = "Bill".center(30,"_")
print(f"""{header}
Total bill was {total_bill:.2f}
tip percent is {tip_percent:g}
tip paid {tip_paaid:.2f}
new total {new_total:.2f}
each share {(new_total/no_people):.2f}
""")