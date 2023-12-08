#define arrlim 100
#ifndef argvet
  #define argvet(a,b) a+b
#endif
#include <iostream>
#include <string>


 template <typename Type>
      Type equal(Type &val1,Type &val2){
        
            return val1=val2;
        
      }

template <typename classtype>
      class testing{
          public:
            classtype add(classtype val1,classtype val2);
        };

template<typename classtype>
    classtype  testing<classtype>::add(classtype val1,classtype val2){

      }

// class definition
class clockType{
  private:
    int hr,min,sec;
    std::string tzone;
  
  public:
    void settime(int,int,int);
    void printTime() const;
    void timer(int,int,int) const;
    bool equaltime(const clockType &) const;
  
    clockType();
    
};

//class implementation

clockType::clockType(){
  hr=0;
  min=0;
  sec=0;
 
}

void clockType::settime(int hour,int mins,int secs){
   hr = hour;
   min = mins;
   sec = secs;
}

void clockType::printTime() const {
    std::cout<<hr<<":"<<min<<":"<<sec<<std::endl;
}

void clockType::timer(int hour, int mins, int secs) const{
    for(hour; hour>=0 && hour<12; hour--){
      for(mins; mins>=0 && mins<60;mins-- ){
        for(secs;secs>=0 && secs<60;secs--){
           std::cout<<hour+":"<<mins+":"<<secs<<std::endl;
        } 
      }
    }
}
bool clockType::equaltime(const clockType &compClock) const {
  return(hr == compClock.hr && min == compClock.min && sec == compClock.sec);
}

// Structure definition 
struct studenType{
  
  std::string home;
  std::string type;
  std::string address;
  std::string func1 (){
    std::cout<<"you made it "<<std::endl;
  }
     
};

void collect(studenType student[])
{
  std::cout <<student[1].home<<std::endl;
}

struct studenType student(studenType &structvar){
  return structvar;
}

//Derived class definition
class timeZone:public clockType{
  public:
    
    std::string zone;
    int *time(int *,int *,int *);
    void settime(int,int,int,std::string) ;
    timeZone();
    
 
};

// derived class implementaiton

int* timeZone::time(int *hour,int *mins,int *secs){

  int *p[3]={hour,mins,secs};
 
  return *p;
}
void timeZone::settime(int hour,int min,int sec,std::string tzone)  {
    clockType::settime(hour,min,sec);
    zone = tzone;
}

//constructor 
timeZone::timeZone(){
  clockType::settime(1,2,5);
   zone= "africa";
}

 class functionOverload{
    public:
      functionOverload();
      functionOverload(int*,int*,int*);
      friend functionOverload operator+ (const functionOverload&,const functionOverload&);
    
      int val1,val2,val3;
    
       
 };
 functionOverload::functionOverload(){
   
 }

 functionOverload::functionOverload(int *v1,int *v2, int* v3){
  val1= *v1;
  val2= *v2;
  val3 =*v3;
 }

functionOverload operator + (const functionOverload &otherClass1, const functionOverload &othercalss2) {
        functionOverload result;
        result.val3= otherClass1.val1+othercalss2.val2;
        return result;
  }
  