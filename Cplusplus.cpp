#include <iostream>
#define arrlim 100

 template <typename Type>
 Type equal(Type val1,Type val2){
    if(sizeof(Type) == 1){
      val1=val2;
    }
   if(sizeof(Type) == 4 || sizeof(Type)==2 ){
      return (val1+val2);
    }
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
     
      functionOverload(int*,int*,int*);
      ~functionOverload();
      friend functionOverload operator+ (const functionOverload&,const functionOverload&);

     private:
       int val1,val2,val3;
 };

 functionOverload::~functionOverload(){
  
 }
 functionOverload::functionOverload(int *v1,int *v2, int* v3){
  val1= *v1;
  val2= *v2;
  val3 =*v3;
  std::cout<< v1 <<":"<< val1 <<std::endl;

 }

  functionOverload operator+ (const functionOverload &otherClass1, const functionOverload &othercalss2) {

  }

main(){
  timeZone Time;
  clockType time2;
  clockType timeess;
  studenType guess[arrlim];
  studenType clen;

  int hour=3;
  int min=6;
  int sec=45;
 

 int y = equal<int>(hour,min);
  std::cout<< y<<std::endl;

   //guess[1] = {"anaji","young","12333"};
   
  //collect(guess);
 // student(clen);
 //int *collecttime = Time.time(&hour,&min,&sec);
 //time2.printTime();
 //std::cout << collecttime[1]<<std::endl;
 //Time.equaltime(time2) ? std::cout<<"E"<<std::endl : std::cout<<"F"<<std::endl;

  //functionOverload obj1(&hour,&min,&sec);


 return 0;

}
