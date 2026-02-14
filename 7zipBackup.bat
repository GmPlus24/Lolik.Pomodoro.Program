rem "C:\Program Files\7-Zip\7z.exe"  -mx9 a -t7z \_Backup\files.7z 

@ECHO ON

rem SET "now=%date:~7,2%%date:~4,2%%date:~12,2%" rem DDMMYY
rem set now=%date:~10,4%%date:~7,2%%date:~4,2%   rem YYYYDDMM
rem SET now=%date:~10,4%-%date:~7,2%-%date:~4,2% rem YYYY-DD-MM
rem SET now=%date:~10,4%-%date:~4,2%-%date:~7,2%  rem YYYY-MM-DD

SET "ttime=%TIME:~0,2%%TIME:~3,2%"
SET now=%date:~10,4%%date:~4,2%%date:~7,2%

SET "ZipName=Lolik__"
SET "DestDir=.\_Backup"
SET "EXCLUDE=!_Backup\"
SET "EXCLUDE0=!__pycache__\"
SET "EXCLUDE1=!venv\"
SET "EXCLUDE2=!Sounds\"
SET "EXCLUDE3=!Icons\"

 "C:\Program Files\7-Zip\7z.exe"  -mx9 a -t7z -x"%EXCLUDE%" -x"%EXCLUDE0%" -x"%EXCLUDE1%" -x"%EXCLUDE2%" -x"%EXCLUDE3%" "%DestDir%\%ZipName%"____"%now%"__"%ttime%"





rem pause