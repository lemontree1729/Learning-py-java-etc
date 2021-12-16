package d035.MMS.ui;

import java.util.Scanner;

import d035.MMS.action.Action;
import d035.MMS.action.MemberDeleteAction;
import d035.MMS.action.MemberListAction;
import d035.MMS.action.MemberUpdateAction;
import d035.MMS.action.MemberRegistAction;
import d035.MMS.action.MemberSearchAction;
import d035.MMS.controller.MemberController;
import d035.MMS.vo.Member;

public class MemberUI {
    public static Member[] memberArray = new Member[0];

    public static void main(String[] args) {
        MemberController memberController = new MemberController();
        boolean stop = false;
        Scanner sc = new Scanner(System.in);
        Action action = null;
        int menu = 0;
        do {
            System.out.println("=====member data=====");
            System.out.println("1. member register");
            System.out.println("2. member list");
            System.out.println("3. member update");
            System.out.println("4. member delete");
            System.out.println("5. member search");
            System.out.println("6. exit program");
            System.out.print("menu num : ");
            menu = sc.nextInt();
            switch (menu) {
            case 1:
                action = new MemberRegistAction();
                break;
            case 2:
                action = new MemberListAction();
                break;
            case 3:
                action = new MemberUpdateAction();
                break;
            case 4:
                action = new MemberDeleteAction();
                break;
            case 5:
                action = new MemberSearchAction();
                break;
            case 6:
                stop = true;
                System.out.println("program exit");
                break;
            default:
                break;
            }
            if (action != null)
                memberController.processRequest(sc, action);
        } while (!stop);
    }
}
