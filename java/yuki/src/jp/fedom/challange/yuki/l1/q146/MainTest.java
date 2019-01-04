package jp.fedom.challange.yuki.l1.q146;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.math.BigInteger;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { 
				"2",
				"2 5", 
				"3 20",
				};

		for(String s : in){
			if(s.split(" ").length == 2){
			Main.solve(new BigInteger(s.split(" ")[0]), new BigInteger(s.split(" ")[1]));
			}
		}
		assertThat(Main.t, is(new BigInteger("45")));
	}
}
