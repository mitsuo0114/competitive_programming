package jp.fedom.challange.yuki.l1.q304;

import org.junit.Test;

public class MainTest {
	@Test
	public void test() throws Exception {

		final String ans = "123";

		Main m = new Main() {
			String res;

			@Override
			protected void send(String s) {
				this.res = s.equals(ans) ? "unlocked" : "locked";
			}

			@Override
			protected String get() {
				// System.out.println(res);
				return res;
			}
		};
		m.solve();
	}
}
