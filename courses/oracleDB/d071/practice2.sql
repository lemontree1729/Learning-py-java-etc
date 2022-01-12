select *
from TB_POINT
where REG_DTTM like '2019%'
  and POINT_MEMO like '%구매%'
order by POINT;

select CLASS_CD, sum(KOR), avg(KOR), min(KOR), max(KOR), count(KOR)
from tb_grade
group by CLASS_CD;

select SALES_DT, PRODUCT_NM, sum(SALES_COUNT)
from TB_SALES
where SALES_DT in ('20190802', '20190803')
group by SALES_DT, PRODUCT_NM
order by SALES_DT, PRODUCT_NM;

select distinct TRAIN_NO
from TB_TRAIN_TM;

select distinct PRODUCT_NM
from TB_SALES
where SALES_DT between '20190801' and '20190802'
order by PRODUCT_NM;

select A.CUSTOMER_CD, A.CUSTOMER_NM, A.MW_FLG, B.SEQ_NO, B.POINT_MEMO, B.POINT
from TB_CUSTOMER A,
     TB_POINT B
where A.CUSTOMER_CD = '2019095'
  and A.CUSTOMER_CD(+) = B.CUSTOMER_CD(+);