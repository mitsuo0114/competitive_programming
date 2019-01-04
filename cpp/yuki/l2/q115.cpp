#include <iostream>
#include <string>
#include <vector>
using namespace std;
static const int m = 16;



int solve(int N, int D, int K){
	if(  <= D + 1 || K * (K + 1) / 2 > D){
		cout << -1 << " ";
		return -1;
	}

	int i = D;
	while(i > 0){
		if(i % 2 != 0){
			cout << i << " ";
		}
		i /= 2;
	}
		// cout << N + D << " " << endl;
}

int main(){
	int N, D, K;
	// cin >> N >> D  >> K;
	// solve(N, D, K);
	 // solve(10, 9, 3);
	 solve(10, 9, 4);
	 solve(10, 55, 10);
	 // solve(30, 40, 4);
}