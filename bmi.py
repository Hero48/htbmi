# Attributes

print("Welcome to Heroz Tech BMI calculator")

Name = input( "what is your name ? ")
Age = int( input("Your age ? "))
Height = float(input("What is your height ? "))
Weight = float(input("What is your Weight ? "))

# abreviations

a = Name
b = Age 
c = Height
d = Weight 

#calculation

x = d/ c**2
  
# results output

print("Your BMI is = " , x)


if x < 18:
    print(a , "you are under weight")
if 18.5 < x < 25.1:
    print(a , "you have a  normal weight")
if 25 < x <30.1:
    print(a , "you are overweight")
if x > 30:
    print(a , "You are obese")
    
print("Thank you for using htBMI")

