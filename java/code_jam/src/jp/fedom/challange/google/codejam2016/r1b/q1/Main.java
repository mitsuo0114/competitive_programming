package jp.fedom.challange.google.codejam2016.r1b.q1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import com.sun.corba.se.impl.encoding.OSFCodeSetRegistry.Entry;

import jp.fedom.challange.google.common.Utils;

public class Main {

	public static class Question {
		String s;
	}

	public static void main(String[] args) {
		String b = "res/2016_r1b_q1/";
		// start(b + "test.in", b + "output_test.txt");
		// start(b + "A-small-attempt1.in", b + "A_output_small.txt");
		start(b + "A-large-practice.in", b + "A_output_large.txt");
	}

	public static void start(String infile, String outputfile) {
		try {
			ArrayList<Question> questionList;
			questionList = getQuestions(infile);
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < questionList.size(); i++) {
				sb.append(solve(questionList.get(i), i + 1)).append("\n");
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
			q.s = s;
			questionList.add(q);
		}
		b.close();
		return questionList;
	}

	public static String solve(Question q, int qNum) {

		List<Integer> ans = new ArrayList<>();

		extract(q, ans, count(q.s, "W"), "TWO", 2);
		extract(q, ans, count(q.s, "X"), "SIX", 6);
		extract(q, ans, count(q.s, "Z"), "ZERO", 0);
		extract(q, ans, count(q.s, "U"), "FOUR", 4);
		extract(q, ans, count(q.s, "G"), "EIGHT", 8);
		extract(q, ans, count(q.s, "R"), "THREE", 3);
		extract(q, ans, count(q.s, "F"), "FIVE", 5);
		extract(q, ans, count(q.s, "V"), "SEVEN", 7);
		extract(q, ans, count(q.s, "I"), "NINE", 9);
		extract(q, ans, count(q.s, "O"), "ONE", 1);

		Collections.sort(ans);
		StringBuilder sb = new StringBuilder();
		for (Integer i : ans) {
			sb.append(String.valueOf(i));
		}

		return "Case #" + qNum + ": " + sb.toString();
	}

	private static void extract(Question q, List<Integer> ans,  int count, String s, int a) {
		for (int i = 0; i < count; i++) {
			ans.add(a);
			for (char ch : s.toCharArray()) {
				q.s = q.s.replaceFirst(String.valueOf(ch), "0");
			}
		}
	}

	private static int count(String s, String string) {
		Map<String, Integer> b = new HashMap<>();
		for (char ch : s.toCharArray()) {
			String k = String.valueOf(ch);
			if (!b.containsKey(String.valueOf(k))) {
				b.put(k, 0);
			}
			b.put(k, b.get(k) + 1);
		}
		return b.containsKey(string) ? b.get(string) : 0;
	}

}
