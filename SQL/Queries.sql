--get number of students in each school by adding up males and females
SELECT "SCH_NAME",
       SUM("TOT_ENR_M" + "TOT_ENR_F") AS "Total_SCH_ENR"
FROM enrollment
GROUP BY "SCH_NAME"
ORDER BY "SCH_NAME";

--add this total to enrollment
ALTER TABLE enrollment ADD "Total_SCH_ENR" INTEGER;
UPDATE enrollment
SET "Total_SCH_ENR" = subquery.total_enrollment
FROM (
    SELECT "SCH_NAME", SUM("TOT_ENR_M" + "TOT_ENR_F") AS total_enrollment
    FROM enrollment
    GROUP BY "SCH_NAME"
) AS subquery
WHERE enrollment."SCH_NAME" = subquery."SCH_NAME";

--create new table that will show district total vs number of students in poverty per district
CREATE TABLE school_summary (
	lea_name varchar(100),
    district_total INT,  
    title_1_status VARCHAR(10), 
    Total_Title1_Enrolled INT   
);
INSERT INTO SCHOOL_SUMMARY(lea_name, district_total, title_1_status, Total_Title1_Enrolled)
SELECT 
    sd."LEA_NAME",
    sd."LEA_ENR" AS DISTRICT_TOTAL,
    subquery."TITLE_I_STATUS",
    COALESCE(subquery.Total_SCH_ENR, 0) AS Total_Title1_Enrolled
FROM 
    school_data sd
LEFT JOIN (
    SELECT 
        e."LEA_NAME",
        p."TITLE_I_STATUS",
        SUM(e."Total_SCH_ENR") AS Total_SCH_ENR
    FROM 
        enrollment e
    JOIN 
        poverty p ON e."LEA_NAME" = p."LEA_NAME"
    WHERE 
        p."TITLE_I_STATUS" = 'Yes' 
    GROUP BY 
        e."LEA_NAME", p."TITLE_I_STATUS"
) AS subquery ON sd."LEA_NAME" = subquery."LEA_NAME"
ORDER BY 
    sd."LEA_NAME";
