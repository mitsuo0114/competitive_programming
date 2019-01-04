package jp.fedom.challange.google.codejam2015.r1b.q1;

import static org.hamcrest.CoreMatchers.instanceOf;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {

	public static long swap(long i){
		return Long.valueOf(new StringBuffer(String.valueOf(i)).reverse().toString());
	}
	
	public static String solve(long target, int qnum){
		long count = getSolve(target);
		return "Case #" + qnum + ": " + count;
		
	}
	
	public static long getSolve(long target){
		if(target < 10){
			return target;
		}
		long count = reachCount(digit(target));

		String str = String.valueOf(target);
		String left = left(str);
		String right = right(str);
		
		if(swap(Long.parseLong(left)) == 1){
			// 10001234 -> no need to swap
			return count + Long.parseLong(right);
		}
		
		if(swap(Long.parseLong(right)) == 0){
			// 12340000 -> left is bigger than 1. can not swap.
			return getSolve(target - 1) + 1 ;
		}
		
		//
		count += swap(Long.parseLong(left));
		count ++;
		count += Long.parseLong(right) - 1;
		
		return count;
	}


	public static String right(String str) {
		int l = str.length();
		return str.substring(l/2);
	}

	public static String left(String str) {
		int l = str.length();
		return str.substring(0, l/2);
	}

	public static long reachCount(int digit) {
		long ans = 0;
		if(digit == 1){
			return 1;
		}else if(digit == 2){
			return 10;
		}else{
			ans = reachCount(digit - 1);
			if(digit % 2 == 0){
				ans += Math.pow(10, digit / 2) - 1;
				ans += 1;
				ans += Math.pow(10, (digit - 1) / 2) - 1; 
			}else{
				ans += Math.pow(10, (digit - 1) / 2) - 1; 
				ans += 1; 
				ans += Math.pow(10, (digit - 1) / 2) - 1; 
			}
			return ans;
		}
	}

	private static int digit(long target) {
		return String.valueOf(target).length();
	}

	public static void main(String[] args) {
		start("res/2015_r1b_q1/test.in", "res/2015_r1b_q1/output_test.txt");
		start("res/2015_r1b_q1/A-small-practice.in", "res/2015_r1b_q1/output_small.txt");
		start("res/2015_r1b_q1/A-large-practice.in", "res/2015_r1b_q1/output_large.txt");
	}

	public static void start(String infile, String outputfile) {
		try {
			ArrayList<Long> questionList;
			questionList = getQuestions(infile);
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < questionList.size(); i++) {
				sb.append(solve(questionList.get(i), i + 1)).append("\n");
			}
			System.out.println(sb);
			File file = new File(outputfile);
			file.delete();
			FileWriter filewriter = new FileWriter(file, true);
			filewriter.write(sb.toString());
			filewriter.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static ArrayList<Long> getQuestions(String infile) throws IOException {
			ArrayList<Long> questionList = new ArrayList<Long>();

			FileReader f = new FileReader(infile);
			BufferedReader b = new BufferedReader(f);
			String s;
			b.readLine();// cut header line
			while ((s = b.readLine()) != null) {
				questionList.add(Long.valueOf(s));
			}
			b.close();
			return questionList;
	}

}
