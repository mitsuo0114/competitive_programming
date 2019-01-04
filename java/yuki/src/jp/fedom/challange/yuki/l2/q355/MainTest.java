package jp.fedom.challange.yuki.l2.q355;

import org.junit.Test;

public class MainTest {
	@Test
	public void test() throws Exception {

		final char[] answer = { '6', '4', '3', '8' };

		Main m = new Main() {
			String res;

			@Override
			protected void send(String s) {
				// System.out.println(s);
				String[] sp = s.split(" ");
				int m1 = 0;
				int m2 = 0;

				for (int i = 0; i < 4; i++) {
					for (int j = 0; j < 4; j++) {
						if (sp[i].charAt(0) == answer[j]) {
							m2++;
						}
					}
				}
				for (int i = 0; i < 4; i++) {
					if (sp[i].charAt(0) == answer[i]) {
						m1++;
						m2--;
					}
				}
				this.res = m1 + " " + m2;
			}

			@Override
			protected String get() {
				// System.out.println(res);
				return res;
			}
		};
		m.solve();
	}

	// @Test
	// public void test1() {
	// int[] in = { 1,2,3,4 };
	//
	// List<int[]> r = Main.split(in);
	// for(int[] d : r){
	// System.out.println(d[0] + " " + d[1] + " " + d[2] + " " + d[3]);
	// }
	// }
}
