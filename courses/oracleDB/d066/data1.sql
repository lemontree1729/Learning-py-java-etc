-----------------------------------------------
-- 고객 테이블
-----------------------------------------------
create table TB_CUSTOMER
(
    CUSTOMER_CD  CHAR(7) primary key,
    CUSTOMER_NM  NVARCHAR2(10) not null,
    MW_FLG       CHAR(1)       not null,
    BIRTH_DAY    CHAR(8)       not null,
    PHONE_NUMBER VARCHAR2(16),
    EMAIL        VARCHAR2(20),
    TOTAL_POINT  NUMBER(10),
    REG_DTTM     CHAR(14)
);
-----------------------------------------------
--추가 고객 테이블
-----------------------------------------------
create table TB_ADD_CUSTOMER
(
    customer_cd  char(7) primary key,
    customer_NM  varchar(10) not null,
    MW_FLG       CHAR(1)     not null,
    BIRTH_DAY    CHAR(8)     not null,
    PHONE_NUMBER VARCHAR2(16)
);
-------------------------------------------------
--포인트 테이블
-------------------------------------------------
create table TB_POINT
(
    CUSTOMER_CD CHAR(7)    not null,
    SEQ_NO      NUMBER(10) not null,
    POINT_MEMO  VARCHAR2(50),
    POINT       NUMBER(10),
    REG_DTTM    CHAR(14)
);
create unique index PK_TB_POINT on TB_POINT (CUSTOMER_CD, SEQ_NO);
alter table TB_POINT
    add (constraint PK_TB_POINT primary key (CUSTOMER_CD, SEQ_NO));
-----------------------------------------------
--2017년 포인트 테이블
-----------------------------------------------
create table TB_POINT_2017
(
    CUSTOMER_CD CHAR(7)    not null,
    SEQ_NO      NUMBER(10) not null,
    POINT_MEMO  VARCHAR2(50),
    POINT       NUMbER(10),
    REG_DTTM    CHAR(14)
);
create unique index PK_TB_POINT_2017 on TB_POINT_2017 (CUSTOMER_CD, SEQ_NO);
alter table TB_POINT_2017
    add (constraint PK_TB_POINT_2017 primary key (CUSTOMER_CD, SEQ_NO));
--------------------------------------------------
--2018년 포인트 테이블
--------------------------------------------------
create table TB_POINT_2018
(
    CUSTOMER_CD CHAR(7)    not null,
    SEQ_NO      NUMBER(10) not null,
    POINT_MEMO  VARCHAR2(50),
    POINT       NUMBER(10),
    REG_DTTM    CHAR(14)
);
create unique index PK_TB_POINT_2018 on TB_POINT_2018 (CUSTOMER_CD, SEQ_NO);
alter table TB_POINT_2018
    add (constraint PK_TB_POINT_2018 primary key (CUSTOMER_CD, SEQ_NO));

--------------------------------------------------
--2019년 포인트 테이블
--------------------------------------------------

create table TB_POINT_2019
(
    CUSTOMER_CD CHAR(7)    not null,
    SEQ_NO      NUMBER(10) not null,
    POINT_MEMO  VARCHAR2(50),
    POINT       NUMBER(10),
    REG_DTTM    CHAR(14)
);

create unique index PK_TB_POINT_2019 on TB_POINT_2019 (CUSTOMER_CD, SEQ_NO);
alter table TB_POINT_2019
    add (constraint PK_TB_POINT_2019 primary key (CUSTOMER_CD, SEQ_NO));

-----------------------------------------------
--기타정보 테이블
-----------------------------------------------
create table TB_ETC_INFO
(
    CUSTOMER_CD     CHAR(7) primary key,
    CUSTOMER_ENG_NM VARCHAR2(20),
    ITEM_LIST       VARCHAR2(40)
);
-----------------------------------------------
--품목정보 테이블
-----------------------------------------------
create table TB_ITEM_INFO
(
    ITEM_CD CHAR(7) primary key,
    ITEM_NM VARCHAR2(20)
);
-----------------------------------------------
--성적 테이블
-----------------------------------------------
create table TB_GRADE
(
    CLASS_CD   CHAR(1)       not null,
    STUDENT_NO NUMBER(2)     not null,
    STUDENT_NM NVARCHAR2(10) not null,
    KOR        NUMBER(3),
    ENG        NUMBER(3),
    MAT        NUMBER(3),
    TOT        NUMBER(3),
    AVG        NUMBER(5, 1)
);
create unique index PK_TB_GRADE on TB_GRADE (CLASS_CD, STUDENT_NO);
alter table TB_GRADE
    add (constraint PK_TB_GRADE primary key (CLASS_CD, STUDENT_NO));
-----------------------------------------------
--8월 성적 테이블
-----------------------------------------------
create table TB_GRADE_08
(
    TEST_CD CHAR(3) primary key,
    KOR     NUMBER(3),
    ENG     NUMBER(3),
    MAT     NUMBER(3)
);
-----------------------------------------------
--7월 성적 테이블
-----------------------------------------------
create table TB_GRADE_07
(
    TEST_CD CHAR(3) primary key,
    KOR     NUMBER(3),
    ENG     NUMBER(3),
    MAT     NUMBER(3)
);
-----------------------------------------------
--9월 성적 테이블
-----------------------------------------------
create table TB_GRADE_09
(
    TEST_CD CHAR(3) primary key,
    KOR     NUMBER(3),
    ENG     NUMBER(3),
    MAT     NUMBER(3)
);
-----------------------------------------------
--2020년 성적 테이블
-----------------------------------------------
create table TB_GRADE_2020
(
    TEST_MONTH CHAR(2) primary key,
    TEST_CD    CHAR(3) not null,
    KOR        NUMBER(3),
    ENG        NUMBER(3),
    MAT        NUMBER(3)
);
-----------------------------------------------
--반 정보 테이블
-----------------------------------------------
create table TB_CLASS_INFO
(
    CLASS_CD CHAR(1)      not null,
    CLASS_NM VARCHAR2(20) not null
);
create unique index PK_TB_CLASS_INFO on TB_CLASS_INFO (CLASS_CD, CLASS_NM);
alter table TB_CLASS_INFO
    add (constraint PK_TB_CLASS_INFO primary key (CLASS_CD, CLASS_NM));
-----------------------------------------------
--판매 테이블
-----------------------------------------------
create table TB_SALES
(
    SALES_DT    CHAR(8)   not null,
    SEQ_NO      NUMBER(5) not null,
    PRODUCT_NM  VARCHAR2(20),
    PRICE       NUMBER(10),
    SALES_COUNT NUMBER(3)
);
create unique index pk_tb_sales on tb_sales (sales_dt, seq_no);
alter table tb_sales
    add (constraint pk_tb_sales primary key (sales_dt, seq_no));
-----------------------------------------------
--9월 판매 테이블
-----------------------------------------------
create table TB_SALES_09
(
    SEQ_NO      NUMBER(10) primary key,
    PRODUCT_NM  VARCHAR2(20),
    CUSTOMER_CD CHAR(7),
    SALES_COUNT NUMBER(3)
);
-----------------------------------------------
--열차시각표 테이블
-----------------------------------------------
create table TB_TRAIN_TM
(
    TRAIN_NO   CHAR(5)   not null,
    RUN_ORDR   NUMBER(5) not null,
    STATION_NM VARCHAR2(20),
    ARV_TM     CHAR(6),
    DPT_TM     CHAR(6)
);
create unique index PK_TB_TRAIN_TM on TB_TRAIN_TM (TRAIN_NO, RUN_ORDR);
alter table TB_TRAIN_TM
    add (constraint PK_TB_TRAIN_TM primary key (TRAIN_NO, RUN_ORDR));
-----------------------------------------------
--포인트 정보 테이블 (연간정보, 프로시저로 등록/삭제)
-----------------------------------------------
create table TB_POINT_INFO
(
    YEAR          CHAR(4)    not null,
    RANK          NUMBER(10) not null,
    CUSTOMER_CD   CHAR(7)    not null,
    POINT         CHAR(7),
    LAST_POINT_DT CHAR(8)
);
create unique index PK_TB_POINT_INFO on TB_POINT_INFO (YEAR, RANK);
alter table TB_POINT_INFO
    add (constraint PK_TB_POINT_INFO primary key (YEAR, RANK));
-------------------------------------------
--고객 테이블
-------------------------------------------
insert into TB_CUSTOMER
values ('2017042', '강원진', 'M', '19810603', '002-8202-8790', 'wjang@navi.con', 280300, '20170123132432');
insert into TB_CUSTOMER
values ('2017053', '나경숙', 'W', '19891225', '002-4509-0043', 'ksna#boram.co.kr', 4500, '20170210180930');
insert into TB_CUSTOMER
values ('2017108', '박승대', 'M', '19711430', '', 'sdpark@haso.com', 23450, '2017050823450');
insert into TB_CUSTOMER
values ('2018087', '서유리', 'W', '19810925', '003-1265-8372', 'urseo@epnt.co.kr', 18700, '20180204160903');
insert into TB_CUSTOMER
values ('2018254', '이혜옥', 'W', '19839012', '003-1287-9734', 'hylee@hansoft.com', 570, '20180619230805');
insert into TB_CUSTOMER
values ('2019001', '김진숙', 'W', '20010426', '002-9842-0074', 'jskim$dreami.org', 12820, '20190101080518');
insert into TB_CUSTOMER
values ('2019069', '김한길', 'M', '1992315', '', 'hkkim@ssoya.com', 15320, '20190217110704');
insert into TB_CUSTOMER
values ('2019095', '남궁소망', 'M', '19620728', '003-6273-8539', '', 890, '20190312124558');
insert into TB_CUSTOMER
values ('2019167', '한찬희', 'M', '19711106', '002-1202-5563', 'chhan@ecom.co.kr', 6800, '20190508155600');
insert into TB_CUSTOMER
values ('2019281', '이아름', 'W', '19940513', '003-2620-0723', 'aulee@hoki.com', 35600, '20190709201308');
--------------------------------------------
--추가 고객 테이블
--------------------------------------------
insert into TB_ADD_CUSTOMER
values ('2017108', '박승대', 'M', '19711430', '002-2580-9919');
insert into TB_ADD_CUSTOMER
values ('2019302', '전미래', 'W', '19740812', '002-8864-0232');
------------------------------------------------
--포인트 테이블
------------------------------------------------
insert into TB_POINT
values ('2017042', 1, '청소기 구매 포인트 적립', 120700, '20181221160803');
insert into TB_POINT
values ('2017042', 2, '이벤트 포인트 적립', 9500, '20190405121520');
insert into TB_POINT
values ('2017042', 3, '냉장고 구매 포인트 적립', 78560, '20190612220810');
insert into TB_POINT
values ('2017042', 4, '에어컨 구매 포인트 적립', 71540, '20190703140913');
insert into TB_POINT
values ('2017053', 1, '세탁기 구매 포인트 적립', 3500, '20170410201432');
insert into TB_POINT
values ('2017053', 2, '드라이기 구매 포인트 적립', 2000, '20181216171040');
insert into TB_POINT
values ('2017108', 1, '청소기 구매 포인트 적립', 14065, '20180412205434');
insert into TB_POINT
values ('2017108', 2, '이벤트 포인트 적립', 9385, '20180702232143');
insert into TB_POINT
values ('2018087', 1, '이벤트 포인트 적립', 7800, '20180421161903');
insert into TB_POINT
values ('2018087', 2, '냉장고 구매 포인트 적립', 10900, '20181112161956');
insert into TB_POINT
values ('2018254', 1, '등록 포인트 적립', 500, '20180619230805');
insert into TB_POINT
values ('2018254', 2, '이벤트 포인트 적립', 70, '20180623170212');
insert into TB_POINT
values ('2019001', 1, '등록 포인트 적립', 500, '20190102120720');
insert into TB_POINT
values ('2019001', 2, '믹성기 구매 포인트 적립', 4600, '20190405134554');
insert into TB_POINT
values ('2019001', 3, '드라이기 구매 포인트 적립', 7820, '20190829071234');
insert into TB_POINT
values ('2019069', 1, '이벤트 포인트 적립', 8900, '20190219120712');
insert into TB_POINT
values ('2019069', 2, '면도기 구매 포인트 적립', 3200, '20190420090820');
insert into TB_POINT
values ('2019069', 3, '전기밥솥 구매 포인트 적립', 3220, '20190620071230');
insert into TB_POINT
values ('2019095', 1, '등록 포인트 적립', 500, '2019031212456');
insert into TB_POINT
values ('2019095', 2, '이벤트 포인트 적립', 390, '20190510072345');
insert into TB_POINT
values ('2019167', 1, '드라이기 구매 포인트 적립', 3200, '20190612042450');
insert into TB_POINT
values ('2019167', 2, '전기밥솥 구매 포인트 적립', 3600, '20190714133422');
insert into TB_POINT
values ('2019281', 1, '등록 포인트 적립', 500, '20190709201308');
insert into TB_POINT
values ('2019281', 2, '청소기 구매 포인트 적립', 8950, '20190710200921');
insert into TB_POINT
values ('2019281', 3, '냉장고 구매포인트 적립', 12200, '20190712082334');
insert into TB_POINT
values ('2019281', 4, '드라이기 구매 포인트 적립', 7600, '20190721134421');
insert into TB_POINT
values ('2019281', 5, '믹서기 구매 포인트 적립', 6250, '20190724022430');
-----------------------------------------------
--기타정보 테이블
-----------------------------------------------
insert into TB_ETC_INFO
values ('2017042', 'Gang won jin', 'S01,S05,S06,S09');
insert into TB_ETC_INFO
values ('2017053', 'Na kyoung suk', 'S02,S03,S07');
insert into TB_ETC_INFO
values ('2017108', 'park seung dea', 'S05,S06,S08');
insert into TB_ETC_INFO
values ('2018087', 'seo you ri', 'S03,S06');
insert into TB_ETC_INFO
values ('2018254', 'lee hye ok', 'S08');
insert into TB_ETC_INFO
values ('2019001', 'kim jun suk', 'S01,S05,S07');
insert into TB_ETC_INFO
values ('2019069', 'KIM JAN KIL', 'S03,S06,S07');
insert into TB_ETC_INFO
values ('2019095', 'NAMKYUNG SOMANG', 'S02,S07,S09');
insert into TB_ETC_INFO
values ('2019167', 'han chan hee', 'S01,S07');
insert into TB_ETC_INFO
values ('2019281', 'lee a rum', 'S06');
-----------------------------------------------
--물품정보 테이블
-----------------------------------------------
insert into TB_ITEM_INFO
values ('S01', '의류/잡화');
insert into TB_ITEM_INFO
values ('S02', '뷰티');
insert into TB_ITEM_INFO
values ('S03', '레저/자동차');
insert into TB_ITEM_INFO
values ('S04', '식품');
insert into TB_ITEM_INFO
values ('S05', '생활/건강');
insert into TB_ITEM_INFO
values ('S06', '가구/인테리어');
insert into TB_ITEM_INFO
values ('S07', '가전');
insert into TB_ITEM_INFO
values ('S08', '도서/취미');
insert into TB_ITEM_INFO
values ('S09', '컴퓨터');
insert into TB_ITEM_INFO
values ('S10', '브랜드');
-----------------------------------------------
-- 성적 테이블
-----------------------------------------------
insert into tb_grade
values ('A', 1, '강원진', 87, 94, 98, 0, 0);
insert into tb_grade
values ('A', 2, '나경숙', 68, 86, 78, 0, 0);
insert into tb_grade
values ('B', 1, '박승대', 90, 92, 86, 0, 0);
insert into tb_grade
values ('B', 2, '서유리', 96, 100, 92, 0, 0);
insert into tb_grade
values ('B', 3, '이혜옥', 98, 86, 78, 0, 0);
insert into tb_grade
values ('C', 1, '김진숙', 95, 77, 95, 0, 0);
insert into tb_grade
values ('C', 2, '김한길', 73, 84, 100, 0, 0);
insert into tb_grade
values ('D', 1, '남궁소망', 56, 68, 78, 0, 0);
insert into tb_grade
values ('D', 2, '한찬희', 94, 90, 68, 0, 0);
insert into tb_grade
values ('D', 3, '이아름', 100, 87, 95, 0, 0);
-----------------------------------------------
--7월 성적 테이블
-----------------------------------------------
insert into TB_GRADE_07
values ('T01', 87, 94, 98);
insert into TB_GRADE_07
values ('T02', 68, 86, 78);
insert into TB_GRADE_07
values ('T03', 86, 94, 92);
insert into TB_GRADE_07
values ('T04', 96, 90, 86);
insert into TB_GRADE_07
values ('T05', 92, 92, 96);
-----------------------------------------------
-- 8월 성적 테이블
-----------------------------------------------
insert into TB_GRADE_08
values ('T01', 87, 94, 98);
insert into TB_GRADE_08
values ('T02', 68, 86, 78);
insert into TB_GRADE_08
values ('T04', 90, 92, 86);
insert into TB_GRADE_08
values ('T07', 96, 100, 92);
insert into TB_GRADE_08
values ('T09', 98, 86, 78);
-----------------------------------------------
--9월 성적 테이블
-----------------------------------------------
insert into TB_GRADE_09
values ('T01', 95, 77, 95);
insert into TB_GRADE_09
values ('T04', 73, 84, 100);
insert into TB_GRADE_09
values ('T05', 56, 68, 78);
insert into TB_GRADE_09
values ('T07', 94, 90, 68);
insert into TB_GRADE_09
values ('T08', 100, 87, 95);
-----------------------------------------------
-- 반 정보 테이블
-----------------------------------------------
insert into TB_CLASS_INFO
values ('A', '종합입시반');
insert into TB_CLASS_INFO
values ('B', '단과반');
insert into TB_CLASS_INFO
values ('C', '대학편입반');
insert into TB_CLASS_INFO
values ('D', '일반인반');
-----------------------------------------------
--판매 테이블
-----------------------------------------------
insert into TB_SALES
values ('20190801', 1, '노트북', 1045000, 4);
insert into TB_SALES
values ('20190801', 2, '청소기', 545000, 2);
insert into TB_SALES
values ('20190801', 3, '노트북', 1021000, 6);
insert into TB_SALES
values ('20190802', 1, '선풍기', 70000, 21);
insert into TB_SALES
values ('20190802', 2, '냉장고', 1870000, 7);
insert into TB_SALES
values ('20190803', 1, '선풍기', 92000, 32);
insert into TB_SALES
values ('20190803', 2, '냉장고', 2012000, 3);
insert into TB_SALES
values ('20190803', 3, '선풍기', 7000, 15);
insert into TB_SALES
values ('20190803', 4, '선풍기', 92000, 24);
insert into TB_SALES
values ('20190804', 1, '청소기', 980000, 5);
-----------------------------------------------
--열차시각표 테이블
-----------------------------------------------
insert into TB_TRAIN_TM
values ('101', 1, '서울', '092000', '092000');
insert into TB_TRAIN_TM
values ('101', 2, '수원', '095400', '095600');
insert into TB_TRAIN_TM
values ('101', 3, '대전', '103800', '104100');
insert into TB_TRAIN_TM
values ('101', 4, '대구', '112500', '112730');
insert into TB_TRAIN_TM
values ('101', 5, '부산', '130500', '130500');
insert into TB_TRAIN_TM
values ('103', 1, '서울', '130800', '130800');
insert into TB_TRAIN_TM
values ('103', 2, '대전', '142100', '142300');
insert into TB_TRAIN_TM
values ('103', 3, '대구', '151200', '151430');
insert into TB_TRAIN_TM
values ('103', 4, '부산', '160400', '160400');
insert into TB_TRAIN_TM
values ('106', 1, '부산', '083500', '083500');
insert into TB_TRAIN_TM
values ('106', 2, '대전', '100200', '100530');
insert into TB_TRAIN_TM
values ('106', 3, '서울', '112800', '112800');