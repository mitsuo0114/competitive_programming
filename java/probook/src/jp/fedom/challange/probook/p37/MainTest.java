package jp.fedom.challange.probook.p37;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] f = new String[]{
				"SG"};

		assertThat(Main.solve(f), is(1));
	}

	@Test
	public void test2() {
		String[] f = new String[]{
		"S",
		"G"};

		assertThat(Main.solve(f), is(1));
	}

	@Test
	public void test3() {
		String[] f = new String[]{
				"S..",
	            "...",
		        "..G"};

		assertThat(Main.solve(f), is(4));
	}

	@Test
	public void test4() {
		String[] f = new String[]{
				"..S",
	            "...",
		        "G.."};

		assertThat(Main.solve(f), is(4));
	}

	@Test
	public void test5() {
		String[] f = new String[]{
				"#S######.#",
				"......#..#",
				".#.##.##.#",
				".#........",
				"##.##.####",
				"....#....#",
				".#######.#",
				"....#.....",
				".####.###.",
				"....#...G#"};
		

		assertThat(Main.solve(f), is(22));
	}


}
