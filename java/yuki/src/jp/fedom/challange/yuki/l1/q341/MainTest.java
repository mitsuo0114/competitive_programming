package jp.fedom.challange.yuki.l1.q341;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		assertThat(Main.solve("……何でもないです。"), is(2));
	}

	@Test
	public void test2() {
		assertThat(Main.solve("………別に………"), is(3));
	}

	@Test
	public void test3() {
		assertThat(Main.solve("……………"), is(5));
	}

}
