#include <iostream>
using namespace std;
void take_data(int a[][10], int b[][10], int r1,int c1, int r2, int c2);
void multiplication(int a[][10],int b[][10],int mult[][10],int r1,int c1,int r2,int c2);
void display(int mult[][10], int r1, int c2);
int main()
{
    int a[10][10], b[10][10], mult[10][10], r1, c1, r2, c2, i, j, k;
    cout << "Enter rows and columns for first matrix: ";
    cin >> r1 >> c1;
    cout << "Enter rows and columns for second matrix: ";
    cin >> r2 >> c2;

/* If colum of first matrix in not equal to row of second matrix, asking user to enter the size of matrix again. */

    while (c1!=r2)
    {
        cout << "Error! column of first matrix not equal to row of second." << endl;
        cout << "Enter rows and columns for first matrix: ";
        cin >> r1 >> c1;
        cout << "Enter rows and columns for second matrix: ";
        cin >> r2 >> c2;
    }
    take_data(a,b,r1,c1,r2,c2);  /* Function to take matrices data */
    multiplication(a,b,mult,r1,c1,r2,c2); /* Function to multiply two matrices. */
    display(mult,r1,c2); /* Function to display resultant matrix after multiplication. */
    return 0;
}

void take_data(int a[][10], int b[][10], int r1,int c1, int r2, int c2)
{
    int i,j;
    cout << endl << "Enter elements of matrix 1:" << endl;
    for(i=0; i<r1; ++i)
    for(j=0; j<c1; ++j)
    {
        cout << "Enter element a" << i+1 << j+1 << " : ";
        cin >> a[i][j];
    }

    cout << endl << "Enter elements of matrix 2:" << endl;
    for(i=0; i<r2; ++i)
    for(j=0; j<c2; ++j)
    {
        cout << "Enter element b" << i+1 << j+1 << " : ";
        cin >> b[i][j];
    }
}

void multiplication(int a[][10],int b[][10],int mult[][10],int r1,int c1,int r2,int c2)
{
    int i,j,k;
/* Initializing elements of matrix mult to 0.*/
    for(i=0; i<r1; ++i)
    for(j=0; j<c2; ++j)
    {
       mult[i][j]=0;
    }
/* Multiplying matrix a and b and storing in array mult. */
    for(i=0; i<r1; ++i)
    for(j=0; j<c2; ++j)
    for(k=0; k<c1; ++k)
    {
        mult[i][j]+=a[i][k]*b[k][j];
    }
}

void display(int mult[][10], int r1, int c2)
{
    int i, j;
    cout << endl << "Output Matrix: " << endl;
    for(i=0; i<r1; ++i)
    for(j=0; j<c2; ++j)
    {
        cout << " " << mult[i][j];
        if(j==c2-1)
            cout << endl;
    }
}
