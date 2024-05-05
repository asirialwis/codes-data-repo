#include<iostream>
#include<vector>
#include<vector>
using namespace std;
int main (void)
{  
    vector<double>temp{87.8,89.5,90.3,91.3};
    double ave_temp{};
    double tot;
    
    
    
    for (auto temps:temp)  // THis method is available on C++ 11
       tot += temps;
        
     //for (unsigned i = 0; i < temp.size(); i++)
        // tot += temp[i];
        
        
    if (temp.size() != 0){
        ave_temp = tot / temp.size();
    }
        
        //cout << fixed <<  setprecision(1);
       cout << "Average tempreture is " << ave_temp << endl; 
       
       
    
    
   cout << endl;
    return 0;
}