#include <stdio.h>
#include <stdlib.h>

int a[10] = {6,1,2,7,9,3,4,5,10,8 };
int n = 10;
void quicksort(int left, int right)
{
	int i, j, t, temp;
	if (left > right)
		return;

	temp = a[left];
	i = left;
	j = right;
	while (i != j)
	{
		while (a[j]>=temp &&i<j)
		{
			j--;
		}
		while (a[i] <= temp && i < j)
		{
			i++;
		}
		if (i < j)
		{
			t = a[i];
			a[i] = a[j];
			a[j] = t;
		}
	}
	a[left] = a[i];
	a[i] = temp;

	quicksort(left, i - 1);
	quicksort(i + 1, right);

}

int main()
{
	int i, j, t;
	n = 10;
	
	quicksort(0, n);
	for(i =0; i <= n;i++)
		{
		printf("\n%d", a[i]);
		}
	system("pause");


}
