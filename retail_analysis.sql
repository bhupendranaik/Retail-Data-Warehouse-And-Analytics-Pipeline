-- select * from retail_data limit 10;

-- Queries for analysis
-- 1) Total Revenue Per country
SELECT 
    Country, 
    ROUND(SUM(TotalPrice), 2) AS TotalRevenue
FROM retail_data
GROUP BY Country
ORDER BY TotalRevenue DESC;

-- 2)Top 10 Products by Revenue
SELECT 
    Description AS Product, 
    ROUND(SUM(TotalPrice)), 2) AS Revenue
FROM retail_data
GROUP BY Description
ORDER BY Revenue DESC
LIMIT 10;

--3)Sales Over Time (Monthly)
SELECT 
    Month, 
    ROUND(SUM(TotalPrice), 2) AS MonthlyRevenue
FROM retail_data
GROUP BY Month
ORDER BY Month;

-- 4) Top 5 Customers by Spend
SELECT 
    CustomerID, 
    ROUND(SUM(TotalPrice), 2) AS TotalSpend
FROM public.retail
GROUP BY CustomerID
ORDER BY TotalSpend DESC
LIMIT 5;

--5) Average Unit Price by Country
SELECT 
    Country, 
    ROUND(AVG(UnitPrice), 2) AS AvgUnitPrice
FROM public.retail
GROUP BY Country
ORDER BY AvgUnitPrice DESC;


--6)Revenue per Invoice (Useful for Dashboard KPIs)
SELECT 
    InvoiceNo, 
    ROUND(SUM(TotalPrice), 2) AS InvoiceRevenue
FROM public.retail
GROUP BY InvoiceNo
ORDER BY InvoiceRevenue DESC
LIMIT 20;

--7)Rank customers by revenue
SELECT 
    CustomerID,
    SUM(Quantity * UnitPrice) AS TotalSpend,
    RANK() OVER (ORDER BY SUM(Quantity * UnitPrice) DESC) AS Rank
FROM public.retail
GROUP BY CustomerID;

--8) Cumulative sales over time
SELECT 
    InvoiceDate,
    SUM(Quantity * UnitPrice) AS DailySales,
    SUM(SUM(Quantity * UnitPrice)) OVER (ORDER BY InvoiceDate) AS RunningTotal
FROM public.retail
GROUP BY InvoiceDate
ORDER BY InvoiceDate;


