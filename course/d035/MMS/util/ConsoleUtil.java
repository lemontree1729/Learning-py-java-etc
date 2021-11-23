package d035.MMS.util;

import java.util.Scanner;
import d035.MMS.vo.Member;
import d035.MMS.vo.SearchData;

public class ConsoleUtil {
    public Member getNewMember(Scanner scan) {
        Member newMember = new Member();
        System.out.println("=====new member register=====");
        System.out.print("member id: ");
        int id = scan.nextInt();
        System.out.print("member name: ");
        String name = scan.next();
        System.out.print("member email: ");
        String email = scan.next();
        System.out.print("member address: ");
        String addr = scan.next();
        System.out.print("member hobby: ");
        String hobby = scan.next();
        System.out.print("member tel: ");
        String tel = scan.next();
        System.out.print("member age: ");
        int age = scan.nextInt();
        newMember.setId(id);
        newMember.setName(name);
        newMember.setEmail(email);
        newMember.setAddr(addr);
        newMember.setHobby(hobby);
        newMember.setTel(tel);
        newMember.setAge(age);
        return newMember;
    }

    public void printRegistSuccessMessage(int id) {
        System.out.println(id + " register success");
    }

    public void printRegistFailMessage(int id) {
        System.out.println(id + " register fail");
    }

    public void printMemberList(Member[] memberArray) {
        if (memberArray.length == 0)
            System.out.println("no added member info");
        else {
            for (int i = 0; i < memberArray.length; i++)
                System.out.println(memberArray[i]);
        }
    }

    public int getId(String msgKind, Scanner scan) {
        System.out.print(msgKind + "id: ");
        return scan.nextInt();
    }

    public Member getNewMember(Member oldMember, Scanner scan) {
        Member member = new Member();
        System.out.println("=====update member information=====");
        System.out.println("member id: " + oldMember.getId());
        System.out.println("name before: " + oldMember.getName());
        System.out.print("new name: ");
        String name = scan.next();
        System.out.println("email before: " + oldMember.getEmail());
        System.out.print("new email: ");
        String email = scan.next();
        System.out.println("address before: " + oldMember.getAddr());
        System.out.print("new address: ");
        String addr = scan.next();
        System.out.println("hobby before: " + oldMember.getHobby());
        System.out.print("new hobby: ");
        String hobby = scan.next();
        System.out.println("tel before: " + oldMember.getTel());
        System.out.print("new tel: ");
        String tel = scan.next();
        System.out.println("age before: " + oldMember.getAge());
        System.out.print("new age: ");
        int age = scan.nextInt();
        member.setId(oldMember.getId());
        member.setName(name);
        member.setEmail(email);
        member.setAddr(addr);
        member.setHobby(hobby);
        member.setTel(tel);
        member.setAge(age);
        return member;
    }

    public void printUpdateSuccessMessage(int id) {
        System.out.println(id + "update success");
    }

    public void printUpdateFailMessage(int id) {
        System.out.println(id + "update fail");
    }

    public void printDeleteSuccessMessage(int id) {
        System.out.println(id + "delete success");
    }

    public void printDeleteFailMessage(int id) {
        System.out.println(id + "delete fail");
    }

    public SearchData getSearchData(Scanner scan) {
        System.out.println("select to search");
        System.out.println("1. id");
        System.out.println("2. name");
        System.out.print("search condition: ");
        String searchCondition = scan.next();
        String searchValue = null;
        if (searchCondition.equals("id")) {
            System.out.print("id to search: ");
            searchValue = scan.next();
        } else if (searchCondition.equals("name")) {
            System.out.print("name to search: ");
            searchValue = scan.next();
        }
        SearchData searchData = new SearchData();
        searchData.setSearchCondition(searchCondition);
        searchData.setSearchValue(searchValue);
        return searchData;
    }

    public void printSearchMember(Member member) {
        if (member == null)
            System.out.println("no id result found");
        else {
            System.out.println("result for id " + member.getId());
            System.out.println(member);
        }
    }

    public void printSearchMemberArray(Member[] memberArray) {
        if (memberArray == null) {
            System.out.println("no name result found");
        } else {
            System.out.println("result for name ");
            for (int i = 0; i < memberArray.length; i++) {
                System.out.println(memberArray[i]);
            }
        }
    }
}