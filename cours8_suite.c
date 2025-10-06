#include <stdio.h>
#include <math.h>

void u(int);

int main()
{
  int n;
  
  scanf("%d", &n);
  
  double result = (4 * pow(5,n+1) - 3 * pow(6, n+1)) / (4 * pow(5,n) - 3 * pow(6,n));
  
  u(n);
  printf("Le résultat devrait être:\nu(%d) = %lf\n", n, result);
  
  
return 0; 
}


void u(int n)
{
  int i;
  
  double u_nmoins1 = 2.0;
  double u_n = -4.0;
  double u_nplus1;
  
  printf("u(0) = %lf\n", u_nmoins1);
  printf("u(1) = %lf\n", u_n);
  
  for (i=2; i<=n; i++)
  {
    u_nplus1 = 111 - 1130/u_n + 3000/(u_n*u_nmoins1);
    printf("u(%d) = %lf\n", i, u_nplus1);
    
    u_nmoins1 = u_n;
    u_n = u_nplus1;
  }
   
}


/*

U(0)=2
U(1)=-4
U(n+1)=111 - 1130/U(n) + 3000/(U(n)*U(n-1))

U(n)=(4*5^(n+1) - 3*6^(n+1)) / (4*5^n - 3*6^n) tend vers 6


*/
