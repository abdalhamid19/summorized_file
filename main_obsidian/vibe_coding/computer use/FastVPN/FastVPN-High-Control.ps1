[CmdletBinding()]
param(
    [ValidateSet('Inspect', 'OpenSettings', 'OpenLocations')]
    [string]$Action = 'Inspect',
    [switch]$Pause
)

$ErrorActionPreference = 'Stop'
$runId = Get-Date -Format 'yyyyMMdd-HHmmss'
$logPath = Join-Path $env:TEMP "FastVPN-HighControl-$runId.log"
$exitCode = 0

function Write-LogLines {
    param([object[]]$Lines)

    foreach ($line in $Lines) {
        $text = [string]$line
        Write-Host $text
        Add-Content -LiteralPath $logPath -Value $text
    }
}

try {
    "Action=$Action" | Set-Content -LiteralPath $logPath
    $groups = & "$env:WINDIR\System32\whoami.exe" /groups 2>&1
    $whoamiExitCode = $LASTEXITCODE
    $highLabel = $groups | Where-Object { $_ -match 'S-1-16-12288' } | Select-Object -First 1
    if ($whoamiExitCode -ne 0 -or -not $highLabel) {
        throw 'This PowerShell process is not High. Start it with Start-Process -Verb RunAs and approve the UAC prompt.'
    }

    Write-LogLines @("PowerShellPID=$PID", "Integrity=High (S-1-16-12288)")
    $winappCommand = Get-Command -Name 'winapp.exe' -CommandType Application -ErrorAction Stop
    $winappPath = $winappCommand.Source
    $targets = @(Get-Process -Name 'FastVPN' -ErrorAction Stop)
    if ($targets.Count -ne 1) {
        throw "Expected exactly one FastVPN process; found $($targets.Count). No UI command was run."
    }

    $targetPid = $targets[0].Id
    Write-LogLines @("FastVPNPID=$targetPid", "winapp.exe=$winappPath")

    if ($Action -eq 'Inspect') {
        $inspectArgs = @('ui', 'inspect', '-a', [string]$targetPid, '--interactive')
        $inspectOutput = & $winappPath @inspectArgs 2>&1
        $inspectExitCode = $LASTEXITCODE
        Write-LogLines $inspectOutput
        Write-LogLines @("InspectExitCode=$inspectExitCode", "Log=$logPath")
        if ($inspectExitCode -ne 0) {
            throw "winapp ui inspect failed with exit code $inspectExitCode."
        }
    }
    else {
        $beforeImage = Join-Path $env:TEMP "FastVPN-$Action-$runId-before.png"
        $beforeImageArgs = @('ui', 'screenshot', '-a', [string]$targetPid, '-o', $beforeImage)
        $beforeImageOutput = & $winappPath @beforeImageArgs 2>&1
        $beforeImageExitCode = $LASTEXITCODE
        Write-LogLines $beforeImageOutput
        if ($beforeImageExitCode -ne 0) {
            throw "The before screenshot failed with exit code $beforeImageExitCode; no click was run."
        }

        $beforeInspectArgs = @('ui', 'inspect', '-a', [string]$targetPid, '--interactive')
        $beforeInspect = & $winappPath @beforeInspectArgs 2>&1
        $beforeInspectExitCode = $LASTEXITCODE
        Write-LogLines $beforeInspect
        if ($beforeInspectExitCode -ne 0) {
            throw "The before inspection failed with exit code $beforeInspectExitCode; no click was run."
        }

        $selector = if ($Action -eq 'OpenSettings') { 'Settings' } else { 'LocationsTitle' }
        $clickArgs = @('ui', 'click', $selector, '-a', [string]$targetPid, '--quiet')
        $clickOutput = & $winappPath @clickArgs 2>&1
        $clickExitCode = $LASTEXITCODE
        Write-LogLines $clickOutput
        Write-LogLines @("Selector=$selector", "ClickExitCode=$clickExitCode")
        if ($clickExitCode -ne 0) {
            throw "winapp ui click failed with exit code $clickExitCode."
        }

        Start-Sleep -Seconds 2
        $afterInspectArgs = @('ui', 'inspect', '-a', [string]$targetPid, '--interactive')
        $afterInspect = & $winappPath @afterInspectArgs 2>&1
        $afterInspectExitCode = $LASTEXITCODE
        Write-LogLines $afterInspect
        if ($afterInspectExitCode -ne 0) {
            throw "The after inspection failed with exit code $afterInspectExitCode."
        }

        $afterImage = Join-Path $env:TEMP "FastVPN-$Action-$runId-after.png"
        $afterImageArgs = @('ui', 'screenshot', '-a', [string]$targetPid, '-o', $afterImage)
        $afterImageOutput = & $winappPath @afterImageArgs 2>&1
        $afterImageExitCode = $LASTEXITCODE
        Write-LogLines $afterImageOutput
        if ($afterImageExitCode -ne 0) {
            throw "The after screenshot failed with exit code $afterImageExitCode."
        }

        Write-LogLines @("BeforeScreenshot=$beforeImage", "AfterScreenshot=$afterImage", "Log=$logPath")
    }
}
catch {
    $exitCode = 1
    Write-LogLines @("ERROR=$($_.Exception.Message)", "Log=$logPath")
}

if ($Pause) {
    Read-Host 'Press Enter to close this elevated window' | Out-Null
}

exit $exitCode
