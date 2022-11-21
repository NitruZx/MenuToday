def bmi(weight, hight):
    body_mase_index = weight/((hight/100)**2)
    return body_mase_index

def bmr(weight, hight, age, sex):
    if sex == "Male":
        calories = 66+(13.7*weight) + (5*hight) - (6.8*age)
    elif sex == "Female":
        calories = 665+(9.6*weight) + (1.8*hight) - (4.7*age)
    return calories

def check_u_bmi(bmi):
    if bmi < 18.5:
        return "Under"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal"
    elif  bmi >= 25 and bmi <30:
        return "Over weight"
    elif  bmi >= 30 and bmi < 35:
        return "Obese"
    elif bmi >= 35:
        return "EX Obese"

def main():
    print("Weight : ",end= "",)
    weight = float(input()) #เป็นKG
    print("Hight : ",end= "")
    hight = float(input()) #เป็นCM
    print("Age : ",end= "")
    age = int(input())  #เป็นปี
    print("Sex : ",end= "")
    sex = input() # male or female
    bmireal = bmi(weight, hight)
    print("%.2f"%bmi(weight, hight))
    print("%d"%bmr(weight, hight, age, sex))
    print(check_u_bmi(bmireal))
    print("how many meal u want to eat? : ", end= "")
    num_meal = int(input())
    print("Calories u want to เอาออก : ", end= "")
    cal_out = int(input())
    
main()

