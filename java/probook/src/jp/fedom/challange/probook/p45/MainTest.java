package jp.fedom.challange.probook.p45;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		assertThat(Main.solve("ACDBCB"), is("ABCBCD"));
		assertThat(Main.solve("ACBDCB"), is("ABCBCD"));
	}

	@Test
	public void test2() {
		assertThat(Main.solve("KBCK"), is("KBCK"));
		assertThat(Main.solve("KCBK"), is("KBCK"));
	}

}
