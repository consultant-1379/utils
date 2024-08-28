@echo off

setlocal EnableDelayedExpansion
echo %CD%
set SEARCH_STRING="FAIL" start
echo %SEARCH_STRING

IF EXIST C:\Jenkins\workspace\BIS_UG_ROBOT\ENIQ_TC_Automation\BO\Results\log.html (
    echo log File exists!
    cd C:\Jenkins\workspace\BIS_UG_ROBOT\ENIQ_TC_Automation\BO\Results\
    dir
    for %%f in (*.xml) do (
		echo %%f

	

		for /f "usebackq delims=" %%i in ("%%f") do (
			set "LINE=%%i"
			if "!LINE:%SEARCH_STRING%=!" neq "!LINE!" (
                                echo !LINE:%SEARCH_STRING%=!
                                echo !LINE!
				echo Found "%SEARCH_STRING%" in "%%f"
				goto :found
			)
		)
	)
	
	echo "%SEARCH_STRING%" not found 
	goto :eof
)

else (
    echo log File does not exist. Please check Robot execution.
)


:found
echo Action to take when "%SEARCH_STRING%" is found
echo Running Python script...
    cd ../../..
    python utils/scripts/ENIQ/Automation_Scripts/JIRA/jira_test.py %JOB_NAME% %BUILD_URL%
goto :eof

