@echo off
REM ============================
REM Auto-build MouseMover.exe
REM ============================

echo Cleaning old build files...
rmdir /s /q build
rmdir /s /q dist
del /q main.spec

echo.
echo Building new executable...
pyinstaller --onefile --noconsole --name "MouseJiggler" main.py

echo.
echo Build finished!
echo Your executable is in the "dist" folder.
pause
