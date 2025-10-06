/* Euler's method numerically approximates solutions of first-order ordinary differential equations (ODEs) with a given initial value.
   It is an explicit method for solving initial value problems (IVPs).

   The ODE has to be provided in the following form: dy(t)/dt = f(t,y(t))

   with an initial value y(t0) = y0

   To get a numeric solution, we replace the derivative on the LHS with a finite difference approximation:

    dy(t)/dt = ( y(t+h) - y(t) ) /  h

    then solve for y(t+h): y(t+h) = y(t) + h dy(t)/dt

    which is the same as

     y(t+h) = y(t) + h f(t,y(t))

   The iterative solution rule is then: yn+1 = yn + h f(tn, yn)

   where h is the step size, the most relevant parameter for accuracy of the solution.
   A smaller step size increases accuracy but also the computation cost, so it has always has to be hand-picked according to the problem at hand.

 Example: Newton's Cooling Law

  Newton's cooling law describes how an object of initial temperature  T(t0) = T0 cools down in an environment of temperature TR

   dT(t)/dt = - k DeltaT

   or dT(t)/dt = - k ( T(t) - TR )

   It says that the cooling rate  dT(t)/dt of the object is proportional to the current temperature difference   deltaT = (T(t) - TR) to the surrounding environment.

  The analytical solution, which we will compare to the numerical approximation, is

   T(t) = TR + (T0 - TR ) e-kt

 Implement a routine of Euler's method and then to use it to solve the given example of Newton's cooling law with it for three different step sizes of:

   2 s, 5 s and 10 s

 and to compare with the analytical solution.

 Initial values
                  initial temperature   T0 shall be 100 �C
                  room temperature      TR shall be  20 �C
                  cooling constant      k shall be 0.07
                  time interval to calculate shall be from  0 s to 100 s
*/
# include <stdio.h>
# include <math.h>

int main( void )
{
   double cooling( double, double, double );    /* k, Tr, T(t) */
   void analytic( double, double, double, double );   /* T0, Tr, k, tm */
   void ivp_euler( double(*)( double, double, double ), double, double, double, double, double );   /* fonction, T0, Tr, k, tm, dt */

   double T0, Tr, k, tm;

   (void)printf( "T0: " ); (void)scanf( "%lf", &T0 );
   (void)printf( "Tr: " ); (void)scanf( "%lf", &Tr );
   (void)printf( "k: " ); (void)scanf( "%lf", &k );
   (void)printf( "Temp max (s): " ); (void)scanf( "%lf", &tm );

   analytic( T0, Tr, k, tm );

   ivp_euler( cooling, T0, Tr, k, tm, 2.0 );
   ivp_euler( cooling, T0, Tr, k, tm, 5.0 );
   ivp_euler( cooling, T0, Tr, k, tm, 10.0 );

   return 0;
}

void ivp_euler( double (*f)( double, double, double ), double T0, double Tr, double k, double end_t, double step )
{
   int    t = 0;
   double y = T0;

   (void)printf( " Step %2f: ", step );

   do
   {
      if ( t % 10 == 0 ) { (void)printf( " %7.3f", y ); }

      y += ( step * f(k, Tr, y) );
   }
   while ( t <= end_t ); { t += step; };

   (void)printf( "\n" );
}

void analytic( double T0, double Tr, double k, double tm )
{
   int t;

   (void)printf( "    Time: " );

   for ( t = 0; t <= tm; t += 10 ) { (void)printf( " %7d", t ); }

   (void)printf( "\nAnalytic: " );

   for ( t = 0; t <= tm; t += 10 ) { (void)printf( " %7.3f", Tr + ( T0 - Tr ) * exp( -k * t ) ); }

   (void)printf( "\n" );
}

double cooling( double k, double Tr, double temp )
{
   return ( -k * ( temp - Tr ) );
}

