package jp.fedom.challange.google.codejam2016.r1b.q2;

import java.util.List;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

import org.apache.commons.math3.ode.FirstOrderConverter;

import jp.fedom.challange.google.common.Utils;

public class Main {

	public static class Question {
		public String first;
		public String second;
	}

	public static void main(String[] args) {
		String b = "res/2016_r1b_q2/";
		start(b + "test.in", b + "output_test.txt");
		start(b + "B-small-practice.in", b + "B_output_small.txt");
		// start(b + "B-small-attempt1.in", b + "B_output_small.txt");
		// start(b + "B-large.in", b + "B_output_large.txt");
	}

	public static void start(String infile, String outputfile) {
		try {
			ArrayList<Question> questionList;
			questionList = getQuestions(infile);
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < questionList.size(); i++) {
				sb.append(solve2(questionList.get(i), i + 1)).append("\n");
			}
			System.out.println(sb.toString());
			File file = new File(outputfile);
			file.delete();
			FileWriter filewriter = new FileWriter(file, true);
			filewriter.write(sb.toString());
			filewriter.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public static ArrayList<Question> getQuestions(String filepath) throws IOException {
		ArrayList<Question> questionList = new ArrayList<>();

		FileReader f = new FileReader(filepath);
		BufferedReader b = new BufferedReader(f);
		String s;
		b.readLine();// cut header line
		while ((s = b.readLine()) != null) {
			Question q = new Question();
			q.first = s.split(" ")[0];
			q.second = s.split(" ")[1];
			questionList.add(q);
		}
		b.close();
		return questionList;
	}

	public static String solve2(Question q, int qNum) {
		Set<String> fCan = split(q.first);
		Set<String> sCan = split(q.second);

		String fans = "";
		String sans = "";
		int min = Integer.MAX_VALUE;
		int total = Integer.MAX_VALUE;
		for (String f : fCan) {
			for (String s : sCan) {
				int m = Math.abs(Integer.valueOf(f) - Integer.valueOf(s));
				int p = Integer.valueOf(f) + Integer.valueOf(s);
				if (m < min) {
					min = m;
					fans = f;
					sans = s;
					total = p;
				} else if (m == min) {
					if (p < total) {
						min = m;
						fans = f;
						sans = s;
						total = p;
					}
				}
			}
		}
		return "Case #" + qNum + ": " + fans + " " + sans;
	}

	public static Set<String> split(String s) {
		Set<String> n = new HashSet<>();
		if (s.contains("?")) {
			for (int i = 0; i < s.length(); i++) {
				char f = s.charAt(i);
				if (f == '?') {
					for (int j = 0; j <= 9; j++) {
						String ne = s.substring(0, i) + String.valueOf(j) + s.substring(i + 1, s.length());
						if (ne.contains("?")) {
							n.addAll(split(ne));
						} else {
							// System.out.println(ne);
							n.add(ne);
						}
					}
				}
			}
		} else {
			n.add(s);
		}
		return n;
	}

	public static String solve(Question q, int qNum) {

		StringBuffer firstAns = new StringBuffer();
		StringBuffer secondAns = new StringBuffer();

		return "Case #" + qNum + ": " + firstAns.toString() + " " + secondAns.toString();// +
	}

	private static int s2i(String string) {
		return Integer.parseInt(string);
	}
	private static String i2s(int i) {
		return String.valueOf(i);
	}

	private static void swap(String first, String second) {
		String tmp = first;
		first = second;
		second = tmp;
	}

	public static String fill(String string, int index, String s) {
		int l = string.length();
		
		StringBuffer sb = new StringBuffer(string);
		for (int k = index; k < l; k++) {
			if (string.charAt(k) == '?') {
				sb.append(s);
			} else {
				sb.append(string.charAt(k));
			}
		}
		return sb.toString();
	}

	private static void fillNine(StringBuffer firstAns, StringBuffer secondAns, int fi, int si, char f, char s) {
		if (fi > si) {
			firstAns.append(f == '?' ? "0" : String.valueOf(f));
			secondAns.append(s == '?' ? "9" : String.valueOf(s));
		} else {
			firstAns.append(f == '?' ? "9" : String.valueOf(f));
			secondAns.append(s == '?' ? "0" : String.valueOf(s));
		}
	}

	private static List<String> dp(String first, String second) {

		return null;
	}

}
