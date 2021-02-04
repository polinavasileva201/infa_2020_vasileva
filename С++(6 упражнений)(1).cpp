#include <iostream>
#include <cmath>
#include <string>
using namespace std;



/*
int main()
{
    cout << "Hello, World!"<< endl;
    return 0;
}
*/


/*
// упражнение №1
int main()
{
    cout << "mipt" << 2021 << '.' << true << endl;
    cout << "Please, enter your full name:";
    string name;
    //cin >> name;
    getline(cin, name);
    cout << name; //check 
    return 0;
}
*/


/*
// упражнение №2
int main()
{
	double x, y; 
    cin >> x >> y;  
    cout << sqrt(x*x + y*y) << endl; 
    return 0;  
}
*/


/*
// упражнение №3
int main()
{
	int N,i,j;
	cin >> N; 
    for(i=0;i<N;i++)
    {
    for (j=0; j<N; j++)
    {
        cout<<'*';
    }
    cout<<endl;
    }
    return 0; 
}
*/


/*
// упражнение №4
int main()
{
	int N,i,j;
	cin >> N; 
    for(i=0;i<N;i++)
    {
    for (j=0; j<i+1; j++)
    {
        cout<<'*';
    }
    cout<<endl;
    }
    return 0; 
}
*/


/*
// упражнение №5
int main()
{
	int N,i,j;
	cin >> N; 
    for(i=0;i<N;i++)
    {
    for (j=0; j<N-i; j++)
    {
        cout<<'*';
    }
    cout<<endl;
    }
    return 0; 
}
*/



// упражнение №6
int main()
{
	int N,i,j;
	cin >> N;
	if (N%2 == 0)
	    cout<< "Please, enter an odd number for a beautiful figure:)";
	else
	
    for(i=0;i<((N+1)/2);i++)
    {
    for (j=0; j<N; j++)
    {
        if (j<i||j>=N-i)
            cout<<' ';
        else cout<<'*';
    }
    cout<<endl;
    }
    return 0; 
}








