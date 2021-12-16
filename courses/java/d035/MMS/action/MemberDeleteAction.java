package d035.MMS.action;

import java.util.Scanner;
import d035.MMS.svc.MemberDeleteService;
import d035.MMS.util.ConsoleUtil;

public class MemberDeleteAction implements Action {
    ConsoleUtil consoleUtil = new ConsoleUtil();

    @Override
    public void execute(Scanner scan) throws Exception {
        int id = consoleUtil.getId("to delete ", scan);
        MemberDeleteService memberDeleteService = new MemberDeleteService();
        boolean deleteSuccess = memberDeleteService.deleteMember(id);
        if (deleteSuccess)
            consoleUtil.printDeleteSuccessMessage(id);
        else
            consoleUtil.printDeleteFailMessage(id);
    }
}