package jp.fedom.challange.probook.p34;

import java.util.List;


public class Main {

	public static boolean solve(List<Long> numbers, long target) {
		if (numbers.isEmpty()) {
			return false;
		}

		for (long l : numbers) {
			if (l == target) {
				return true;
			}
		}
		List<Long> sub = numbers.subList(1, numbers.size());

		return solve(sub, target) || solve(sub, target - numbers.get(0));
	}
}
