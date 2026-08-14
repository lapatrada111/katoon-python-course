เขียน function ชื่อ convert_currency()
ที่ำหน้าที่แปลงสกุลเงิน
THB <--> USD กำหนดให้ 1 USD = 33 THB
ทั้งนี้ให้ function ดังกล่าว รับข้อมูล จำนวนเงินที่ต้องการแปล และสกุลเงินปลายทาง

วอย่างวิธีการเรียกใช้ conret_currency(100, "USD")

ตัวอย่างวิธีการเรียกใช้
convet_currency(100, "USD")
convet_currency(100, "THB")
 
ตัวอย่างหน้าจอ
100 THB = 3.33 USD
100 USD = 3300.3 THB
""

def convert_cerrency(value,currency):
    result = 0
    if cuerrency == "USD":
        result = value / 33.0
        print(f"{value} THB = {value / 33.0} USD")
    else:
        result = value * 33.0
        print(f"{value} USD = {result} THB")

convert_currency(100,"USD")
convert_currency(100,"THB")