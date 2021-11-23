package d035.MMS.action;

import java.util.Scanner;
import d035.MMS.svc.MemberSearchService;
import d035.MMS.util.ConsoleUtil;
import d035.MMS.vo.Member;
import d035.MMS.vo.SearchData;

public class MemberSearchAction implements Action {
    @Override
    public void execute(Scanner scan) {
        ConsoleUtil consoleUtil = new ConsoleUtil();
        SearchData searchData = consoleUtil.getSearchData(scan);
        MemberSearchService memberSearchService = new MemberSearchService();
        if (searchData.getSearchCondition().equals("id")) {
            Member member = memberSearchService.searchMemberById(searchData.getSearchValue());
            consoleUtil.printSearchMember(member);
        } else if (searchData.getSearchCondition().equals("name")) {
            Member[] memberArray = memberSearchService.searchMemberByName(searchData.getSearchValue());
            consoleUtil.printSearchMemberArray(memberArray);
        }
    }
}
