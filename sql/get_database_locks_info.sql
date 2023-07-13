
/**
GETS ANY DATABASE LOCKS ASSOCIATED WITH A SPECIFIC DATBASE OBJECT ID
**/

SELECT *
FROM sys.dm_tran_locks 
WHERE resource_associated_entity_id = object_id('table_name');


/**
GETS SQL SESSION INFO ON ANY SESSION THAT HAS AN ASSOCIATED DATABASE LOCK
**/

SELECT DISTINCT
        name AS database_name,
        session_id,
        host_name,
        login_time,
        login_name,
        reads,
        writes
FROM sys.dm_exec_sessions
    LEFT OUTER JOIN sys.dm_tran_locks ON sys.dm_exec_sessions.session_id = sys.dm_tran_locks.request_session_id
    INNER JOIN sys.databases ON sys.dm_tran_locks.resource_database_id = sys.databases.database_id
WHERE   resource_type <> 'DATABASE'
--AND name ='YourDatabaseNameHere'
ORDER BY name


/** 
KILLS PROCESS HAVING session_id = 33
**/

KILL 33
