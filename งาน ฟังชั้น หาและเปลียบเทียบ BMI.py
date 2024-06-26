def calculate_bmi(weight, height):
    height_meter = height / 100  
    bmi = weight / (height_meter ** 2) 
    return bmi
######################################################################################
def compare_bmi(weight, height):
    if bmi > 30:
        return ("อยู่ในเกณฑ์ : อ้วนมาก / โรคอ้วนระดับ3\nภาวะเสี่ยงต่อโรค : อันตรายระดับ 3")
    elif bmi >= 25 and bmi <= 29.90:
        return ("อยู่ในเกณฑ์ : อ้วน / โรคอ้วนระดับ2\nภาวะเสี่ยงต่อโรค : อันตรายระดับ 2")
    elif bmi >= 23 and bmi <= 24.90:
        return ("อยู่ในเกณฑ์ : ท้วม / โรคอ้วนระดับ1\nภาวะเสี่ยงต่อโรค : อันตรายระดับ 1")
    elif bmi >= 18.50 and bmi <= 22.90:
        return ("อยู่ในเกณฑ์ : ปกติ (สุขภาพดี)\nภาวะเสี่ยงต่อโรค : เท่าคนปกติ")
    else:
        return "อยู่ในเกณฑ์ : น้ำหนักน้อย / ผอม\nภาวะเสี่ยงต่อโรค : มากกว่าคนปกติ:"

#####################################################################################

weight = float(input("โปรดบอกนำหนักตัวของคุณ[กิโลกรัม] : "))
height = float(input("โปรดบอกความสูงของคุณ[เซนติเมตร] : "))
bmi = calculate_bmi(weight, height)
print(f"\nดัชนีมวลกายของคุณคือ {bmi:.2f}\n-------------------------")
result = compare_bmi(weight, height)
print(result)
print("-------------------------")