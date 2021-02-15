#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
using namespace std;


/*
// 1
int main()
{    
    int a, b, c;  
    cin >> a >> b >> c; //a < c and b < c
    
    if (a > c || b > c)
        cout << "Please, enter numbers in ascending order";
    else
        if (c >= a + b)
    	    cout << "impossible" << endl;
        else
        	if (c*c == a*a + b*b)
    	    	cout << "right" << endl;
        	if (c*c < a*a + b*b)
    	    	cout << "acute" << endl;
	    	if (c*c > a*a + b*b)
    		    cout << "obtuse" << endl;
					
    return 0;
    
}
*/


/*
// 2
int main()
{    

    int T;  
    cin >> T; 
    int t1, t2, t3, S ;
    t1 = T % 10;
    t2 = (T / 10) % 10;
    t3 = T / 100;
    S = t1 + t2 + t3;
    cout << S;
    return 0;
    
}
*/


/*
// 3
int main()
{
	int X, s, x;
	cin >> X;
	s = 2;
	while (s <= X){
	    if (X % s == 0){
	        x = X / s;
	        cout << "*" << s;
			X = x;}
	    else    
	        s += 1;
    }
    return 0;  
}
*/



// 4
/*
//--------------
int prime(int n) {
	//cin >> n;
	int j, a;
    a = 0;
    for (int p = 2;; p++)   {
        for (j = 2; j*j <= p; j++)
        
        if ((p % j) == 0) {
            break;}
        if (j*j > p) {
            a++;
            if (a == n) 
            {
                cout << p << endl;
                break;
            }
        }
    }
    return 0;
}
 
int main() {
	int n;
	cin >> n;
    cout << prime(n);
    return 0;
}
*/


// 5

/*
int main()
{
	 int i2, j2, k2, m2, i, j, k, m, N;
	 cin >> N;
     i2 = 0;
for(i=0; i2 < N; i++) {
  i2 = j2 = i*i; 
  for(j=i; i2 + j2 <N; j++) {
    j2 = k2 = j*j;
    for(k=j; i2 + j2 + k2 < N; k++) {
      k2 = m2 = k*k;
      for(m=k; i2 + j2 + k2 + m2 <= N; m++) {
        m2 = m*m;
        if (i2+j2+k2+m2 == N)
          cout << N << "="  << i2 << "+" << j2 <<"+" << k2 << "+" << m2 << endl;
      }
    }
  }
}
   return 0;
}

 */


//6


//7
/*
int main(){

int	N, i, j;
cin >> N;

for(i=0; i*i*i < N; i++){
  for(j=i; i*i*i + j*j*j <= N; j++){
    if (i*i*i + j*j*j == N){
      cout << i << "^3 + " << j<< "^3 = " << N << endl;
      break;}
    else
	  cout <<"impossible";
 
      break;
      
	    
}
}
return 0;
}
*/

//8

/*
//--------------
int main()
{
    int a, b, m;
    cin >> a >> b >> m;
    int n = 1;
{   
    int x = 0, y = 1;
    for (int i = 0; i < n; i++)
    { 
        int r1 = a*y, r2 = m, x1 = 1, x2 = 0, r = 1;
        while (r != 0)
        {
            int q = (int)floor((double)r1/r2), t = x1 - q*x2;
            x1 = x2; x2 = t; r = r1 - q*r2; r1 = r2; r2 = r;
        }
        int b1 = b - a*x;
        if (b1 % r1 != 0)
        { 
           cout <<"no solutions"; 
        }
        x += y * b1 * x1/r1;
        y *= m/r1; 
    }
    if (x < 0 || x >= y) 
        x -= y * (int)floor((double)x/y);
    cout <<"x = " << x ;

}
    return 0;
}
*/


//9



	































