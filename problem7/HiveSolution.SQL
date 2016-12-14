-- There is orders table in production which has order_id, order_date, order_csutomer_id and order_status column.
-- Arrange table in such a way that order_id and order_customer_id gets disassociated/gets randomley assigned to each other .

CREATE TEMPORARY TABLE O1 AS 
    SELECT ROW_NUMBER() OVER (ORDER BY RAND()) AS ROWNUM, ORDER_ID 
    FROM ORDERS;


CREATE TEMPORARY TABLE O2 AS 
    SELECT ROW_NUMBER() OVER (ORDER BY RAND()) AS ROWNUM, ORDER_CUSTOMER_ID AS CUST_ID FROM ORDERS;


SELECT O1.ORDER_ID, O2.CUST_ID
    FROM O1 JOIN O2 
    ON O1.ROWNUM = O2.ROWNUM;

DROP TABLE O1;

DROP TABLE O2;
