#include <stdio.h>
/**
 * Main function where the program execution begins.
 * 
 * This program initializes two integers, x and y, with values 10 and 20, respectively.
 * It then enters a loop where it prints a message indicating that x is less than y,
 * along with the current value of x, until x is no longer less than y.
 * 
 * Parameters: None
 * 
 * Return value: Returns 0 to indicate successful execution.
 */
int main()
{
	int x, y;
	x = 10;
	y = 20;
	while (x < y)
	{
		printf("X is less than Y and its value is %d\n", x);
		x++;
	}
}