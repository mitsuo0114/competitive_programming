package jp.fedom.challange.probook.p49;

import java.util.Arrays;

public class Main {

	public static int solve(int[] L, int N) {
		int ans = 0;
		while (L.length > 1) {
			Arrays.sort(L);
			int n1 = L[0];
			int n2 = L[1];

			System.out.println(n1 + "/" + n2);
			ans += n1 + n2;

			L[1] = n1 + n2;
			L = Arrays.copyOfRange(L, 1, L.length);
		}
		return ans;
	}

}
