#include <stdio.h>
#include <math.h>
#include <time.h>
float Q_rsqrt( float number )
{
	long i;
	float x2, y;
	const float threehalfs = 1.5F;

	x2 = number * 0.5F;
	y  = number;
	i  = * ( long * ) &y;                       // evil floating point bit level hacking
	i  = 0x5f3759df - ( i >> 1 );               // what the fuck? 
	y  = * ( float * ) &i;
	y  = y * ( threehalfs - ( x2 * y * y ) );   // 1st iteration
//	y  = y * ( threehalfs - ( x2 * y * y ) );   // 2nd iteration, this can be removed

	return y;
}

int main() {
   // printf() displays the string inside quotation
   printf("Hello, World!\n");
//    double time_spent = 0.0;
   clock_t begin = clock();
   printf("Inbuild Sqrt: %.6f, ", 1/sqrt(125461.0));
   clock_t end = clock();
   double time_spent = (double)(end - begin);
   printf("elapsed time : %f\n", time_spent);
   
   begin = clock();
   printf("Fast InvSqrt: %.6f, ", Q_rsqrt(125461.0));
   end = clock();
   time_spent = (double)(end - begin);
   printf("elapsed time : %f\n", time_spent);

   return 0;
}