package jp.fedom.challange.yuki.l2.q342;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "�C�����ɂ����͂Ȃ邗��" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("���͂Ȃ�"));
	}

	@Test
	public void test1_() {
		String[] in = { "���͂�����������������������" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("����" + System.lineSeparator() + "����"));
	}

	@Test
	public void test1__() {
		String[] in = { "��������Ȃ���" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("�����"));
	}

}