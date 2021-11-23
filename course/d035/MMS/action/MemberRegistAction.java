package d035.MMS.action;

import java.util.Scanner;
import d035.MMS.svc.MemberRegistService;
import d035.MMS.util.ConsoleUtil;
import d035.MMS.vo.Member;

public class MemberRegistAction implements Action {
    @Override
    public void execute(Scanner scan) throws Exception {

        ConsoleUtil consoleUtil = new ConsoleUtil();
        Member newMember = consoleUtil.getNewMember(scan);
        MemberRegistService memberRegistService = new MemberRegistService();
        boolean registSuccess = memberRegistService.registMember(newMember);
        if (registSuccess) {
            consoleUtil.printRegistSuccessMessage(newMember.getId());
        } else {
            consoleUtil.printRegistFailMessage(newMember.getId());
        }
    }
}