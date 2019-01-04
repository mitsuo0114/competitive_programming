package jp.fedom.challange.probook.p34;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		List<Long> numbers = new ArrayList<Long>();
		long t = 13;
		String num = "1 2 4 7";

		numbers = toList(num);
		assertThat(Main.solve(numbers, t), is(true));
	}

	@Test
	public void test2() {
		List<Long> numbers = new ArrayList<Long>();
		long t = 15;
		String num = "1 2 4 7";

		numbers = toList(num);
		assertThat(Main.solve(numbers, t), is(false));
	}

	private List<Long> toList(String num) {
		List<Long> numbers = new ArrayList<Long>();
		String[] n = num.split(" ");
		for (int i = 0; i < n.length; i++) {
			numbers.add(Long.parseLong(n[i]));
		}
		return numbers;
	}

}
