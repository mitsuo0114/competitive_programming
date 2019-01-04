package jp.fedom.challange.yuki.l1.q341;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String input;
		if (args.length == 0) {
			input = sc.nextLine();
		} else {
			input = args[0];
		}

		System.out.println(solve(input));

		sc.close();
	}

	public static int solve(String in) {
		int ans = 0;
		int c = 0;
		for(int i = 0; i < in.length(); i++){
			if(in.substring(i, i + 1).equals("c")){
				c++;
				ans = Math.max(c, ans);
			}else{
				c = 0;
			}
		}
		return ans;
	}
}
