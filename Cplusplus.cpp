#include <iostream>
#include <iomanip>
#include <fstream>
#include "headerfile.h"


main(){
  timeZone Time;
  clockType time2;
  clockType timeess;

  std::string hey;

  int hour=7;
  int mins=3;
  int sec=5;
  
  timeess.settime(0,0,0);
  time2.settime(1,2,3);
  equal<clockType>(time2,timeess);
  time2.printTime();

 
 int *collecttime = Time.time(&hour,&mins,&sec);
 time2.printTime();
 std::cout << collecttime[1]<<std::endl;
 Time.equaltime(time2) ? std::cout<<"E"<<std::endl : std::cout<<"F"<<std::endl;

 
  std::ofstream file;
  std::ifstream filein;

  file.open("home.txt",std::ios::app);
  filein.open("home.txt");

  file<<"halleujah\n"<<std::endl;

  filein>>hey;

  std::cout<<hey<<std::endl;
  functionOverload obj;
  functionOverload t1(&hour,&mins,&sec);
  functionOverload t2(&hour,&mins,&sec);

 file.close();
 filein.close();
 
 std::cout<<argvet('a','b')<<std::endl;
 obj= t1 + t2;
 std::cout<<obj.val3;
 return 0;
}
