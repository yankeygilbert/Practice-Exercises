#Acessing date - time functionality
from datetime import date
#<---------------------------------------------------------------------------->#
#Functionality Implemented Here
class HealthAnalyzer:
    #function to collect User Information
    def __init__():
        pass
    def userinfo(self):
        #objective 1 Accepting user input **str mean string data type & ** int means Integer
        self.firstname = str(input("Enter Your FirstName \n"))
        self.lastname  = str(input("Enter your LastName \n"))
        self.DOB = str(input("Please Enter date of birth in YYYY-MM-DD \n"))
        self.weight = int(input("Enter your Weight on KG \n"))
        self.Height  = int(input("Enter your Height \n"))
        self.ChlLevel  = int(input("Enter your Cholestrol Level \n"))
        self.DateToday = date.today()
        
    
    #function to store User Information   
    def storeInfo(self):
        #Storing Patient in Dictionary
        self.PatientRecord = {
            "first_name" : self.firstname, 
            "last_name" : self.lastname,
            "D_O_B" : self.DOB,
            "weight" : self.weight,
            "Height" : self.Height,
            "Chl_Level" :self.ChlLevel,
        }

        # storing Records in List 
            #creating an empty list
        self.PatientDB = []
        #appendidng to list 
        self.PatientDB.append(self.PatientRecord)
       
    #function perform analysis this takes a parameter that could be the search_lastname. 
    def healthAnalysis(self):
        #Patient Health Analysis

            #Getting Current Date
        #Get Patient Record
        for index in range(0,len(self.PatientDB)):
            if (self.lastname ) == self.PatientDB[index]['last_name']:
                self.Record = self.PatientDB[index]
        
            else:
                # this Exits if users last name does not exist in Db
                print("User Not In Patient Records")
                exit

        #Calculate  patient age
        # this part extracts the year from the DOB in the record and adds to subtracts from current Year

        self.Age = int(self.DateToday.year) - int(self.Record['D_O_B'][:3]) 

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

    #function to  implement Search   
    def Search(self,Sname=" "):
        self.searchlastname = Sname
        #Patient Health Analysis

            #Getting Current Date
        #Get Patient Record
        for index in range(0,len(self.PatientDB)):
            if (self.searchlastname ) == self.PatientDB[index]['last_name']:
                self.Record = self.PatientDB[index]
        
            else:
                # this Exits if users last name does not exist in Db
                print("User Not In Patient Records")
                exit

        #Calculate  patient age
        # this part extracts the year from the DOB in the record and adds to subtracts from current Year

        self.Age = int(self.DateToday.year) - int(self.Record['D_O_B'][:3]) 

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
    #function to display Summary
    def Summary(self):
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
            print("Patient Health Profile Manager & Analyzer \n")
        
            print(f"Please choose and Option \n 1.Add new patient \n 2.Search for a patient by last name \n 3.Update patient information \n 4.Exit \n")
           
            print("#----------------------------------#")
            self.value = int(input())

           
            if self.value == 1:
                AddPatient.userinfo()
                AddPatient.storeInfo()
                AddPatient.healthAnalysis()
                AddPatient.Summary()
                
            if self.value == 2:
                
                searchname = input("Enter Patient lastname \n")
                AddPatient.Search(searchname)
                AddPatient.Summary()
                    

            if self.value == 3:
                
                AddPatient.userinfo()
                AddPatient.storeInfo()
                AddPatient.healthAnalysis()
                AddPatient.Summary()
                

            if self.value == 4:
                print("Thank you for using the Patient Health Profile Manager & Analyzer!")
                exit 
        else:   
            print("Thank you for using the Patient Health Profile Manager & Analyzer!")
        



#Code Running start Here
print("Patient Health Profile Manager & Analyzer \n")
        
print(f"Please choose and Option \n 1.Add new patient  \n 2.Update patient information \n 3.Exit \n")

print("#----------------------------------#")

value = int(input())
AddPatient = HealthAnalyzer()
if value == 1:
         AddPatient.userinfo()
         AddPatient.storeInfo()
         AddPatient.healthAnalysis()
         AddPatient.Summary()
            
if value == 2:
            AddPatient.userinfo()
            AddPatient.storeInfo()
            AddPatient.healthAnalysis()
            AddPatient.Summary()
            

if value == 3:
            print("Thank you for using the Patient Health Profile Manager & Analyzer!")
            exit 


