$ErrorActionPreference = 'Stop'
$ghidraHome = $env:GHIDRA_INSTALL_DIR
if ([string]::IsNullOrWhiteSpace($ghidraHome)) { $ghidraHome = Join-Path $env:LOCALAPPDATA 'Programs\Ghidra\ghidra_12.2_PUBLIC' }
$javaHome = $env:GHIDRA_JAVA_HOME
if ([string]::IsNullOrWhiteSpace($javaHome)) { $javaHome = Join-Path $env:LOCALAPPDATA 'Programs\Java\jdk-25.0.5+8' }
$launcher = Join-Path $ghidraHome 'ghidraRun.bat'
if (-not (Test-Path -LiteralPath $launcher)) { throw "Ghidra launcher not found: $launcher" }
if (-not (Test-Path -LiteralPath (Join-Path $javaHome 'bin\java.exe'))) { throw "Java 25 not found: $javaHome" }
$env:JAVA_HOME = $javaHome
$env:PATH = (Join-Path $javaHome 'bin') + [IO.Path]::PathSeparator + $env:PATH
& $launcher @args
exit $LASTEXITCODE
