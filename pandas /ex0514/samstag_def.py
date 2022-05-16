def all_Age(age):
    
    if age < 20:
        real_age = 10
        
    elif age < 30:
        real_age = 20
        
    elif age < 40:
        real_age = 30
        
    elif age < 50:
        real_age = 40
        
    elif age < 60:
        real_age = 50
        
    elif age < 70:
        real_age = 60
        
    elif age < 80:
        real_age = 70
        
    elif age < 90:
        real_age = 80
    
    else:
        real_age = 90
        
    return real_age

# 1. 신용등급별 대출이자 계산 (A:1%, B:3%, C:5%, D:7%)

def Interest(interest):
    if interest == 0:
        result = 0.01     
    
    elif interest == 1:
        result = 0.03
        
    elif interest == 2:
        result = 0.05  
    
    else:
        result = 0.07
        
    return result 
        