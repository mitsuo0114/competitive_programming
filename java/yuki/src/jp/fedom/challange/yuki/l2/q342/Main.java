package jp.fedom.challange.yuki.l2.q342;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		List<String> input = new ArrayList<>();
		while (sc.hasNext()) {
			input.add(sc.nextLine());
		}

		System.out.println(solve(input));

		sc.close();
	}

	public static String solve(List<String> in) {
		String S = in.get(0);
		Pattern p = Pattern.compile("([^‚—]+)(‚—+)");
		Matcher m = p.matcher(S);

		StringBuilder sb = new StringBuilder();
		String d = System.lineSeparator();
		int max = 0;
		
		while (m.find()) {
			if (m.groupCount() == 2) {
				if (max == m.group(0).length() - m.group(1).length()) {
					sb.append(m.group(1)).append(d);
				} else if (max < m.group(0).length() - m.group(1).length()) {
					sb = new StringBuilder();
					sb.append(m.group(1)).append(d);
					max = m.group(0).length() - m.group(1).length();
				}
			}
		}

		return sb.toString().trim();
	}

}
