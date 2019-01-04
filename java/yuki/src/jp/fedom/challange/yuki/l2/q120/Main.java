package jp.fedom.challange.yuki.l2.q120;

import java.io.ByteArrayInputStream;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

class CN {
	public CN(int i) {
		n = i;
	}

	int n;

	public String toString() {
		return "" + n;
	}

}

public class Main {

	public static void main(String[] args) {
		Scanner sc;
		if (args.length == 0) {
			sc = new Scanner(System.in);
		} else {
			sc = new Scanner(new ByteArrayInputStream(args[0].getBytes()));
		}
		int T = sc.nextInt();
		for (int i = 0; i < T; i++) {
			int N = sc.nextInt();
			long[] L = new long[N];
			for (int j = 0; j < N; j++) {
				L[j] = sc.nextLong();
			}
			System.out.println(solve(N, L));
		}
		sc.close();
	}

	public static int solve(int N, long[] L) {
		Map<Long, CN> nm = new HashMap<>();
		for (long l : L) {
			if (!nm.containsKey(l)) {
				nm.put(l, new CN(0));
			}
			nm.get(l).n++;
		}
		Queue<CN> qu = new PriorityQueue<>(new Comparator<CN>() {
			@Override
			public int compare(CN o1, CN o2) {
				return o2.n - o1.n;
			}
		});
		qu.addAll(nm.values());

		int c = 0;
		while (qu.size() >= 3) {
			CN cn1 = qu.poll();
			CN cn2 = qu.poll();
			CN cn3 = qu.poll();
			cn1.n--;
			cn2.n--;
			cn3.n--;
			c++;
			if (cn1.n > 0) {
				qu.add(cn1);
			}
			if (cn2.n > 0) {
				qu.add(cn2);
			}
			if (cn3.n > 0) {
				qu.add(cn3);
			}
		}

		return c;
	}
}
