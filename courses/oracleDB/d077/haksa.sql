------------------------as system
------------1
alter session set "_ORACLE_SCRIPT"= true;
create user HAKSA identified by 1234 default tablespace "USERS" temporary tablespace "TEMP";
grant connect, resource, dba to HAKSA;

------------------------as local-MOVIE
------------2
alter session set current_schema = HAKSA;
create table 학과
(
    번호 number        not null primary key,
    이름 nvarchar2(10) not null
);
create table 교수
(
    번호   number        not null primary key,
    이름   nvarchar2(10) not null,
    학과번호 number        not null,
    constraint FK_교수_학과번호 foreign key (학과번호) references 학과 (번호)
);
create table 학생
(
    번호   number        not null primary key,
    이름   nvarchar2(10) not null,
    주소   nvarchar2(50),
    학년   number,
    키    number,
    몸무게  number,
    상태   nvarchar2(4),
    입력일자 date,
    학과번호 number        not null,
    constraint FK_학생_학과번호 foreign key (학과번호) references 학과 (번호)
);
create table 과목
(
    번호   number        not null primary key,
    이름   nvarchar2(10) not null,
    학점   number,
    교수번호 number        not null,
    constraint FK_과목_교수번호 foreign key (교수번호) references 교수 (번호)
);
alter table 과목
    modify 이름 nvarchar2(11);

create table 수강내역
(
    학생번호 number not null,
    과목번호 number not null,
    점수   number(4, 1),
    등급   nvarchar2(1),
    constraint PK_수강내역 primary key (학생번호, 과목번호),
    constraint FK_수강내역_학생번호 foreign key (학생번호) references 학생 (번호),
    constraint FK_수강내역_과목번호 foreign key (과목번호) references 과목 (번호)
);
------------3
insert into 학과 values (1, '소프트웨어공학과');
insert into 학과 values (2, '컴퓨터공학과');
insert into 학과 values (3, '경영정보학과');
insert into 학과 values (4, '경영학과');
insert into 학과 values (5, '연극영화과');
insert into 학과 values (6, '철학과');

insert into 교수 values (1, '이해진', 1);
insert into 교수 values (2, '김정주', 1);
insert into 교수 values (3, '김이숙', 1);
insert into 교수 values (4, '이석호', 2);
insert into 교수 values (5, '김사부', 3);
insert into 교수 values (6, '장미희', 5);
insert into 교수 values (7, '백남영', 5);
insert into 교수 values (8, '김현이', 5);
insert into 교수 values (9, '이사부', 5);

insert into 과목 values (1, '데이터베이스관리', 3, 3);
--length error(11, expect 10)
insert into 과목 values (2, '데이터베이스프로그래밍', 3, 3);
insert into 과목 values (3, 'SQL활용', 3, 4);
insert into 과목 values (4, '데이터베이스', 4, 5);
insert into 과목 values (5, '인터넷마케팅', 3, 5);
insert into 과목 values (6, '연기실습', 2, 7);
insert into 과목 values (7, '영화제작실습', 2, 8);
insert into 과목 values (8, '영화마케팅', 1, 9);

insert into 학생
values (1, '김이향', '인천 남동구', 4, 166, 56, '재학', '2005-03-01', 5);
insert into 학생
values (6, '박지은', '서울 양천구', 2, 183, 65, '재학', '2015-02-14', 3);
insert into 학생
values (7, '안칠현', '서울 금천구', 1, 178, 65, '재학', '2016-02-19', 1);
insert into 학생
values (8, '김태희', '서울 구로구', 1, 165, 45, '재학', '2016-02-19', 3);
insert into 학생
values (9, '채영', '서울 구로구', 1, 172, 47, '재학', '2016-02-19', 2);
insert into 학생
values (11, '영란', '서울 강남구', 1, 162, 43, '재학', '2016-02-19', 5);
insert into 학생
values (12, '윤호', '서울 강남구', 1, 184, 66, '휴학', '2016-08-10', 1);
insert into 학생
values (13, '보아', '서울 구로구', 1, 162, 45, '재학', '2016-02-19', 1);
insert into 학생
values (14, '문근영', '서울 강남구', 1, 165, 45, '재학', '2016-02-19', 3);
insert into 학생
values (3, '이세영', '서울 구로구', 4, null, null, '재학', '2013-03-01', 4);
insert into 학생
values (4, '문주원', '경기 부천시', 3, null, null, '재학', '2014-02-13', 3);
insert into 학생
values (5, '성춘향', '서울 영등포구', 3, null, null, '재학', '2014-02-13', 5);
insert into 학생
values (10, '박수애', null, 1, 168, 46, '재학', '2016-02-19', 2);
insert into 학생
values (2, '박보검', '인천 부평구', 4, 168, null, '재학', '2010-03-01', 6);

insert into 수강내역 values (7, 1, 85, 'B');
insert into 수강내역 values (12, 1, 50, 'F');
insert into 수강내역 values (13, 1, 90, 'A');
insert into 수강내역 values (7, 2, 80, 'B');
insert into 수강내역 values (13, 2, 95, 'A');
insert into 수강내역 values (9, 3, 90, 'A');
insert into 수강내역 values (10, 3, 70, 'C');
insert into 수강내역 values (4, 4, 90, 'A');
insert into 수강내역 values (6, 4, 55, 'F');
insert into 수강내역 values (8, 4, 85, 'B');
insert into 수강내역 values (14, 4, 95, 'A');
insert into 수강내역 values (4, 5, 70, 'C');
insert into 수강내역 values (6, 5, 95, 'A');
insert into 수강내역 values (8, 5, 90, 'A');
insert into 수강내역 values (14, 5, 95, 'A');
insert into 수강내역 values (6, 8, 90, 'A');
insert into 수강내역 values (8, 8, 80, 'B');
insert into 수강내역 values (14, 8, 90, 'A');
insert into 수강내역 values (1, 6, 85, 'B');
insert into 수강내역 values (5, 6, 80, 'B');
insert into 수강내역 values (11, 6, 78.5, 'C');
insert into 수강내역 values (1, 7, 95, 'A');
insert into 수강내역 values (5, 7, 85, 'B');
insert into 수강내역 values (1, 8, 100, 'A');
commit;
------------4
------1
select *
from 학생
order by 번호;
------2
select 이름, 학년, 주소
from 학생
order by 학년 desc, 이름;
------3
select 이름 as 성명, 주소 as "현재 주소지"
from 학생;
------4
select distinct 학년
from 학생;
------5
select *
from 학생
where 번호 = 1;
------6
select *
from 학생
where 키 < 165;
------7
select 이름, 학년, 키, 몸무게
from 학생
where 학년 = 1
  and 키 >= 170;
------8
select 이름, 학년, 키, 몸무게
from 학생
where 학년 = 1
   or 키 >= 170;
------9
select 이름, 주소, 키, 몸무게
from 학생
where 몸무게 between 45 and 50;
------10
select 이름, 주소, 키, 몸무게
from 학생
where 몸무게 >= 45
  and 몸무게 <= 50;
------11
select 번호, 이름, 학년
from 학생
where 학년 in (2, 3);
------12
select 번호, 이름, 학년
from 학생
where 학년 = 2
   or 학년 = 3;
------13
select *
from 학생
where 이름 like '박%';
------14
select *
from 학생
where 이름 like '김%'
   or 이름 like '이%'
   or 이름 like '박%';
-- where regexp_like(이름, '^[김이박]');
------15
select *
from 학생
where 이름 like '김%'
union
select *
from 학생
where 이름 like '이%'
union
select *
from 학생
where 이름 like '박%';
------16
select 이름, 학년, 주소
from 학생
where 주소 is null;
------17
select 이름, 학년, 몸무게
from 학생
where 몸무게 is not null;
------18
select *
from 학생
order by 이름;
------19
select 이름, 주소, 키
from 학생
order by 키 desc nulls last;
------20
select 이름, 학년, 주소, 몸무게
from 학생
where 몸무게 is not null
order by 몸무게;
------21
select 이름, 학년, 키, 몸무게
from 학생
where 몸무게 is not null
  and 학년 = 1
order by 키 desc, 몸무게;
------22
select 번호, 이름, 주소
from 학생
order by 이름;
------23
select 이름, 키, 몸무게
from 학생
where 학년 = ( select 학년 from 학생 where 이름 = '문주원' );
------24
select 이름, 학년, 키
from 학생
where 키 < ( select avg(키) from 학생 where 학과번호 = 1 );
------25
select 이름, 학년, 키
from 학생
where 학년 = ( select 학년 from 학생 where 이름 = '김태희' )
  and 키 > ( select 키 from 학생 where 이름 = '김태희' );
------26
select 번호, 이름, 키
from 학생
where 키 = 165;
------27
select count(번호) as 학생수
from 학생;
------28
select count(번호) as "몸무게 정보 있는 학생의 수"
from 학생
where 이름 like '박%'
  and 몸무게 is not null;
------29
select avg(점수) as 평균점수
from 수강내역
where 과목번호 = 1;
------30
select 과목번호, avg(점수) as 과목평균점수
from 수강내역
group by 과목번호;
------31
select 학과번호, 학년, count(학년) as 인원, avg(키) as 평균키
from 학생
group by 학과번호, 학년
order by 학년;
------32
select 과목번호, count(과목번호) as 누적학생수, avg(점수) as 과목평균점수
from 수강내역
group by 과목번호
having count(과목번호) >= 4;
------33
select 과목번호, count(과목번호) as 누적학생수, avg(점수) as 과목평균점수
from 수강내역
group by 과목번호
having count(과목번호) >= 4
order by avg(점수) desc;
------34
select 학생.번호 as 번호, 학생.이름 as 이름, 학과.이름 as 이름
from 학생
         join 학과 on 학과번호 = 학과.번호
order by 학생.번호;
------35
select 교수.번호 as 번호, 교수.이름 as 이름, 학과.이름 as 이름
from 교수
         join 학과 on 학과번호 = 학과.번호
order by 교수.번호;
------36
select 학생.번호 as 번호, 학생.이름 as 이름, 학과.이름 as 이름
from 학생
         join 학과 on 학과번호 = 학과.번호
where 학생.이름 = '김이향';
------37
select 학생.번호 as 번호, 학생.이름 as 이름, 키, 학과.이름 as 이름
from 학생
         join 학과 on 학과번호 = 학과.번호
where 키 > 180;
------38
select 학과.이름 as 이름, 교수.이름 as 이름, 과목.이름 as 이름
from 학과
         join 교수 on 학과번호 = 학과.번호
         join 과목 on 교수.번호 = 과목.교수번호;
------39
select 학과.이름 as 이름, 과목.이름 as 이름
from 학과
         join 교수 on 학과번호 = 학과.번호
         join 과목 on 교수.번호 = 과목.교수번호;