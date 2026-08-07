"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""

# อัตราแลกเปลี่ยน: 1 USD = 35.5 THB
EXCHANGE_RATE = 35.5

# ให้ผู้ใช้เลือกทิศทางการแปลง
print("เลือกทิศทางการแปลงสกุลเงิน")
print("1. THB to USD")
print("2. USD to THB")
choice = input("กรุณาเลือก (1 หรือ 2): ")

# รับจำนวนเงินที่จะแปลง
amount = float(input("กรุณากรอกจำนวนเงินที่ต้องการแปลง: "))

if choice == "1":
    # แปลงจากบาทเป็นดอลลาร์: หารด้วยอัตราแลกเปลี่ยน
    result = amount / EXCHANGE_RATE
    print(f"\nสูตรที่ใช้: USD = THB / {EXCHANGE_RATE}")
    print(f"{amount:.2f} THB = {result:.2f} USD")
elif choice == "2":
    # แปลงจากดอลลาร์เป็นบาท: คูณด้วยอัตราแลกเปลี่ยน
    result = amount * EXCHANGE_RATE
    print(f"\nสูตรที่ใช้: THB = USD x {EXCHANGE_RATE}")
    print(f"{amount:.2f} USD = {result:.2f} THB")
else:
    print("กรุณาเลือก 1 หรือ 2 เท่านั้น")
