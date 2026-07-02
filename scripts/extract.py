SELECT * FROM invoices;

SELECT COUNT(*) AS total_invoices
FROM invoices;

SELECT vendor_name,
COUNT(*) AS total_invoices
FROM invoices
GROUP BY vendor_name;

SELECT payment_status,
COUNT(*) AS total_records
FROM invoices
GROUP BY payment_status;

SELECT SUM(invoice_amount) AS total_amount
FROM invoices;

SELECT vendor_name,
SUM(invoice_amount) AS total_amount
FROM invoices
GROUP BY vendor_name;

SELECT *
FROM invoices
WHERE payment_status='Pending';

SELECT *
FROM invoices
ORDER BY invoice_amount DESC;