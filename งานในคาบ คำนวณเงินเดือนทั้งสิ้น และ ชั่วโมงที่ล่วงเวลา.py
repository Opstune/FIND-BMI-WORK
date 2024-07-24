def cal_salary():
    print("--------------------------------------------")
    name = str(input("ชื่อพนักงาน: "))
    base_salary = float(input("เงินเดือนปกติ (บาท/เดือน): "))
    ot_hours = int(input("จำนวนชั่วโมงที่ล่วงเวลา: "))
    
    # ค่าจ้างต่อชั่วโมง
    hour_rate = 100
    #คำนวณชั่วโมงล่วงเวลา
    overtime_salary = base_salary + (ot_hours*hour_rate)
    #ตรวจสอบเงื่อนไข ถ้ามากกว่า 40 คิดชั่วโมงละ 1.5
    if ot_hours > 40:
        overtime_pay = (ot_hours - 40) * hour_rate * 1.5
        overtime_salary += overtime_pay
        total_salary = overtime_salary + base_salary


    print("--------------------------------------------")
    print(f"ชั่วโมงที่ล่วงเวลา : {overtime_pay:.2f} บาท")
    print(f"รวมเป็นเงินเดือนทั้งสิ้น : {total_salary:.2f} บาท")
    print("--------------------------------------------")
    

cal_salary()