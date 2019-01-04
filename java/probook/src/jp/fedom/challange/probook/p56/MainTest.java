package jp.fedom.challange.probook.p56;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;


public class MainTest {
	
	@Test
	public void test_simple1() {
		assertThat(Main.solve("a", "a"), is(1));
		assertThat(Main.solve("a", "b"), is(0));
		assertThat(Main.solve("abcdtrtrtrtr", "becd"), is(3));
		assertThat(Main.solve("babaefwecdtrtrtrtr", "becd"), is(4));
	}
	
}
