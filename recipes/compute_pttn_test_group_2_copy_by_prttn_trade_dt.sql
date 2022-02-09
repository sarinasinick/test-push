SELECT 
    `prttn_trade_dt` AS `prttn_trade_dt`,
    COUNT(*) AS `count`
  FROM (
    SELECT 
        `col1` AS `col1`,
        `prttn_trade_dt` AS `prttn_trade_dt`,
        `col2` AS `col2`
      FROM `pttn_test_group_2_copy`
    ) `dku__beforegrouping`
  GROUP BY `prttn_trade_dt`