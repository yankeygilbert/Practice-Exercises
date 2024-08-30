#Acessing date - time functionality
from datetime import date

Patientdb = []
#<---------------------------------------------------------------------------->#
#Functionality Implemented Here
class HealthAnalyzer:
    #function to collect User Information
    def __init__(self):
        self.DateToday = date.today()
        pass
    def userinfo(self):
        #objective 1 Accepting user input **str mean string data type & ** int means Integer
        self.firstname = str(input("Enter Your FirstName \n"))
        self.lastname  = str(input("Enter your LastName \n"))
        self.DOB = str(input("Please Enter date of birth in YYYY-MM-DD \n"))
        self.weight = float(input("Enter your Weight on KG \n"))
        self.Height  = float(input("Enter your Height \n"))
        self.ChlLevel  = float(input("Enter your Cholestrol Level \n"))
        #Patient Record
        self.PatientRecord = {
            "first_name" : self.firstname, 
            "last_name" : self.lastname,
            "D_O_B" : self.DOB,
            "weight" : self.weight,
            "Height" : self.Height,
            "Chl_Level" :self.ChlLevel,
        }
        #appendinf to list
        Patientdb.append(self.PatientRecord)
    
    def restartProgram(self):
                    print(f"Please choose and Option \n 1.Add new patient \n 2.Search for a patient by last name \n 3.Update patient information \n 4.Exit \n")

                    print("#----------------------------------#")

                    value = int(input())
                    if value == 1:
                            AddPatient.userinfo()
                            AddPatient.healthAnalysis()
                            
                    if value == 2:
                        searchnn = input("Enter Patient lastname \n")
                        AddPatient.Search(searchnn)
                                          
                    if value == 3:
                                AddPatient.userinfo()
                                AddPatient.healthAnalysis()
                    
                    if value == 4:
                                print("Thank you for using the Patient Health Profile Manager & Analyzer!")
                                exit() 

                    else:
                     print("Thank you for using the Patient Health Profile Manager & Analyzer!")
                     exit()         
   
    #function perform analysis this takes a parameter that could be the search_lastname. 
    def healthAnalysis(self):
                    
                self.Record = self.PatientRecord
                self.Age = int(self.DateToday.year) - int(self.Record['D_O_B'][:4]) 

                if self.Age < 18 :
                    self.AgeCategory = "Minor"
                else:
                    self.AgeCategory = "Adult" 


                #BMI calculation

                self.BMI = self.Record['weight'] /(self.Record['Height'] * self.Record['Height'])

                if self.BMI < 18.5:
                    self.bmiCategory = "Underweight"
                elif self.BMI < 24.9 and self.BMI >= 18.5:
                    self.bmiCategory = "normal"
                elif self.BMI < 29.9 and self.BMI >= 25:
                    self.bmiCategory = "OverWeight"
                elif self.BMI >= 30:
                    self.bmiCategory = "Obessed"

                #Cholestrol Calculation

                self.Cholestrol = self.Record['Chl_Level'] 

                if self.Cholestrol < 200:
                    self.chlcategory = "Desirable"
                elif self.Cholestrol< 239 and self.Cholestrol >= 200:
                    self.chlcategory = "BoarderLine"
                elif self.Cholestrol >= 240: 
                    self.chlcategory = "High"
                
                        #Health Summary
                print("#----------------------------------#")
                self.fullname = self.Record['first_name'] +" "+ self.Record['last_name']
                print(f'Health Summary for {self.fullname}\n')
                print(f'AgeCategory:{self.AgeCategory}\n')
                print(f'BMICategory:{self.bmiCategory}\n')
                print(f'CholestrolLevel:{self.chlcategory}\n')
                
                print("Would you like to enter another patient's details? Yes/No")
                self.val = str(input())
            
                if self.val in ["Yes","yes","y","Y"] :
                    self.restartProgram()
    #function to  implement Search   
    def Search(self,Sname=""):
        #Get Patient Record
        for index in range(0,len(Patientdb)):
            print (Sname)
            if (Sname) == Patientdb[index]['last_name'] :
                self.Record = Patientdb[index]
                self.Age = int(self.DateToday.year) - int(self.Record['D_O_B'][:4]) 
                
                if self.Age < 18 :
                    self.AgeCategory = "Minor"
                else:
                    self.AgeCategory = "Adult" 
                    
                #BMI calculation

                self.BMI = self.Record['weight'] /(self.Record['Height'] * self.Record['Height'])

                if self.BMI < 18.5:
                    self.bmiCategory = "Underweight"
                elif self.BMI < 24.9 and self.BMI >= 18.5:
                    self.bmiCategory = "normal"
                elif self.BMI < 29.9 and self.BMI >= 25:
                    self.bmiCategory = "OverWeight"
                elif self.BMI >= 30:
                    self.bmiCategory = "Obessed"

                #Cholestrol Calculation

                self.Cholestrol = self.Record['Chl_Level'] 

                if self.Cholestrol < 200:
                    self.chlcategory = "Desirable"
                elif self.Cholestrol< 239 and self.Cholestrol >= 200:
                    self.chlcategory = "BoarderLine"
                elif self.Cholestrol >= 240: 
                    self.chlcategory = "High"

                print("#----------------------------------#")
                self.fullname = self.Record['first_name'] +" "+ self.Record['last_name']
                print(f'Health Summary for {self.fullname}\n')
                print(f'AgeCategory:{self.AgeCategory}\n')
                print(f'BMICategory:{self.bmiCategory}\n')
                print(f'CholestrolLevel:{self.chlcategory}\n')
            
                print("Would you like to enter another patient's details? Yes/No")
                self.val = str(input())
            
                if self.val in ["Yes","yes","y","Y"] :
                    self.restartProgram()
         # this Exits if users last name does not exist in Db
        print("User Not In Patient Records")
        print("Thank you for using the Patient Health Profile Manager & Analyzer!")
        exit()
#end of class

#Code Running start Here
AddPatient = HealthAnalyzer()
print("Patient Health Profile Manager & Analyzer \n")
        
print(f"Please choose and Option \n 1.Add new patient  \n 2.Update patient information \n 3.Exit \n")

print("#----------------------------------#")

value = int(input())

if value == 1:
         AddPatient.userinfo()
         AddPatient.healthAnalysis()
        
            
if value == 2:
            AddPatient.userinfo()
            AddPatient.healthAnalysis()
            

if value == 3:
            print("Thank you for using the Patient Health Profile Manager & Analyzer!")
            exit() 


