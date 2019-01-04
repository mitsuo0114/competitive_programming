package jp.fedom.challange.probook.p23;

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
		long l = 10;
		long n = 3;
		String num = "2 6 7";

		numbers = toList(num);
		assertThat(Main.solve(numbers, l, n), is("4 8"));
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
