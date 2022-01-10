select grade.CLASS_CD
from TB_GRADE grade
where CLASS_CD = 'A';

select *
from TB_POINT;

select CUSTOMER_CD, POINT_MEMO, POINT
from TB_POINT;

select *
from TB_CUSTOMER
where BIRTH_DAY < 19900101
  and MW_FLG = 'M';

select *
from TB_CUSTOMER
where length(BIRTH_DAY) < 9;

select length(trim(BIRTH_DAY)), BIRTH_DAY
from TB_CUSTOMER;

select *
from TB_CUSTOMER
where BIRTH_DAY = 1992315;


select CUSTOMER_CD, SEQ_NO, POINT
from TB_POINT
where CUSTOMER_CD = 2017053
  and SEQ_NO = 2;

select *
from TB_GRADE
where CLASS_CD in ('A', 'B')
   or (KOR >= 80 and ENG >= 80 and MAT >= 80);

select *
from TB_POINT
where REG_DTTM between 20180101000000 and 20181231235959
  and POINT between 10000 and 50000;

select CUSTOMER_CD, CUSTOMER_NM, MW_FLG, BIRTH_DAY, TOTAL_POINT
from TB_CUSTOMER
where MW_FLG = 'M'
  and substr(BIRTH_DAY, 6, 1) in (5, 6, 7);

select *
from TB_CUSTOMER
where ((substr(CUSTOMER_CD, 1, 4) = 2017 and MW_FLG = 'M') or (substr(CUSTOMER_CD, 1, 4) = 2019 and MW_FLG = 'W'))
  and TOTAL_POINT <= 30000