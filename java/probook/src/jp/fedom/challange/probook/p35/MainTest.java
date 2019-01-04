package jp.fedom.challange.probook.p35;

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
				"***",
	            "*W*",
		        "***"};

		assertThat(Main.solve(f), is(1));
	}

	@Test
	public void test2() {
		String[] f = new String[]{
				"***",
	            "*W*",
		        "*W*"};

		assertThat(Main.solve(f), is(1));
	}

	@Test
	public void test3() {
		String[] f = new String[]{
				"W*W",
	            "***",
		        "W*W"};

		assertThat(Main.solve(f), is(4));
	}

	@Test
	public void test3_2() {
		String[] f = new String[]{
				"W*W",
	            "*W*",
		        "W*W"};

		assertThat(Main.solve(f), is(1));
	}

	@Test
	public void test4() {
		String[] f = new String[]{
				"W.........WW.",
				".WWW......WWW",
				"...WW.....WW.",
				"..........WW.",
				"..W.......WW.",
				".W.W......WW.",
				"W.W.W......W.",
				".W.W.......W.",
				"..W........W."};

		assertThat(Main.solve(f), is(3));
	}


}
