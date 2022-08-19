deaths_vs_supply_per_warehouse = """
SELECT deaths_per_warehouse.id, deaths_per_warehouse.name, deaths_num, bags_consumed, 
s.chicken_added, s.bags_added, s.chicken_added - deaths_num AS remaining, s.bags_added - bags_consumed AS bags_remaining
FROM (SELECT s.warehouse_id, Sum(s.chicken_added) as chicken_added, Sum(s.bags_added) as bags_added
	  FROM Supply s
	  GROUP BY s.warehouse_id) as s
JOIN (SELECT w.id, w.name, Sum(d.deaths_num) as deaths_num
      FROM deaths d
      JOIN warehouses w
      ON w.id = d.warehouse_id
      GROUP BY w.id, w.name
      ORDER BY w.id) as deaths_per_warehouse
ON s.warehouse_id = deaths_per_warehouse.id
JOIN (SELECT w.id, Sum(f.bags_consumed) as bags_consumed
      FROM feeding f
      JOIN warehouses w
      ON w.id = f.warehouse_id
      GROUP BY w.id, w.name
      ORDER BY w.id) as bags_consumed_per_warehouse
ON deaths_per_warehouse.id = bags_consumed_per_warehouse.id

     """

payments_per_farm = """
SELECT debit.farm_id, debit.debit_sum, credit.credit_sum
FROM (SELECT d.farm_id, Sum(d.amount) as debit_sum
      FROM debit d
      GROUP BY d.farm_id
      ORDER BY d.farm_id) as debit
FULL OUTER JOIN (SELECT c.farm_id, Sum(c.amount) as credit_sum
      FROM credit c
      GROUP BY c.farm_id
      ORDER BY c.farm_id) as credit
ON debit.farm_id = credit.farm_id
"""