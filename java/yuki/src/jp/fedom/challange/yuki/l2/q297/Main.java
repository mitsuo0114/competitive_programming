package jp.fedom.challange.yuki.l2.q297;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		String[] c = new String[N];
		for (int i = 0; i < N; i++) {
			c[i] = sc.next();
		}
		sc.close();
		System.out.println(solve(N, c));
	}

	public static String solve(int N, String[] c) {
		PriorityQueue<Long> n = new PriorityQueue<>(new Comparator<Long>() {
			@Override
			public int compare(Long o1, Long o2) {
				return (int) (o2 - o1);
			};
		});
		PriorityQueue<Character> ex = new PriorityQueue<>(new Comparator<Character>() {
			@Override
			public int compare(Character o1, Character o2) {
				return o1 - o2;
			};
		});
		PriorityQueue<Character> nex = new PriorityQueue<>(new Comparator<Character>() {
			@Override
			public int compare(Character o1, Character o2) {
				return o2 - o1;
			};
		});
		boolean containMinus = false;
		for (String s : c) {
			if (s.equals("+") || s.equals("-")) {
				ex.add(s.charAt(0));
				containMinus |= s.charAt(0) == '-';
			} else {
				n.add(new Long(s));
			}
		}
		long max = 0;
		long min = 0;

		if (containMinus) {
			while (n.size() > ex.size()) {
				max *= 10;
				max += n.poll();
			}
			nex.addAll(ex);
			long absmax = max;
			PriorityQueue<Long> nc = new PriorityQueue<>(n);

			while (ex.size() > 0) {
				char ch = (char) ex.poll();
				if (ch == '-') {
					max -= n.poll();
				} else {
					max += n.poll();
				}
			}
			nc.add(absmax);
			nex.add('+');
			while (nex.size() > 0) {
				char ch = (char) nex.poll();
				if (ch == '-') {
					min -= nc.poll();
				} else {
					min += nc.poll();
				}
			}
		} else {
			PriorityQueue<Long> nn = new PriorityQueue<>(new Comparator<Long>() {
				@Override
				public int compare(Long o1, Long o2) {
					return (int) (o1 - o2);
				};
			});
			nn.addAll(n);

			while (n.size() > ex.size()) {
				max *= 10;
				max += n.poll();
			}
			while (n.size() > 0) {
				max += n.poll();
			}

			int m = ex.size() + 1;
			int[] mins = new int[m];
			int i = 0;
			while (nn.size() > 0) {
				mins[i % m] *= 10;
				mins[i % m] += nn.poll();
				i++;
			}

			for (int j = 0; j < mins.length; j++) {
				min += mins[j];
			}
		}

		return max + " " + min;
	}
}
