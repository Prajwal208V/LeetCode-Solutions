1-- Write your PostgreSQL query statement below
2SELECT patient_id, patient_name, conditions -- select patient details
3FROM Patients
4WHERE conditions LIKE 'DIAB1%' -- condition starts with DIAB1
5   OR conditions LIKE '% DIAB1%'; -- condition appears after a space