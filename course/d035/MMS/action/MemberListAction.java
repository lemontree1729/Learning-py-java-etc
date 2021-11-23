package d035.MMS.action;

import java.util.Scanner;
import d035.MMS.svc.MemberListService;
import d035.MMS.util.ConsoleUtil;
import d035.MMS.vo.Member;

public class MemberListAction implements Action {
    @Override
    public void execute(Scanner scan) {
        ConsoleUtil consoleUtil = new ConsoleUtil();
        MemberListService memberListService = new MemberListService();
        Member[] memberArray = memberListService.getMemberArray();
        consoleUtil.printMemberList(memberArray);
    }
}
