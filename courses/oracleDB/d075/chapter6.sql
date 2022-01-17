create or replace procedure userProc1(
    pi_userID in USERTBL.userID%type) as
    v_uName varchar(10);
begin
    select USERNAME into v_uName from USERTBL where USERID = pi_userid;
    DBMS_OUTPUT.PUT_LINE(v_uName);
end;
begin
    userProc1('JKW');
end;