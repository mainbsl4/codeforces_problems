#include <iostream>
using namespace std;

int main(){
    int inp;

    cin >> inp;

    if (inp % 2 == 0 and inp > 2){
        cout << "YES";
    }
    else{
        cout << "NO";
    }
}