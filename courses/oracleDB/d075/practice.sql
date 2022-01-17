-- join
select CLASS_NM, STUDENT_NM
from TB_GRADE A
         join TB_CLASS_INFO B on A.CLASS_CD = B.CLASS_CD;

select *
from TB_CUSTOMER TC
         join TB_POINT TP on TC.CUSTOMER_CD = TP.CUSTOMER_CD
where CUSTOMER_NM = '남궁소망';

-- rollup
select nvl(CUSTOMER_CD, 'total') as CUSTOMER_CD, sum(POINT) as SUM
from TB_POINT
group by rollup (CUSTOMER_CD);

-- case
select CLASS_CD, STUDENT_NM, case when KOR >= 90 then 'A' else 'F' end as KOR
from TB_GRADE;


select *
from dual;
