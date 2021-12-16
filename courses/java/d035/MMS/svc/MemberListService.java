package d035.MMS.svc;

import d035.MMS.ui.MemberUI;
import d035.MMS.vo.Member;

public class MemberListService {
    public Member[] getMemberArray() {
        return MemberUI.memberArray;
    }
}
