-- Cities in states with join
SELECT id, name, name FROM cities LEFT JOIN states ON cities.state_id = states.id;