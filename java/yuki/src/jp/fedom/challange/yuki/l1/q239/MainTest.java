package jp.fedom.challange.yuki.l1.q239;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "4", 
				"- nyanpass uissu ohayo", 
				"konbanwa - ohayo ohayo", 
				"ohayogozaimasu nyanpass - komachanyuuna", 
				"konnichiwa nyanpass komachanohayo -", };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(2));
	}

	@Test
	public void test2() {
		String[] in = { "3",
				"- nyanpass ohayo",
				"nyanpass - chicchakunaiyo",
				"nyanpass nyanpass -",
 };
		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(-1));

	}
	
	@Test
	public void test3() {
		String[] in = { "3",
				"- ohayo nyanpass",
				"nyanpass - ohayo",
				"nyanpass ohayo -",
 };
		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(1));

	}
	
	@Test
	public void test4() {
		String[] in = { "2",
				"- ohayo",
				"zukoo -",

 };
		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(-1));

	}
}