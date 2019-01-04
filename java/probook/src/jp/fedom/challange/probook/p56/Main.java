package jp.fedom.challange.probook.p56;

public class Main {

	public static int solve(String s, String t) {
		if (s.isEmpty() || t.isEmpty()) {
			return 0;
		}

		if (s.charAt(0) == t.charAt(0)) {
			return solve(s.substring(1), t.substring(1)) + 1;
		} else {
			return Math.max(solve(s, t.substring(1)), solve(s.substring(1), t));
		}
	}
}
