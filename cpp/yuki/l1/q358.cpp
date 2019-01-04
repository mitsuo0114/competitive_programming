#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

string solve(const int a1,const  int a2,const  int a3){
	if(a1 == a2 || a2 == a3 || a1 == a3){
		return "0";
	}else if( (a2 > a1 && a2 > a3) || (a2 < a1 && a2 < a3) ){
		return "INF";
	}

	int max = std::max( std::max(a1,a2), a3);
	int count = 0;
	for(int i = 1; i <= max; i++ ){
		int b1 = a1 % i;
		int b2 = a2 % i;
		int b3 = a3 % i;

		if(b1 == b2 || b2 == b3 || b1 == b3){
			continue;
		}else if( (b2 > b1 && b2 > b3) || (b2 < b1 && b2 < b3) ){
			count++;
		}
	}
	return to_string(count);
}

int main(){
	int a1, a2, a3;
	// cin >> a1 >> a2 >> a3;
	// cout << solve(a1,a2,a3) << endl;
	// return 0;

	cout << solve(5,6,7) << endl;
	cout << solve(5,1,4) << endl;
	cout << solve(10,20,30) << endl;
	cout << solve(114,514,114) << endl;

	return 0;
}

