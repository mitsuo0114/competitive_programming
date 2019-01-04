package jp.fedom.challange.yuki.l1.q353;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		assertThat(Main.solve("5 2"), is("7"));
		assertThat(Main.solve("765 346"), is("1111"));
	}

}
