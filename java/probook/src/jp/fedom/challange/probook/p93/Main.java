package jp.fedom.challange.probook.p93;

import java.util.ArrayList;

class V {
	public V(int i, int j) {
		n1 = i;
		n2 = j;
	}

	int n1;
	int n2;
}

public class Main {

	public static boolean solve(int N, V[] vs) {
		int c[] = new int[N];
		for (int i = 0; i < N; i++) {
			if (i == 0) {
				c[i] = 1;
			}

			for (V v : vs) {
				if (v.n1 == i) {
					if (c[v.n2] * c[i] == 1) {
						return false;
					} else {
						c[v.n2] = c[i] == 1 ? -1 : 1;
					}
				} else if (v.n2 == i) {
					if (c[v.n1] * c[i] == 1) {
						return false;
					} else {
						c[v.n1] = c[i] == 1 ? -1 : 1;
					}
				}
			}

		}

		return true;
	}

}
