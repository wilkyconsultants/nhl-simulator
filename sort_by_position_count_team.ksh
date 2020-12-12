mysql -u root   -e "select  Fposition,count(Fposition),team from nhl_season group by Fposition,team;" -p nhl --password=""|sort -k1n
