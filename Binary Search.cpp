


#include <iostream.h>
#include <conio.h>
void display(int a[], int);
void binary_search(int a[], int, int);
void main()
{
	clrscr();
	int arr[25];
	int size = 6;
	int find = 50;
	int arr2[] = { 10,20,30,40,50,60 };
	display(arr, size);
	binary_search(arr2, size, find);			

	getch();
}

void display(int a[], int  ln)
{
	for (int i = 0; i < ln; i++)		
	{
		cout << a[i];					
		if (i < (ln - 1))					
			cout << ", ";
	}									
	cout << "\n";						
}

void binary_search(int a[], int ln, int search)
{																
	int beg = 0;												
	int end = ln - 1;											
	int mid = (beg + end) / 2;									
	while ((beg <= end) && (a[mid] != search)) 					
	{
		if (search < a[mid]) end = mid - 1;						
		else beg = mid + 1;										

		mid = (beg + end) / 2;									
	}

	if (beg > end) cout << "Item not found";					
	else cout << search << " is found in position : " << (mid + 1);
}																