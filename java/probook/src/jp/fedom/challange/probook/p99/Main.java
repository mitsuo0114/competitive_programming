package jp.fedom.challange.probook.p99;

public class Main {

	static int[] prev;
	
	public static int solve(int N, int[][] w, char s, char e) {
		int[] d = new int[N];
		prev = new int[N];
		boolean[] f = new boolean[N];
		int INF = Integer.MAX_VALUE - 1000;
		for (int i = 0; i < N; i++) {
			d[i] = INF;
			f[i] = false;
			prev[i] = i;
		}

		d[s - 'A'] = 0;

		while (true) {
			int v = -1;

			for (int i = 0; i < N; i++) {
				if (f[i] == false && (v == -1 || d[i] < d[v])) {
					v = i;
				}
			}
			if (v == -1) {
				break;
			}
			f[v] = true;

			System.out.println("update --");
			for (int i = 0; i < N; i++) {
				if (w[i][v] == 0 || f[i] == true) {
					continue;
				}
				if(d[v] + w[i][v] < d[i]){
					d[i] = d[v] + w[i][v];
					prev[i] = v;
				}
				
				System.out.println(Character.toString((char) (i + 'A')) + " = " + d[i]);
			}
			System.out.println("--");
		}
		return d[e - 'A'];
	}

	public static String path(char s, char e) {
		int i = e - 'A';
		StringBuilder sb = new StringBuilder();
		while(prev[i] != i){
			sb.insert(0, Character.toString((char) (i + 'A')));
			i = prev[i];
		}
		sb.insert(0, Character.toString((char) (i + 'A')));
		
		return sb.toString();
	}

}
