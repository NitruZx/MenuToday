import random

def bmi(weight, hight):
    """ find bmi""" # หาค่าของBMI
    find_bmi = weight/((hight/100)**2)
    return find_bmi

def bmr(weight, hight, age, sex):
    """ find bmr"""
    if sex == "male": # หาค่าcalของ ชาย,หญิง
        calories = 66+(13.7*weight) + (5*hight) - (6.8*age)
    elif sex == "female":
        calories = 665+(9.6*weight) + (1.8*hight) - (4.7*age)
    return calories

def check_u_bmi(bmi):
    """check your weight""" # checkว่าอยู่ในเกณไหน
    if bmi < 18.5:
        return "Under weight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal"
    elif  bmi >= 25 and bmi <30:
        return "Over weight"
    elif  bmi >= 30 and bmi < 35:
        return "Obese"
    elif bmi >= 35:
        return "EX Obese"
        
def find_menu(menu_c, num_cpm):
    menu_rice = [("ข้าวต้มทรงเครื่อง", 230), ("โจ๊กใส่ไข่", 250), ("ข้าวต้มปลา", 325), ("ข้าวแกงกะหรี่ไก่", 389), ("ข้าวผัดต้มยำทะเลแห้ง", 400), \
("ข้าวคลุกกะปิ", 410),("ข้าวเหนียวหมูทอด", 440),("ข้าวไข่เจียว",445),("ข้าวพะแนงเนื้อ", 457),("ข้าวผัดน้ำพริกกุ้งสด", 460),("ข้าวไก่อบ", 490),(\
"ข้าวกุ้งทอดกระเทียม", 495),("ข้าวหมูทอดกระเทียม", 525),("ข้าวหมกไก่", 534),("ข้าวผัดกะเพรากุ้ง", 540),("ข้าวหมูแดง", 541),("ข้าวผัดหมูใส่ไข่", 557),(\
"ข้าวผัดกะเพราหมู", 580),("ข้าวมันไก่ต้ม", 596),("ข้าวกะเพราเนื้อ", 622),("ข้าวผัดกะเพราหมูกรอบ", 650),("ข้าวผัดคะน้าหมูกรอบ", 670),(\
"ข้าวขาหมู", 690),("ข้าวมันไก่ทอด", 695)]
    menu_yum = [("ยำมาม่า", 105),("ยำไส้กรอก", 110),("ยำวุ้นเส้น", 120),("ยำขนมจีน", 220)]
    menu_noodle = [("ก๋วยเตี๋ยวเรือ", 180),("เส้นหมี่ลูกชิ้นน้ำใส", 225),("สุกี้แห้งทะเล", 280, \
"เย็นตาโฟ", 290),("บะหมี่น้ำต้มยำหมู", 300),("บะหมี่น้ำเกี๊ยวหมูแดง", 305),("ก๋วยเตี๋ยวต้มยำ", 320, \
"สุกี้น้ำไก่", 345),("ราดหน้าเส้นใหญ่หมู", 405),("มักกะโรนีผัดกุ้ง", 420),("ก๋วยเตี๋ยวคั่วไก่", 435, \
"ราดหน้าบะหมี่กรอบ", 515),("เส้นใหญ่ผัดซีอิ๊วใส่ไข่", 520),("ขนมจีนแกงเขียวหวานไก่", 594)]

    kid_org = []
    if "Rice" in menu_c:
        for i in menu_rice:
            if i[1] <= num_cpm:
                kid_org.append(i)
        # return random.choice(newrice)
    if "Sen" in menu_c:
        for i in menu_noodle:
            if i[1] <= num_cpm:
                kid_org.append(i)
        # return random.choice(newsen)
    if "yum" in menu_c:
        for i in menu_yum:
            if i[1] <= num_cpm:
                kid_org.append(i)
        # return random.choice(newyum)
    return kid_org
def calpermeal(num_meal, cal_want):
    """cpm"""
    num_cpm = cal_want//num_meal
    return num_cpm

def outmenu(num_meal, menu_c, cal_want):
    """out"""
    show_menu = []
    sumcal =  0
    for _ in range(num_meal):
        show_menu.append(random.choice(find_menu(menu_c, calpermeal(num_meal, cal_want))))
    for k in range(num_meal):
        sumcal += (show_menu[k][1])
    return show_menu, sumcal

def main():
    """ """
    print("Weight : ",end= "",)
    weight = float(input()) #เป็นKG
    print("Hight : ",end= "")
    hight = float(input()) #เป็นCM
    print("Age : ",end= "")
    age = int(input())  #เป็นปี
    print("Sex : ",end= "")
    sex = input().lower() # male or female
    bmireal = bmi(weight, hight)
    print("%.2f"%bmi(weight, hight))
    print("%d"%bmr(weight, hight, age, sex))
    print("You are "+check_u_bmi(bmireal)+" body")
    print("how many meal u want to eat? : ", end= "")
    num_meal = int(input())
    print("Calories u want to want : ", end= "")
    cal_want = int(input())
    print("Type of menu u want to eat : ", end= "")
    menu_c = input()
    print(outmenu(num_meal, menu_c, cal_want))
