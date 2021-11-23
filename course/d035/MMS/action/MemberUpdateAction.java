package d035.MMS.action;

import java.util.Scanner;
import d035.MMS.svc.MemberUpdateService;
import d035.MMS.util.ConsoleUtil;
import d035.MMS.vo.Member;

public class MemberUpdateAction implements Action {
    @Override
    public void execute(Scanner scan) {
        ConsoleUtil consoleUtil = new ConsoleUtil();
        int id = consoleUtil.getId("to change ", scan);
        MemberUpdateService memberUpdateService = new MemberUpdateService();
        Member oldMember = memberUpdateService.getOldMember(id);
        Member newMember = consoleUtil.getNewMember(oldMember, scan);
        boolean updateSuccess = memberUpdateService.updateMember(newMember);
        if (updateSuccess) {
            consoleUtil.printUpdateSuccessMessage(newMember.getId());
        } else {
        }
        consoleUtil.printUpdateFailMessage(newMember.getId());
    }

}