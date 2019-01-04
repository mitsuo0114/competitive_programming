package jp.fedom.challange.probook.p25;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

import org.hamcrest.Matcher;

public class Main {

	public static boolean solve(List<Long> numbers, long target) {
		for(long l1 : numbers){
			for(long l2 : numbers){
				for(long l3 : numbers){
					for(long l4 : numbers){
						if(l1 + l2 + l3 + l4 == target){
							return true;
						}
					}
				}
			}
		}
		return false;
	}

	public static boolean solve2(List<Long> numbers, long target) {
		Collections.sort(numbers);
		for(long l1 : numbers){
			for(long l2 : numbers){
				for(long l3 : numbers){
						long f = target - l1 - l2 - l3;
						if(Collections.binarySearch(numbers, f) >= 0){
							return true;
						}
				}
			}
		}
		return false;
	}
	
	public static boolean solve3(List<Long> numbers, long target) {
		Collections.sort(numbers);
		List<Long> inNumbers = new ArrayList<Long>();
		for (long l1 : numbers) {
			for (long l2 : numbers) {
				inNumbers.add(l1 + l2);
			}
		}
		Collections.sort(inNumbers);
		for (long l1 : numbers) {
			for (long l2 : numbers) {
				long f = target - l1 - l2;
				if (Collections.binarySearch(inNumbers, f) >= 0) {
					return true;
				}
			}
		}
		return false;
	}
	
}
