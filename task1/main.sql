CREATE OR REPLACE FUNCTION sagar_return_dep_people (strr text)
  RETURNS text /* returns text */
  LANGUAGE sql AS
$func$
   SELECT array_agg(concat( department, ':',people )) /* concat = merge 2 strings together , array_agg: Merge array into one single row */
   as "dep_people"
   FROM  test_sch."apollo_org_job_function"
   WHERE  organization_id LIKE '_______' || strr || '%' /* like clause is used for string comparing */
   and people > 0
$func$;
END; $$
LANGUAGE plpgsql;

select * from sagar_return_dep_people(('2a')) as "dep_people"; /* 2a is example here we haven't used the actual user parameters.

																it will be used in python and our API*/



