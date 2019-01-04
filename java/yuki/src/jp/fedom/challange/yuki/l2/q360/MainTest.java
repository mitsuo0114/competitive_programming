package jp.fedom.challange.yuki.l2.q360;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.List;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		int[] in = new int[] { 1, 2, 3, 4, 5, 6, 7 };
		assertThat(Main.solve(in), is("YES"));
	}

	@Test
	public void test2() {
		int[] in = new int[] { 1, 1, 1, 1, 1, 1, 1 };
		assertThat(Main.solve(in), is("NO"));
	}

	@Test
	public void test3() {
		int[] in = new int[] { 1, 2, 2, 3, 3, 4, 5 };
		assertThat(Main.solve(in), is("YES"));
	}

	@Test
	public void test_p() {
		List<Integer> t = new ArrayList<>();
		t.add(1);
		t.add(1);
		t.add(1);
		t.add(1);
		t.add(1);
		List<List<Integer>> ans = Main.getPermulation(t);
		System.out.println(ans.size());
	}

}
