#include <iostream>
#define arrlim 100

// class definition
class clockType{
  private:
    int hr,min,sec;
    static int count;
  
  public:
  
    void settime(int,int,int);
    void gettime() const;
    void timer(int,int,int) const;
    bool equaltime(const clockType &) const;
    clockType();
};

//class implementation

clockType::clockType(){
  (hr,min,sec)=0;
 
}
void clockType::settime(int hour,int mins,int secs){
   hr = hour;
   min = mins;
   sec = secs;
}

void clockType::gettime() const {
    std::cout<<hr+":"<<min+":"<<sec<<std::endl;
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
    
   private:
    int hr,min,sec; 
};

// derived class implementaiton
int *timeZone::time(int *hour,int *mins,int *secs){
  hr = *hour;
  min= *mins;
  sec= *secs;
  int *p[3]={hour,mins,secs};
 
  return *p;
}
void timeZone::settime(int hour,int min,int sec,std::string tzone)  {
    clockType::settime(hour,min,sec);
    zone = tzone;
}

timeZone::timeZone(){
  clockType::settime(0,0,0);
   zone= "africa";
}

main(){

  timeZone Time;
  studenType guess[arrlim];
  studenType clen;
   
  int hour = 12;
  int min,sec;

   guess[1] = {"anaji","young","12333"};
   
  //collect(guess);
  //student(clen);
 int *collecttime = Time.time(&hour,&min,&sec);
 
 std::cout << collecttime[1]<<std::endl;

return 0;


  
}
