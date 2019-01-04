package jp.fedom.challange.google.codejam2013.r1b.q1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import jp.fedom.challange.google.common.Utils;

public class MainExecute {

	public static void main(String[] args) {
//		start("res/2013_r1b_q1/test.in", "res/2013_r1b_q1/output_test.txt");
		start("res/2013_r1b_q1/A-small-practice.in", "res/2013_r1b_q1/output_small.txt");
//		start("res/2013_r1b_q1/A-large-practice.in", "res/2013_r1b_q1/output_large.txt");
	}
	
	public static class Question{
		long a;
		int n;
		List<Long> motes = new ArrayList<>();
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

	public static ArrayList<Question> getQuestions(String filepath)
			throws IOException {
		ArrayList<Question> questionList = new ArrayList<>();

		FileReader f = new FileReader(filepath);
		BufferedReader b = new BufferedReader(f);
		String s;
		b.readLine();// cut header line
		while ((s = b.readLine()) != null) {
			Question q = new Question();
			q.a = Long.parseLong(s.split(" ")[0]);
			q.n = Integer.parseInt(s.split(" ")[1]);
			String[] l = b.readLine().split(" ");
			List<Long> ll = new ArrayList<>();
			for(String ss : l){
				ll.add(Long.parseLong(ss));
			}
			q.motes.addAll(ll);
			questionList.add(q);
		}
		b.close();
		return questionList;
	}

	public static String solve(Question q, int qnum) {

		Collections.sort(q.motes);
		
		int ans = solve(q);
		if(q.motes.size() != q.n){
			System.err.println("the question is not match.");
			return "ERR";
		}
		
		return "Case #" + qnum + ": "+ String.valueOf(ans);
	}

	public static int solve(Question q){
		int ans = 0;
		long size = q.a;
		int takencount = 0; 
		int[] taken = new int[q.n];
		
		for (int nn = 0; nn < 1000; nn++) {
			boolean sizeChange = false;
			for (int i = 0; i < q.n; i++) {
				if (q.motes.get(i) < size
					&& taken[i] == 0) {
					size += q.motes.get(i);
					taken[i] = -1;
					takencount++;
					sizeChange = true;
				} else {
					break;
				}
			}
			if (takencount == taken.length) {
				// 全部終わった
				break;
			}

			if (sizeChange) {
				// 大きくなる余地あり
				continue;
			}
			
				// ごろごろしても大きくならない
				int remain = q.n - takencount;
				if (size == 1) {
					// どうがんばっても大きくできない
					ans = q.motes.size();
					break;
				}else if (remain == 1) {
					// 残りひとつしかないなら削ったほうが確実によい
					ans += 1;
					break;
				}else{
					// この壁を登った場合と上らなかった場合を比べる
					int unCrime = remain;
					long targetSize = q.motes.get(takencount);
					int c = 0;
					long newSize = size;
					
					while(targetSize > newSize){
						c++;
						newSize = newSize + (newSize - 1);
					}
					
					if(unCrime < c){
						ans = unCrime;
						break;
					}
					
					Question qq = new Question();
					ans += 1;
					qq.a = newSize;
					qq.motes = q.motes.subList(takencount, q.n);
					qq.n = qq.motes.size();
					c = solve(qq);
					ans += Math.min(c, unCrime);
					break;
				}
		}
		System.out.println(ans);
		return ans;
	}
	
	private static Set<String> pickup(long dd) {
		String dString = String.valueOf(dd);
		Set<String> set = new HashSet<String>();
		for(int i = 0; i < dString.length(); i++){
			set.add(String.valueOf(dString.charAt(i)));
		}
		return set;
	}

	private static void out(double q) {
		System.out.print(q);
	}

}
