package jp.fedom.challange.probook.p45;

public class Main {

	public static String solve(String s) {
		StringBuilder sb = new StringBuilder();
		StringBuilder ss = new StringBuilder(s);

		while (ss.length() > 0) {
			char f = ss.charAt(0);
			char e = ss.charAt(ss.length() - 1);
			if (f == e) {
				String revs = ss.reverse().toString();
				ss.reverse();

				if (ss.toString().compareTo(revs) < 0) {
					sb.append(f);
					ss = new StringBuilder(ss.substring(1, ss.length()));
				} else {
					sb.append(e);
					ss = new StringBuilder(ss.substring(0, ss.length() - 1));
				}
			} else if (f < e) {
				sb.append(f);
				ss = new StringBuilder(ss.substring(1, ss.length()));
			} else {
				sb.append(e);
				ss = new StringBuilder(ss.substring(0, ss.length() - 1));
			}
		}

		return sb.toString();
	}

}
