sqoop import \ 
--connectjdbc:mysql://upgraddetest.cyaielc9bmnf.us-east-1.rds.amazonaws.com/testdatabase \ 
--table bookings \ 
--username student \ 
--password STUDENT123 \ 
--target-dir /home/hadoop/Capstone/Bookings_Batch_data \ 
-m 1
