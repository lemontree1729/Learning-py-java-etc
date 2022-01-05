create table indexTBL as
select first_name, last_name, hire_date
from HR.EMPLOYEES;

select *
from indexTBL
where first_name = 'Jack';

create index idx_indexTBL_firstname on indexTBL (first_name);

create view membertbl_view as
select membername, memberaddress
from membertbl;

create procedure myProc as
    var1 int;
    var2 int;
begin
    select count(*) into var1 from MEMBERTBL;
    select count(*) into var2 from PRODUCTTBL;
    dbms_output.PUT_LINE(var1 + var2);
end;

begin
    myProc();
end;

insert into membertbl
values ('Figure', '연아', '경기도 군포시 당정동');

select *
from membertbl;

select *
from deletedmembertbl;

delete
from MEMBERTBL
where memberid = 'Figure';

create table deletedMemberTBL
(
    memberid      char(8),
    membername    nchar(8),
    memberaddress nvarchar2(20),
    deleteddate   date
);

drop table deletedMemberTBL;

drop trigger trg_deletedMemberTBL;

create trigger trg_deletedMemberTBL
    after delete
    on MEMBERTBL
    for each row
begin
    insert into DELETEDMEMBERTBL values (:old.memberid, :old.membername, :old.memberaddress, sysdate);
end;

delete
from membertbl
where membername = '연아';

