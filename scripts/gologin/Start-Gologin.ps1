$ErrorActionPreference = 'Stop'

$Executable = Join-Path $env:LOCALAPPDATA 'Programs\Gologin\Gologin.exe'

if (-not (Test-Path -LiteralPath $Executable -PathType Leaf)) {
    [Console]::Error.WriteLine("GoLogin executable was not found: $Executable")
    exit 1
}

$Process = Get-Process -Name Gologin -ErrorAction SilentlyContinue |
    Where-Object { $_.MainWindowHandle -ne 0 } |
    Select-Object -First 1

$LaunchedByScript = $false

if (-not $Process) {
    Start-Process -FilePath $Executable | Out-Null
    $Deadline = (Get-Date).AddSeconds(30)

    do {
        Start-Sleep -Milliseconds 250
        $Process = Get-Process -Name Gologin -ErrorAction SilentlyContinue |
            Where-Object { $_.MainWindowHandle -ne 0 } |
            Select-Object -First 1
    } while (-not $Process -and (Get-Date) -lt $Deadline)

    if (-not $Process) {
        [Console]::Error.WriteLine('GoLogin started, but no main window appeared within 30 seconds.')
        exit 2
    }

    $LaunchedByScript = $true
}

[pscustomobject]@{
    Status              = 'window-detected'
    WindowDetected      = $true
    ReadinessConfirmed  = $false
    LaunchedByScript    = $LaunchedByScript
    ProcessResponding   = $Process.Responding
    ProcessId           = $Process.Id
    WindowTitle         = $Process.MainWindowTitle
    WindowHandle = ('0x{0:X}' -f $Process.MainWindowHandle.ToInt64())
    Executable          = $Executable
} | ConvertTo-Json -Depth 3
