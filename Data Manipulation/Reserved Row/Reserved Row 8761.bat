@set @n=0;/* & echo off
pushd %~dp0
for /f "delims=" %%a in ('dir /b *.dat') do (
        cscript -nologo -e:jscript "%~0"<"%%a">$
        move $ "%%a"
)
pause & exit/b & rem */

ar = WScript.StdIn.ReadAll().split("\r\n");
WScript.Echo(ar.slice(0,8761).join("\r\n"))