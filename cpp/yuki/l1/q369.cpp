#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int solve(int N, int a[], int v){
	int c = 0;
	for(int i = 0; i < N; i++){
		c += a[i];
	}
	return c - v;
}

int main(){
	int N, v;
	cin >> N;
	int a[N];
	for(int i = 0; i < N; i++){
		cin >> a[i];
	}
	cin >> v;
	cout << solve(N,a,v) << endl;
	return 0;

	int a1[] = {5, 1, 4, 3};
	cout << solve(4, a1, 10) << endl;
	int a2[] = {2, 1, -1};
	cout << solve(3, a2 ,0) << endl;
	int a3[] = {-5, -2, -4};
	cout << solve(3, a3 ,0) << endl;

	return 0;
}

