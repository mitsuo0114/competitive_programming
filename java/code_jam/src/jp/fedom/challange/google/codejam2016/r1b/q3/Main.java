package jp.fedom.challange.google.codejam2016.r1b.q3;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
	
	public static class Question {
		String[] f;
		String[] s;
		int size;
	}

	public static void main(String[] args) {
		String b = "res/2016_r1b_q3/";
		start(b + "test.in", b + "output_test.txt");
		start(b + "C-small-practice.in", b + "C_output_small.txt");
		// start(b + "C-large.in", b + "C_output_large.txt");
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
			int n = Integer.valueOf(s);
			q.size = n;
			q.f = new String[n];
			q.s = new String[n];
			for (int i = 0; i < n; i++) {
				s = b.readLine();
				q.f[i] = s.split(" ")[0];
				q.s[i] = s.split(" ")[1];
			}
			questionList.add(q);
		}
		b.close();
		return questionList;
	}

	public static String solve(Question q, int qNum) {
		Map<String, Integer> fcheck = new HashMap<>();
		Map<String, Integer> scheck = new HashMap<>();
		for (int i = 0; i < q.size; i++) {
			if (!fcheck.containsKey(q.f[i])) {
				fcheck.put(q.f[i], 0);
			}
			fcheck.put(q.f[i], fcheck.get(q.f[i]) + 1);

			if (!scheck.containsKey(q.s[i])) {
				scheck.put(q.s[i], 0);
			}
			scheck.put(q.s[i], scheck.get(q.s[i]) + 1);
		}
		List<String> subsets = fetchubset(q.size);
		int max = Integer.MIN_VALUE;
		for (String set : subsets) {
			List<String> fSet = filter(q.f, set);
			List<String> sSet = filter(q.s, set);
			Map<String, Integer> fc = new HashMap<>(fcheck);
			Map<String, Integer> sc = new HashMap<>(scheck);

			boolean success = true;
			for (int t = 0; t < fSet.size(); t++) {
				String fk = fSet.get(t);
				String sk = sSet.get(t);
				fc.put(fk, fc.get(fk) - 1);
				sc.put(sk, sc.get(sk) - 1);
				if (fc.get(fk) < 1 || sc.get(sk) < 1) {
					success = false;
					break;
				}
			}
			if (success) {
				max = Math.max(max, fSet.size());
			}

		}

		return "Case #" + qNum + ": " + max;
	}

	public static List<String> filter(String[] s, String set) {
		List<String> n = new ArrayList<>();
		for(int i = 0; i < set.length(); i++){
			if(set.charAt(i) == '1'){
				n.add(s[i]);
			}
		}
		return n;
	}

	public static List<String> fetchubset(int size) {
		List<String> n = new ArrayList<>();
		for(int i = 0; i < Math.pow(2, size); i++){
			n.add(String.format("%" + size + "s",Integer.toBinaryString(i)).replace(" ", "0"));
		}
		return n;
	}

}
