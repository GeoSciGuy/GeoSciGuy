(ARRG_STAT_DESC = 'Active') 
And
 ((ST_NAME = 'Oklahoma' And CNTY_NAME NOT IN ('Beaver', 'Beckham', 'Custer', 'Dewey', 'Ellis', 'Greer', 'Harmon', 'Jackson', 'Kiowa', 'Roger Mills', 'Tillman', 'Washita')) 
 OR 
 (ST_NAME = 'Texas' And CNTY_NAME NOT IN ('Hansford', 'Hemphill', 'Hutchinson', 'Lipscomb', 'Ochiltree', 'Roberts', 'Wheeler')))