#include<iostream>
#include<string>
using namespace std;

// class A {
//    public:
//         string name;
//         A(){
//             cout<<"constructor"<<endl;
//         }
//         ~A(){
//             cout<<"deconstructor"<<endl;
//         }    
// };

class A {
   public:
        string name;
        A();
        ~A();
  };



A::A(){
            cout<<"constructor A"<<endl;
            name = "A_V";
            cout<<name<<endl;
        }

A::~A(){
            cout<<"deconstructor A"<<endl;
        }    

class B {
    public:
        int age;
        B(){
            cout<<"Constructor B"<<endl;
            age=12;
            cout<<age<<endl;
        }
        ~B(){
            cout<<"Deconstructor B"<<endl;
        }
        // string name;
       
};


class C : public A,public B {
    public:
         C(){
            cout<<"Constructor C"<<endl;
        }
        ~C(){
            cout<<"Deconstructor C"<<endl;
        }
        void chng(string x,int y){
            name=x;
            age=y;
        }
};

int main(){
    C obj1;
    cout<<"hey"<<endl;
    obj1.name="Amrith";
    obj1.age = 23;
    cout<<"Before Chnging"<<obj1.name << obj1.age <<endl;
    obj1.chng("Venkat",25);
    cout<<"After Chng "<<obj1.name << obj1.age <<endl;
    return 0;

}