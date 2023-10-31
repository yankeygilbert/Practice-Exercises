#include <iostream>
#define arrlim 100

class clockType{
  private:
    int hr,min,sec;
  
  public:
    void settime(int,int,int);
    void gettime() const;
    void timer(int,int,int) const;
};

void clockType::settime(int hour,int mins,int secs){
   hr = hour;
   min = mins;
   sec = secs;
}

void clockType::gettime() const {
    std::cout<<hr+":"<<min+":"<<sec<<std::endl;
}

void clockType::timer(int hour, int mins, int secs) const{
    for(hour; hour>0; hour--){
      for(mins; mins>0 && mins<60;mins-- ){
        for(secs;secs>0 && secs<60;secs--){
           std::cout<<hour+":"<<mins+":"<<secs<<std::endl;
        } 
      }
    }
}
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

main(){
  
   studenType guess[arrlim];
   studenType clen;
  

   guess[1] = {"anaji","young","12333"};
   
  collect(guess);
  student(clen);
return 0;
  
}

