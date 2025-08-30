# lib/sql_queries.py

select_all_female_bears_return_name_and_age = """
    SELECT name, age FROM bears WHERE sex = 'F';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT name FROM bears ORDER BY name ASC;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT name, age FROM bears WHERE alive = 1 ORDER BY age ASC;
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT name, age FROM bears ORDER BY age DESC LIMIT 1;
"""

select_youngest_bear_and_returns_name_and_age = """
    SELECT name, age FROM bears ORDER BY age ASC LIMIT 1;
"""

select_all_bears_and_orders_them_by_id = """
    SELECT * FROM bears ORDER BY id ASC;
"""

select_all_bears_names_and_ages_that_are_calm = """
    SELECT name, age FROM bears WHERE temperament = 'calm';
"""

select_bear_with_earliest_birthdate_and_returns_name_and_birthdate = """
    SELECT name, birthdate FROM bears ORDER BY birthdate ASC LIMIT 1;
"""

select_bear_with_latest_birthdate_and_returns_name_and_birthdate = """
    SELECT name, birthdate FROM bears ORDER BY birthdate DESC LIMIT 1;
"""
