package jp.fedom.challange.yuki.l2.q120;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test_main() {
		String[] args = new String[1];
		StringBuffer sb = new StringBuffer();
		String d = System.lineSeparator();
		sb.append("4").append(d);
		sb.append("8").append(d);
		sb.append("2 2 5 8 7 3 8 8").append(d);
		sb.append("3").append(d);
		sb.append("1 1 1").append(d);
		sb.append("6").append(d);
		sb.append("1 1 2 2 2 3").append(d);
		sb.append("15").append(d);
		sb.append("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15");

		args[0] = sb.toString();

		Main.main(args);
	}

	@Test
	public void test() {
		assertThat(Main.solve(3, new long[] { 1, 2, 3 }), is(1));
		assertThat(Main.solve(7, new long[] { 7, 3, 4, 7, 1, 3, 9 }), is(2));
		assertThat(Main.solve(2, new long[] { 1, 1 }), is(0));
		assertThat(Main.solve(1, new long[] { 3 }), is(0));
		assertThat(Main.solve(2, new long[] { 10, 20 }), is(0));
		assertThat(Main.solve(8, new long[] { 2, 2, 5, 8, 7, 3, 8, 8 }), is(2));
		assertThat(Main.solve(8, new long[] { 2, 2, 5, 8, 7, 3, 8, 8 }), is(2));
		assertThat(Main.solve(3, new long[] { 1, 1, 1 }), is(0));
		assertThat(Main.solve(6, new long[] { 1, 1, 2, 2, 2, 3 }), is(1));
		assertThat(Main.solve(15, new long[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 }), is(5));
	}

	@Test
	public void test1() {
		assertThat(Main.solve(3, new long[] { 1, 10000000, 1000000000 }), is(1));
		assertThat(Main.solve(17, new long[] { 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3 }), is(5));

		assertThat(Main.solve(100,
				new long[] { 879994055, 395365356, 438468960, 692409451, 879994055, 438468960, 449258913, 395365356,
						872289258, 692409451, 395365356, 449258913, 98984499, 879994055, 102509450, 879994055,
						438468960, 438468960, 438468960, 378428819, 652125080, 319480293, 395365356, 438468960,
						879994055, 438468960, 432192605, 85004789, 395365356, 879994055, 257732118, 395365356,
						449258913, 395365356, 395365356, 449258913, 361915203, 879994055, 438468960, 692409451,
						907628951, 340127040, 652125080, 692409451, 438468960, 409906894, 395365356, 438468960,
						395365356, 980568169, 664285675, 556946205, 432192605, 395365356, 68778038, 395365356,
						692409451, 395365356, 921977763, 319480293, 879994055, 395365356, 432192605, 395365356,
						554784914, 378428819, 692409451, 207382139, 606267912, 858511101, 395365356, 333259743,
						879994055, 879994055, 395365356, 927837655, 438468960, 692409451, 319480293, 395365356,
						877067524, 606267912, 843851883, 507551214, 591490540, 395365356, 438468960, 626261931,
						395365356, 438468960, 438468960, 449258913, 31993829, 395365356, 438468960, 395365356,
						319480293, 879994055, 395365356, 664285675 }),
				is(33));
	}

}
