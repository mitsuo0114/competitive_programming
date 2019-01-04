package jp.fedom.challange.yuki.l2.q78;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		List<String> input = new ArrayList<>();
		while (sc.hasNext()) {
			input.add(sc.nextLine());
		}

		System.out.println(solve(input));

		sc.close();
	}

	public static long solve_slow(List<String> in) {
		int N = Integer.valueOf(in.get(0).split(" ")[0]);
		long K = Long.valueOf(in.get(0).split(" ")[1]);
		int[] ice = new int[N];
		int iceTotal = 0;
		for (int i = 0; i < in.get(1).length(); i++) {
			ice[i] = Integer.valueOf(in.get(1).substring(i, i + 1));
			iceTotal += ice[i];
		}

		long p = 0;
		int stock = 0;
		for (long i = 0; i < K; i++) {
			if (i == N) {
				if (iceTotal >= N) {
					break;
				}
			}

			if (stock == 0) {
				p++;
			} else {
				stock--;
			}

			int r = ice[(int) (i % N)];
			if (r != 0) {
				stock += r;
			}

		}

		return p;
	}

	public static long solve(List<String> in) {
		int N = Integer.valueOf(in.get(0).split(" ")[0]);
		long K = Long.valueOf(in.get(0).split(" ")[1]);
		int[] ice = new int[N];
		int iceTotal = 0;
		for (int i = 0; i < in.get(1).length(); i++) {
			ice[i] = Integer.valueOf(in.get(1).substring(i, i + 1));
			iceTotal += ice[i];
		}

		long p = 0;
		int stock = 0;
		for (long i = 0; i < K; i++) {
			if (i == N) {
				if (iceTotal >= N) {
					break;
				} else if (iceTotal < N) {
					int diff = N - iceTotal;
					// System.out.println(p + " " + i + " " + diff);
					if ((K / N) - 2 > 0) {
						long skip = (K / N) - 2;
						p += skip * diff;
						i += skip * N;
					}
					// System.out.println(p + " " + i);
				}
			}
			// System.out.println("pis " + p + " " + i + " " + stock);

			if (stock == 0) {
				p++;
			} else {
				stock--;
			}

			int r = ice[(int) (i % N)];
			if (r != 0) {
				stock += r;
			}

		}

		return p;
	}

}
