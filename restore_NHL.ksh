#!/bin/ksh
#
# backup tables
#
echo "Backing up nhl_season and nhl_counter tables from NHL database.."
mysqldump -uroot NHL NHL_Season >NHL_Season.sql
mysqldump -uroot NHL NHL_counter >NHL_Counter.sql
#
# Drop tables
#
echo "Dropping nhl_season and nhl_counter tables from NHL database.."
mysql -uroot nhl < drop_tables.sql
#
# restore tables
#
#echo "Restoring nhl_season and nhl_counter tables to NHL database.."
#mysql -uroot nhl < restore_tables.sql
